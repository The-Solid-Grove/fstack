#!/usr/bin/env python3
"""Exercise the public checker deadline against a slowly streaming Git remote."""

import socket
import subprocess
import sys
import threading
import time


checker, repo = sys.argv[1:]
sha = subprocess.check_output(["git", "-C", repo, "rev-parse", "HEAD"]).strip()
closed = threading.Event()

with socket.socket() as listener:
    listener.bind(("127.0.0.1", 0))
    listener.listen()

    def serve():
        connection, _ = listener.accept()
        with connection:
            connection.recv(8192)
            service = b"# service=git-upload-pack\n"
            prefix = f"{len(service) + 4:04x}".encode() + service + b"0000"
            ref = sha + b" refs/heads/main\x00multi_ack\n"
            data = f"{len(ref) + 4:04x}".encode() + ref + b"0000"
            connection.sendall(
                b"HTTP/1.1 200 OK\r\n"
                b"Content-Type: application/x-git-upload-pack-advertisement\r\n"
                b"Content-Length: " + str(len(prefix) + len(data)).encode()
                + b"\r\n\r\n" + prefix
            )
            connection.settimeout(0.1)
            try:
                # Enough body traffic to avoid Git's low-speed timeout, but
                # never a complete ref before the checker's 15-second deadline.
                for offset in range(0, len(data), 2):
                    connection.sendall(data[offset:offset + 2])
                    try:
                        if connection.recv(1) == b"":
                            closed.set()
                            return
                    except socket.timeout:
                        pass
                    time.sleep(0.9)
            except OSError:
                closed.set()

    threading.Thread(target=serve, daemon=True).start()
    url = f"http://127.0.0.1:{listener.getsockname()[1]}/repo.git"
    subprocess.run(["git", "-C", repo, "remote", "add", "origin", url], check=True)
    try:
        start = time.monotonic()
        result = subprocess.run(
            ["bash", checker, "--repo-root", repo, "--quiet"],
            text=True, capture_output=True, timeout=20,
        )
        elapsed = time.monotonic() - start
        assert result.returncode == 0, result
        assert not result.stdout and not result.stderr, result
        assert 14 <= elapsed < 19, f"watchdog was not exercised: {elapsed:.1f}s"
        assert closed.wait(2), "Git transport stayed open after the checker returned"
    finally:
        subprocess.run(["git", "-C", repo, "remote", "remove", "origin"], check=True)

print("ok: stalled Git transport stops at the deadline and quiet stays silent")

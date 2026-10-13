// Floating variant switcher for brainstorm boards. Throwaway review tooling.
// <script src="switcher.js" data-variants="a:Current,b:Inline CTA,c:Value first,d:Progress"></script>
// Updates ?variant= (other params are kept) and reloads; ← and → cycle.
(() => {
  const script = document.currentScript;
  const variants = script.dataset.variants.split(",").map((v) => {
    const [key, ...name] = v.split(":");
    return { key: key.trim(), name: name.join(":").trim() };
  });
  const params = new URLSearchParams(location.search);
  const index = Math.max(0, variants.findIndex((v) => v.key === params.get("variant")));
  const go = (step) => {
    params.set("variant", variants[(index + step + variants.length) % variants.length].key);
    location.search = params.toString();
  };

  const bar = document.createElement("div");
  bar.setAttribute("role", "toolbar");
  bar.setAttribute("aria-label", "Brainstorm variants");
  bar.style.cssText = "position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:2147483647;" +
    "display:flex;align-items:center;gap:4px;padding:6px;border-radius:999px;background:#132C25;color:#F0F2E9;" +
    "font:600 13px/1 system-ui,sans-serif;box-shadow:0 8px 24px rgba(0,0,0,.25)";
  const button = (label, step) => {
    const b = document.createElement("button");
    b.type = "button";
    b.textContent = label;
    b.setAttribute("aria-label", step < 0 ? "Previous variant" : "Next variant");
    b.style.cssText = "width:36px;height:36px;border:0;border-radius:999px;background:#183A31;color:inherit;font:inherit;cursor:pointer";
    b.onclick = () => go(step);
    return b;
  };
  const label = document.createElement("span");
  const current = variants[index];
  label.textContent = `${current.key.toUpperCase()}${current.name ? ` · ${current.name}` : ""}  (${index + 1}/${variants.length})`;
  label.style.cssText = "padding:0 12px;white-space:nowrap";
  bar.append(button("←", -1), label, button("→", 1));
  if (document.body) document.body.append(bar);
  else document.addEventListener("DOMContentLoaded", () => document.body.append(bar));

  addEventListener("keydown", (event) => {
    if (event.target.closest?.("input, textarea, select, [contenteditable]")) return;
    if (event.key === "ArrowLeft") go(-1);
    if (event.key === "ArrowRight") go(1);
  });
})();

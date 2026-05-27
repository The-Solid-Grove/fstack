# Edit Funnel QA Publish Flow Design

## Goal

Update `edit-funnel` so hosted funnel edits default to a local preview loop, require an explicit publish decision, and run meaningful QA before preview-to-production promotion.

## Scope

This change updates skill guidance, README usage docs, and smoke coverage. It does not add an executable QA runner because `fstack` is a skill pack and each synced funnel may have different local scripts, checkout tooling, test payment setup, and subscription state.

## Workflow

The skill should guide agents through this flow:

1. Edit the local synced funnel tree.
2. Run available local checks.
3. Start or open the local preview by default.
4. Inspect the local preview, then adjust and repeat until the local result is acceptable.
5. Ask the user whether to publish.
6. If the user says yes, publish to preview.
7. Run the QA checklist on the preview URL.
8. Publish to production only after preview QA passes and the user has explicitly requested production publish.
9. Run the QA checklist again on the production URL.

For major edits, the skill should ask whether to run the full QA checklist even before publish. Major edits include checkout, pricing, payment, subscription, cancellation, identity/email capture, routing, analytics, or broad visual/flow changes.

## QA Checklist

Full QA covers:

- add or submit email
- make a test payment, or verify the payment path with the target-approved equivalent
- close checkout and reopen it to confirm the larger discount path
- visit `/manage-subscription` and verify the cancellation flow

If a flow cannot run because test credentials, payment mode, an existing subscription, or route support is unavailable, the agent must report the skipped flow as a named blocker or explicit unavailable item. Production completion must not be claimed when production QA fails or is unavailable unless the user explicitly accepts that risk.

## Files

- `skills/edit-funnel/SKILL.md`: update the workflow, publish gate, QA checklist, and completion gate.
- `README.md`: update the public usage sequence.
- `tests/smoke.sh`: add regression assertions for local preview, publish confirmation, preview QA, production QA, discount reopen QA, email QA, payment QA, and `/manage-subscription` cancellation QA.

## Testing

Use `bash tests/smoke.sh`. The smoke test should fail before the skill/README wording is updated and pass after the workflow includes the new gates.

# Identity and entitlement map

## IDs

| System | Identifier | Created when | How is it linked to the internal user? |
| --- | --- | --- | --- |
| Browser/session | | | |
| Funnel user | | | |
| Authentication | | | |
| Payment customer | | | |
| Subscription | | | |
| App user | | | |

## Entitlement states

| Billing state | Access state | User message | Trigger/event | Recovery |
| --- | --- | --- | --- | --- |
| pending | | | | |
| active | | | | |
| past due/grace | | | | |
| canceled, paid-through | | | | |
| expired/unpaid | | | | |
| refunded/disputed | | | | |

## Handoff journeys

App already installed:

New install:

Desktop purchase → phone:

Lost deep link:

Wrong email/account:

Paid but no access:

## Failure-path matrix

| Failure | Detection | Source of truth | Automatic recovery | User message | Manual owner | SLA | Analytics event |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Webhook delayed | | | | | | | |
| Webhook duplicated | | | | | | | |
| Payment processing | | | | | | | |
| Email typo | | | | | | | |
| Deep link lost | | | | | | | |
| Different app account | | | | | | | |
| Renewal failed | | | | | | | |
| Refund/dispute | | | | | | | |

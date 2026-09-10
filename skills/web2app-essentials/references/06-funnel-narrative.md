# 6. Funnel architecture: mental energy and storytelling

## Lesson outcome

You'll turn the brief into a screen-by-screen narrative where every screen either adds mental energy or spends it deliberately.

## Mental energy model

Mental energy here is a working metaphor for design review, not a scientific quantity and not a standalone analytics metric. In production, measure observable behavior: completion, time, exits, errors, and downstream purchase quality.

After the click, the user arrives with a small reserve of attention, curiosity, and motivation. At every step they either gain energy or lose it.

Energy grows when a screen:

- continues the promise of the creative;
- shows a personally relevant insight;
- gives clear feedback;
- reduces uncertainty;
- demonstrates progress;
- builds trust with real proof;
- makes the outcome more concrete.

Energy drops when a screen:

- asks for effort without value;
- repeats generic questions;
- carries too much text or too many decisions;
- looks like bait-and-switch;
- triggers fear and offers no relief;
- sells too early;
- creates an expectation the product will not meet.

The goal is not to make every screen pleasant. By the paywall, enough perceived value and commitment should have accumulated that the purchase feels like a logical continuation of the path.

## Ask screens and give screens

An **ask screen** asks the user to spend energy: pick an answer, read, enter data, wait, or make a decision.

A **give screen** returns energy: it explains, shows a result, confirms progress, gives feedback, or removes a barrier.

After two or three ask screens you usually need a give screen. This is not a hard number, it is a way to see quiz fatigue before launch.

An example rhythm:

```text
Easy goal question      — ask
Immediate confirmation  — give
Context question        — ask
Pain question           — ask
Mechanism insight       — give
Behavior question       — ask
Personalized projection — give
Commitment              — ask
Result preparation      — give
Email                   — ask
Result + offer          — give/decision
```

## The seven parts of the narrative

### 1. Expectation match

The first screen repeats the specific promise, visual language, and vocabulary of the creative. Don't spend your best attention moment on "Welcome".

The screen needs:

- one outcome;
- one easy action;
- a clear expectation of what happens next.

### 2. Self-recognition

Questions help a person recognize themselves. Start with the goal and observable context, then move to pain and barriers.

Every question should affect the flow or a later interpretation. If an answer is never used, delete the question or admit honestly that it is a research question.

### 3. Problem mechanism

Show why the problem persists. A good mechanism does not blame the user. It turns "something is wrong with me" into "the old approach did not account for an important part of the system".

Use a diagram, a short comparison, a chart, or a concrete example. Verify scientific, medical, financial, and legal claims.

### 4. Feedback and branching

After a meaningful answer, show the consequence:

- "Your bottleneck is most likely here…"
- "We will take this into account when building your plan…"
- "For this goal, consistency matters more than intensity…"

In one funnel we built, a positive answer opened a separate evidence/interstitial screen, while a negative answer led straight on. That made the branch shorter for an irrelevant person and richer for a relevant one.

### 5. Future state

Show point B as a trajectory, not a guarantee. You can use:

- a timeline;
- a progress curve;
- a before/after state;
- a personalized plan outline;
- a readiness score;
- a first-week schedule.

Every range, date, and prediction needs a real model behind it or clearly stated assumptions.

### 6. Commitment and result preparation

Before the offer, the user can confirm the goal, choose a time commitment, or set preferences. Active commitment is useful when it affects the plan.

The loader must not depict an analysis that does not exist. If the backend really does build the result, show the real stages. If processing is instant, a short transition with a useful explanation works better.

### 7. Email and offer

Ask for the email in exchange for a function:

- save the result;
- create an account;
- send the plan;
- link the purchase to app access.

After the email, show the result and the offer as the conclusion of the path the user has just taken. Don't start a new sales story on the paywall.

## Screen rule

Fill this in for every screen:

| Field | Question |
| --- | --- |
| Job | why does this screen exist? |
| Message | what single thought should the person take away? |
| Energy | does it add or spend energy? |
| Input | what should the person do? |
| Payoff | what do they get for that action? |
| Data | is the answer stored, and where is it used? |
| Next | how is the next screen chosen? |
| Proof | are sources or real testimonials needed? |

If the Job cannot be described in one line, the screen is overloaded.

## Funnel length

Don't optimize the number of screens for its own sake. A short funnel may fail to create desire. A long one can hold attention if every question is relevant and a payoff appears regularly.

The right length is the shortest sequence that:

1. delivers on the entry promise;
2. diagnoses the important context;
3. explains the mechanism;
4. creates a personalized result;
5. removes the main barriers;
6. makes the offer clear.

## The first screen carries extra weight

Before the second screen, the user has invested nothing. Check:

- loading speed;
- mobile viewport;
- headline/creative match;
- clarity of the first tap;
- absence of unnecessary choices;
- behavior inside Meta/TikTok webviews.

A large mid-funnel redesign will not save a weak entry screen.

## Exercise

Build a table of all screens. Mark each one `+`, `−`, or `0` in the energy column. Then:

- delete zero-value screens;
- add feedback or an insight after clusters of ask screens;
- check that by the paywall the user has seen every value the paywall promises;
- run a five-second test on each screen: what single thought remains?

## Worksheet

[Open the screen map and energy audit](templates/05-screen-map.md)

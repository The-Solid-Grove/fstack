# 12min — Copy Swipe (verbatim from source)
> Source: rag-catalog/12min. Extracted from step source files (`src/steps/step-01.tsx` … `step-11.tsx`) in manifest sequence order. Shared header/back live in `twelve-min-ui.tsx`. The manifest defines 11 steps; the long-form paywall is step 11. There are no separate subscription-started / upsell / cancellation step files in this funnel.

## Shared UI (twelve-min-ui.tsx)
- **Back button:** "Go back"
- **CTA component default label (per-step):** "Continue"

## Step 1 — age picker / intro hero
- **Headline:** "Become the Most Interesting Person at the Table"
- **Kicker:** "3-MINUTE QUIZ"
- **Options:** "Age: 18-24 →", "Age: 25-34 →", "Age: 35-44 →", "Age: 45+ →"

## Step 2 — book interest (single choice)
- **Headline:** "Is this book interesting to you?"
- **Options:** "No", "Yes" (book shown: The Power of Habit)

## Step 3 — email capture
- **Headline:** "Achieve your goals with the 12min App."
- **Subhead/body:** "Create an account to access your personalized plan"
- **Checkbox:** "I want to receive exclusive offers, personalized content, and updates about products and services."
- **CTA:** "Continue"
- **Other:** awards image ("12min awards")

## Step 4 — plan ready (summary)
- **Headline:** "Your personal development plan is ready!"
- **Subhead/body:** "Based on your answers, we have created a development plan with readings that will help you improve exactly where you need to."
- **Chart labels:** "20 books" / "per month", "Now", {start date}, {end date} (today and +3 months, e.g. "June 15" / "September 15")
- **Footnote:** "*To use the 12min app, you need an Android or iPhone."
- **CTA:** "Continue"

## Step 5 — improve topics (multi-select)
- **Headline:** "What Would You Like to Improve?"
- **Progress label:** "Profile"
- **Options (chips):** "Understanding Emotions", "Motivation", "Nutrition", "Habits", "Self-Confidence", "Mindset", "Self-Care", "Fitness Life", "Empathy", "Dating and Marriage", "Personal Finances", "Creativity"
- **CTA:** "Continue" (disabled until 1+ selected)

## Step 6 — learning concepts (interstitial)
- **Headline:** "Learn Great Concepts in Minutes, Not Hours"
- **Subhead/body:** "Read or listen to the main concepts of any book in just 12 minutes with our app. This way, it is easier to find time to put learnings into practice."
- **Progress label:** "Profile"
- **CTA:** "Continue"

## Step 7 — patterns / positive framing (interstitial)
- **Headline:** "Focusing on the positive aspects is a great way to motivate yourself even more."
- **Subhead/body:** "The development plan we are creating for you will include books that will teach you how to stay positive and know when it is time to move on to your next achievements."
- **Progress label:** "Patterns"
- **CTA:** "Continue"

## Step 8 — patterns / social proof (interstitial)
- **Headline:** "Last month, our users read/listened to over 300,000 microbooks!"
- **Subhead/body:** "Join 12min and finally make time to learn in your busy life."
- **Progress label:** "Patterns"
- **CTA:** "Continue"

## Step 9 — specific goals (multi-select)
- **Headline:** "Do you have a specific goal at the moment?"
- **Options:** "🙋 Get a promotion", "📊 Becoming an entrepreneur", "💑 Relationship commitment", "👨‍👩‍👧 Parenthood", "✈️ Major life transition", "🤯 Mental and emotional well-being", "🏦 Financial milestone", "🏖️ Retirement planning"
- **CTA:** "Continue" (disabled until 1+ selected)

## Step 10 — summary bridge
- **Headline:** "Become the most interesting person at the table!"
- **Subhead/body:** "Based on your answers, we have created your personal development plan."
- **CTA:** "Continue"

## Step 11 — long-form annual paywall
- **Headline:** "Learn fast and exceed your expectations"
- **Subhead/body:** "Join the 12min community of over 5,274,333 people"
- **Offer timer:** "00:13:50" / "Limited time offer"
- **Plan 1 (selected):** badge "40% OFF" — "Premium Annual" — ~~US$ 4.98/mo~~ — "US$ 2.98/mo" — "Unconditional 7-day guarantee period"
- **Guarantee box:** "How the guarantee works:"
  - "Today" — "Start enjoying everything the 12min library has to offer. If you do not like it, request a refund within the next 7 days and we return your money."
  - "Day 5" — "We send a reminder that your guarantee period is ending."
  - "Day 7" — "Last day to request your refund."
- **Plan 2 (secondary):** "Premium Monthly" — "US$ 11.77/mo" — "Unconditional 7-day guarantee"
- **FAQ section:** "Frequently Asked Questions"
  - Q: "What is 12min?" / A: "At the 12min App, we extract the best ideas and insights from the world's bestselling nonfiction books and organize them into unique and self-contained summaries that can be consumed in audio and/or text in about 12 minutes!"
  - Q: "How does the guarantee period work?"
  - Q: "Can I change my subscription plan?"
  - Q: "What does 12min Premium give me access to?"
  - Q: "Can I cancel my subscription during the trial period?"
  - Q: "I still have questions. How can I contact you?"
- **Footer:** "Rua. Castelo de Alcazar, 125 - Castelo - Belo Horizonte/MG." / "About • Terms of Use"
- **CTA (sticky):** "Continue"

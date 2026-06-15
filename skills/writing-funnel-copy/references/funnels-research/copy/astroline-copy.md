# Astroline — Copy Swipe (verbatim from source)
> Source: rag-catalog/astroline. Copy is inline in `src/steps/step-NN.tsx`. Step order from `src/config/funnel.sequence.ts` / `funnel.steps.ts`. Some headlines (speech bubbles, summary cards) are dynamically composed from user answers — static literal copy captured below.

## step-1 — Landing / gender select
- **Brand:** "Astroline"
- **Headline:** "Personalized astrology report with powerful predictions"
- **Body:** "Complete a 1-minute quiz to get a personalized prediction. The result is not guaranteed and may vary from case to case."
- **Question:** "Select your gender to start"
- **Options:** "Female", "Male", "Non-binary"

## step-2 — Birthday picker
- **Headline:** "When's your birthday?"
- **Subhead:** "It's also important to know your date of birth for making complete and accurate predictions"
- **Column labels:** "Month", "Day", "Year"
- **CTA:** "Continue"

## step-3 — Birth time picker
- **Headline:** "Do you know your birth time?"
- **Subhead:** "This helps us find out where planets were placed in the sky at the moment of your birth"
- **Microcopy:** "I don't remember"
- **CTA:** "Continue"

## step-4 — Birth place input
- **Headline:** "Where were you born?"
- **Subhead:** "The place is important to explore your core personality traits, needs, and desires"
- **Placeholder:** "Detecting your city..." (then "Enter your city")
- **CTA:** "Continue"

## step-5 — Chart mapping interstitial (auto-advance)
- **Headline:** "Mapping your birth chart..."
- **Chips:** "🧩Your challenges", "🧭Your approach to life", "🦋Your transformations", "🌙Your intuition and dreams"

## step-6 — Chart snapshot reveal
- **Speech bubble:** "Your chart shows a rare spark - let's discover your best match"
- **Zodiac stat labels:** "Moon Sign", "Sun Sign", "Ascendant"
- **CTA:** "Continue"

## step-7 — Forecast accuracy (34%)
- **Headline:** "Forecast accuracy"
- **Orb value:** 34
- **Speech bubble:** "The cosmic energy is building up! Share a bit more to reveal what's driving you"
- **CTA:** "Continue"

## step-8 — Relationship status
- **Headline:** "To get started, tell us about your current relationship status"
- **Options:** "💕 In a relationship", "💔 Just broke up", "🥰 Engaged", "💍 Married", "💫 Looking for a soulmate", "😌 Single", "🤔 It's complicated"

## step-9 — Future goals (multi-select, pick 3)
- **Headline:** "What are your goals for the future?"
- **Counter:** "Selected: {n}/3"
- **Options:** "❤ Family harmony", "💼 Career", "💊 Health", "💍 Getting married", "🌎 Traveling the world", "🎓 Education", "👥 Friends", "👩‍🍼 Children"

## step-10 — Color preference
- **Headline:** "Which of the following colors do you prefer?"
- **Subhead:** "The color is important for better personalization"
- **Options:** "Red", "Yellow", "Blue", "Orange", "Green", "Violet"

## step-11 — Nature element
- **Headline:** "Which element of nature do you like the best?"
- **Subhead:** "The element of nature is important for better personalization"
- **Options:** "Earth", "Water", "Fire", "Air"

## step-12 — Profile summary (auto-advance)
- **Details card defaults:** title "You"; meta "Woman • Capricorn • Earth"; "Modality" / default "Cardinal"; "Polarity" / default "Feminine"; pill "Your Details"
- **Trait type labels:** "Moon Sign", "Sun Sign", "Ascendant"

## step-13 — Profile summary + advisor
- **Speech bubble (templated):** "Your {Sun sign} chart{ in {city}} shows a rare spark for {goal} - let's align it with your {relationship} energy."
- **Details card:** shows traits ("Moon Sign", "Sun Sign", "Ascendant"); side labels "Modality", "Polarity"; details/meta lines composed from answers (e.g. "{color} • {element} Focus", "{gender} • {Sun sign} • {element}")
- **CTA:** "Continue"

## step-14 — Forecast accuracy (67%)
- **Headline:** "Forecast accuracy"
- **Orb value:** 67
- **Speech bubble:** "You're close to a big reveal! Confirm one last thing and see your full story"
- **CTA:** "Continue"

## step-15 — Palm photo prompt
- **Headline:** "Take a photo of your left palm"
- **Palm chips:** "👩‍🍼 Children", "💼 Career", "💞 Marriage", "⏳ Big Change", "💸 Money"
- **Legal:** "These readings are for entertainment purposes only and should not be taken as 100% accurate"
- **Privacy:** "Privacy is a priority for us. We only process non-identifiable data to ensure anonymity"
- **CTA:** "Take a photo" (states: "Opening camera...", "Uploading...")
- **Secondary CTA:** "Upload palm photo" (uploading: "Uploading...")
- **Camera modal:** "Cancel", "Use this photo"
- **Errors:** "Could not start camera preview. Please upload a photo instead.", "Live camera requires HTTPS. Using file capture fallback.", "Camera access was blocked. Please allow camera access or upload a photo.", "Could not capture a frame from camera. Please upload a photo instead.", "Could not process captured photo. Please upload a photo instead.", "Photo upload failed. Try again."

## step-16 — Palm scan interstitial
- **Scan messages:** "Analyzing your palm shape...", "Scanning your fingers...", "Identifying lines, mounts and plains...", "Generating your palm reading result..."
- **Microcopy:** progress number shown (starts 44, to 100)

## step-17 — Palm reading report + email capture
- **Report card title:** "Overview"
- **Score rows:** "Love" 85%, "Health" 80%, "Wisdom" 78%, "Career" 91%
- **Report copy:** "Your Heart Line demonstrates your emotional stability and approachable demeanor."
- **Report copy:** "Your Life Line suggests several challenges that can affect you in the future."
- **Sheet headline:** "Sign up to understand yourself better with Astroline"
- **Placeholder:** "Enter your email"
- **Privacy:** "🛡 Your personal data is safe with us. We'll use your email for updates, receipts, and subscription details."
- **CTA:** "Continue"

## step-18 — Palm chat setup interstitial (auto-advance)
- **Headline:** "Setting up our Palm Reading chat..."

## step-19 — Paywall offer

### Hero
- **Brand:** "Astroline"
- **Headline:** "Your {Sun sign} Palm Reading Is Ready!"
- **Floating chips:** "👩‍🍼 Children", "💞 Marriage", "⏳ Big change at {age}", "💸 Money success at {age}"
- **CTA:** "Get My Prediction"

### Pricing
- **Section title:** "Unlock predictions"
- **Plans:**
  - "1-Week Trial" — $1 (old $4.99) — "then 2-Week Plan $19.99" — side "1-WEEK trial"
  - "2-Week Trial" — $5.49 (old $9.99) — "then 2-Week Plan $19.99" — side "2-WEEK trial" — tag "Most popular"
  - "4-Week Trial" — $9.99 (old $19.99) — "then 1-Month Plan $29.99" — side "4-WEEK trial" — tag "SAVE 50%"
- **CTA:** "Start Trial and Continue"
- **Terms checkbox:** "I confirm that I have read and agree to the Terms of Use, Billing Terms and Money-back Policy. Start your 14-day trial for {price}. Then continue on a recurring plan until canceled."
- **Trust line:** "Guaranteed safe checkout"

### Palm reading card
- **Title:** "Your palm reading"
- **Analysis rows:** "Love" 85%, "Health" 80%, "Wisdom" 78%, "Career" 91%
- **Copy:** "Your Heart Line shows that you are very passionate and freely express your thoughts and feelings."
- **Copy:** "Your Life Line depicts that your physical health requires hard work to improve."
- **Microcopy:** "More data in the full report"
- **CTA:** "Get Full Report"

### Advisors
- **Headline:** "Gain insights from professional advisors"
- **Body:** "Our advisors provide astrological readings to help you understand yourself better"

### Share card
- **Tip:** "This card was made for you"
- **Tip body:** "You may share it with friends or partners to let them explore your astrological self"
- **Card name:** "You"
- **Card meta (templated):** "{gender} • {Sun sign} • {element}"
- **Action:** "Customize and Share"

### 2026 Forecast
- **Headline:** "Your Free 2026 Astrology Forecast"
- **Items:**
  - "Full Year Overview" — "Your personal roadmap for all of 2026"
  - "Major Cosmic Events" — "How big transits will shape your year"
  - "Moon Calendar 2026" — "Best days for love, energy & decisions"
  - "Retrogrades Explained" — "Avoid setbacks & use cosmic timing"
  - "Zodiac Forecasts" — "See how 2026 unfolds for your sign"
- **CTA:** "Get 2026 Forecast"

### Social proof
- **Number:** "3.4 million"
- **Copy:** "users worldwide use Astroline to understand themselves better"

### Birth chart analysis
- **Headline:** "Your birth chart analysis"
- **Body:** "Your true path of life and hidden opportunities"
- **List:** "Your purpose and mission", "Your hidden talents", "Your priorities and values"
- **CTA:** "Get Full Report"

### Compatibility profile
- **Headline:** "Your compatibility profile"
- **Body:** "How to improve relationships and build deeper emotional harmony."
- **CTA:** "Get Full Report"

### Footer
- **Links:** "Privacy Policy", "Terms of Use", "Billing Terms"

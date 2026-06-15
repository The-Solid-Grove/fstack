# Blesse — Copy Swipe (verbatim from source)
> Source: rag-catalog/blesse. (Brand shown on-screen: "Perfect Prayer".)

## Step 1 — Landing intro + gender (intro_hero)
- **Promo banner:** "🎁 The Presentation of Jesus Day -70% OFF! 🎁"
- **Language selector:** "🇺🇸"
- **Logo alt:** "Perfect Prayer"
- **Headline:** "Personalized way to / spirituality"
- **Bullets:** "Feel closer to God", "Develop a prayer routine", "Find your inner peace", "Understand God's word"
- **Prompt:** "Choose your gender"
- **Options:** "Male", "Female"
- **Footer links:** "Access your program", "Perfect Prayer", "Perfect Bible", "Terms & conditions", "Privacy & policy"
- **Footer contact:** "Contact us", "info@blesse.co"
- **Legal:** "2026 © ALL RIGHTS RESERVED", "Disclaimer: results may vary from person to person."

## Step 2 — Journey intro (progress_interstitial; Goals 1/17, ~6%)
- **Headline:** "Your spiritual journey starts / here!"
- **Body:** "We worked for five years to create perfect quiz - a quiz that would give us all the information we need to write fully personalised prayer book **ONLY FOR YOU**"
- **Body:** "Remember, your answers will determine the content of this book, so be honest and read every question carefully."
- **CTA:** "Got it"

## Step 3 — Primary reason (intro_hero; Goals 2/17, ~12%)
- **Headline:** "What is your primary reason / for wanting a prayer book?"
- **Options:**
  - "Reduce stress and anxiety"
  - "Strengthen the relation with God"
  - "Developing a regular practice"
  - "Understand the bible better"
  - "Increase focus and mindfulness"
  - "Get over addiction"
  - "Get over a difficult life situation"

## Step 4 — Daily routine selector (intro_hero; Get to know you 4/17, ~24%)
- **Headline:** "What should your ideal daily / routine include?"
- **Options:** "Morning Prayer", "Evening Prayer", "Bible Verse", "Mealtime Blessing", "Journaling & Reflections", "Bible Reading & Daily Devotional", "Christian Meditation", "Daily Affirmation", "Bible Sleep Story"
- **CTA:** "Continue"

## Step 5 — Benefits summary (summary_confirmation; Goals 7/17, ~41%)
- **Headline:** "Benefits of Your Personalized / 'Perfect Prayer' Book"
- **Benefits list:**
  - "Custom daily prayers tailored to your spiritual needs"
  - "No need for other prayer books or websites - everything's here"
  - "Stress-free way to connect with God daily"
  - "Curated Bible studies to deepen your faith"
  - "Content that will be useful for the rest of your life"
- **CTA:** "Got it"

## Step 6 — Generation progress (progress_interstitial; auto-advance ~2.4s)
- **Headline:** "We are now generating the / content of your book"
- **Status:** animated percentage ring "{n}%" (animates 0 → 78%)

## Step 7 — Personalized result summary (summary_confirmation; Goals 14/17, ~82%)
- **Headline:** "Would you look at that! Based on / your preferences, we've created"
- **Card body:** "We created personalized content crafted from the most powerful passages of Scripture-made just for you to feel closer to God and his peace."
- **Stats:** "1200+ Personalized Prayers", "140+ Selected Bible Readings"
- **CTA:** "Got it"

## Step 8 — Book cover personalization (paywall_offer; Personalisation 17/17, 100%)
- **Headline:** "Personalise your book cover"
- **Label:** "Choose cover colour"
- **Color options (aria-labels):** "blue", "black", "green", "pink", "red", "white"
- **Label:** "Put your name on the book"
- **Input placeholder:** "Enter your name"
- **CTA:** "Continue"

## Step 9 — Long-form paywall (paywall_offer / kind: paywall)
- **Headline:** "Well done, your Perfect / Prayer is almost ready!"
- **Cover name overlay:** "for MARI"
- **CTA (top):** "Get your book"

### Sneak peek card
- **Heading:** "Here's a sneak peek what's in your / book:"
- **Body:** "We analyzed your responses and have put together the Perfect Prayer book just for you!"
- **Stats:**
  - "300+ Pages of tailored content for you"
  - "1200+ Prayers based on your preferences"
  - "140+ Selection of Bible, Scriptures readings"
  - "97% Personalisation score"

### Daily practice length card
- **Heading:** "Length of a daily practices"
- **Body:** "To better accommodate your schedule, we have selected content that is"
- **Detail:** "Medium Length", "5 - 15 minutes"

- **CTA (middle):** "Get your book"

### Mood chart card
- **Heading:** "Your mood in 3 months:"
- **Chart labels:** "Today", "Happy", "May", "Peaceful"

### Stats card
- "39% Experienced the same triggers for stress and anxiety as you"
- "68% Felt that they could cope with anxiety much better"
- "83% Reported improvement in a sense of joy & happiness"
- "91% Said they feel connected to God better than ever before"

- **CTA (bottom):** "Get your book"

### Scripture verse
- "2 Kings 20_5 (NKJV)"
- "\"I have heard your prayer, I have seen your tears; surely I will heal you.\""

### Testimonial / quote section
- **Heading:** "The new God squad"
- **Quote:** "I've come across the Perfect Prayer book, and I can't tell you how much it's been a blessing. It's like a friend that's always there to strengthen your faith and bring you peace. I wholeheartedly encourage you to discover this book for yourself; it's a beautiful way to grow closer to God and find the inner peace we all seek."
- **Author:** "- Fr. Peter Flant"

---
_Note: Funnel sequence runs step-1 → step-9 (progress labels reference 17 total internal questions, but only these 9 step files exist). No separate subscription-started / upsell / cancellation step files; step-9 paywall is the terminal flow step. A generic `manage-subscription` account page exists outside the funnel sequence._

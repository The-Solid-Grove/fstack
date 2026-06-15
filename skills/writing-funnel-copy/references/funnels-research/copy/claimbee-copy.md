# ClaimBee — Copy Swipe (verbatim from source)
> Source: rag-catalog/claimbee-funnel. Copy lives in `src/steps/content/*.content.ts` (step .tsx files re-render these). Step order from `src/config/funnel.manifest.ts`.

## claim (step-01) — Landing / hook headline
- **Headline:** "People getting" / "free money" / "know one secret"

## claim-b (step-01b) — Landing variant (same copy, alt layout)
- **Headline:** "People getting" / "free money" / "know one secret"

## profile (step-02) — Hook headline 2
- **Headline:** "They" / "take it back" / "from big corporations"

## activate (step-03) — Brand intro
- **Headline:** "ClaimBee" / "helps you claim" / "what is yours"

## eligibility (step-04) — Yes/No question (Android)
- **Headline:** "Have you owned" / "or used any" / "Android devices" / "with cellular data?"
- **Options:** "✅ Yes", "❌ No"

## active-google-claim (step-04b) — Interstitial (Google settlement)
- **Body:** "Right now," / "Android users" / "can file claims for the"
- **Pill:** "active Google privacy settlement"
- **Note label:** "Good to know:"
- **Note:** "Eligible users may receive"
- **Amount:** "up to $100 per user"
- **Status/loader:** "Checking active claim status..."

## devices-selected (step-05) — Multi-select devices
- **Headline:** "Which of these devices have you used?"
- **Subhead:** "Select all that apply. This helps us calculate your potential device-specific compensation"
- **Options:** "iPhone", "Apple Watch", "iPad", "MacBook", "None of the above"

## settlement (step-07) — Interstitial (batterygate)
- **Body:** "In early 2024," / "iPhone owners" / "began receiving checks for the"
- **Pill:** "\"batterygate\" settlement"
- **Note label:** "Good to know:"
- **Note:** "The average compensation was"
- **Amount:** "$92 per device"
- **Status/loader:** "Connecting to FTC Registry..."

## subscriptions (step-08) — Value prop (Google settlement)
- **Tag:** "Google settlement"
- **Title:** "Your Android data may qualify"
- **Highlight:** "Google privacy settlement is active"
- **Body:** "for Android users with cellular data" / "Google set aside $135M for refunds" / "Let's check what else may be waiting for you"

## prime-question (step-09) — Yes/No question (Amazon Prime)
- **Tag:** "Subscriptions"
- **Body:** "Did you have" / "an active" / "Amazon" / "Prime subscription" / "at any point between" / "2019 and 2025?"
- **Options:** "✅ Yes", "❌ No"

## digital-rights (step-10) — Value prop (Amazon FTC)
- **Tag:** "Subscriptions"
- **Title:** "Your digital rights matter"
- **Body:** "The FTC ordered Amazon to pay out a record"
- **Pill:** "$2.5 billion"
- **Why label:** "Why?"
- **Body:** "Because they used confusing interface designs known as \"dark patterns\" to sign people up without clear consent."

## never-miss (step-11) — Social proof / testimonial
- **Title:** "Never miss a payout you're owed"
- **Body:** "Our system tracks verified legal sources 24/7 to find payouts you didn’t know existed"
- **Testimonial:** "ClaimBee told me about money I was owed even though my friends and social feeds never mentioned it." — George P. (5 stars)

## delivery-apps (step-12) — Yes/No question (delivery apps)
- **Tag:** "Subscriptions"
- **Headline:** "Did you use delivery apps like UberEats, DoorDash, or GrubHub during 2025?"
- **Options:** "✅ Yes", "❌ No"

## active-cases (step-13) — Value prop (hidden fees)
- **Tag:** "Subscriptions"
- **Headline:** "We are tracking active cases regarding hidden fees"
- **Body:** "Many of these services are currently facing lawsuits regarding non-transparent service fees charged to customers during that period"

## claims-progress (step-14) — Interstitial
- **Headline:** "See claims others miss"
- **Body:** "ClaimBee monitor trusted legal sources to catch hidden settlements and alert you the moment you qualify"
- **Status/loader:** "Verifying claim deadlines..."

## digital-safety-intro (step-15) — Section intro (Privacy)
- **Tag:** "Privacy & Security"
- **Headline:** "Now, let’s talk about your digital safety"
- **Body:** "The largest compensation funds in recent years aren’t from social media, but from"
- **Pill:** "the companies you trusted with your personal data"

## facebook-question (step-16) — Yes/No question (Facebook)
- **Tag:** "Privacy & Security"
- **Headline:** "Did you have an active Facebook account between 2007 and 2024?"
- **Options:** "✅ Yes", "❌ No"

## facebook-breach (step-17) — Interstitial (Facebook/Cambridge Analytica)
- **Tag:** "Privacy & Security"
- **Headline:** "This period 2007-2024 covers a massive data breach at"
- **Pill:** "Facebook & Cambridge Analytica"
- **Note label:** "Good to know:"
- **Body:** "The settlement reached was"
- **Amount:** "$725 million"

## google-question (step-18) — Yes/No question (Google Maps/Search)
- **Tag:** "Privacy & Security"
- **Headline:** "Do you use Google Maps or Google Search on your smartphone?"
- **Options:** "✅ Yes", "❌ No"

## privacy-right (step-19) — Value prop (Google location verdict)
- **Tag:** "Privacy & Security"
- **Headline:** "Privacy is a right, not a setting"
- **Body lead:** "Google faced a"
- **Pill:** "$425 million verdict"
- **Body:** "for tracking location data even when users explicitly turned \"Location History\" off"

## data-breach-question (step-20) — Yes/No question (data breach email)
- **Tag:** "Privacy & Security"
- **Headline:** "Have you ever received an email with the subject line Notice of Data Breach?"
- **Options:** "✅ Yes", "❌ No"

## spam-explainer (step-21) — Explainer
- **Tag:** "Privacy & Security"
- **Pill:** "We get it - it looks like spam"
- **Body:** "But that email is effectively a check waiting to be cashed, often ranging"
- **Amount:** "$50 to $500"
- **Body:** "We help you turn those \"junk\" emails into cash."

## be-first-progress (step-22) — Interstitial / value prop
- **Headline:** "Be the First to Know and File"
- **Pill:** "Speed is your biggest advantage"
- **Body 1:** "Because we automate the search, we tell you about new money settlements days early, leaving you with zero risk of missing the date"
- **Body 2:** "News sites are often 2 weeks late. We find settlements before they hit the headlines"
- **Status/loader:** "Verifying claim deadlines..."

## nyt-question (step-23) — Question (NYT referral)
- **Headline:** "Did a The New York Times article bring you here?"

## payout-calculating (step-24) — Loader frames
- **Caption:** "Calculating your potential payout..."
- **Frame messages:** "Analyzing device history...", "Scanning data breach records (2018-2025)...", "Matching profile with open Class Action lawsuits...", "Identifying antitrust settlement eligibility...", "Filtering out expired claims...", "Cross-referencing FTC settlement registry...", "Structuring claim groups...", "Finalizing potential payout estimate..."

## great-news (step-25) — Results reveal
- **Headline:** "Great news!"
- **Body:** "Based on your answers, you are pre-qualified for 7 active class action lawsuits"
- **Payout label:** "Your Potential Payout:"
- **Axis end label:** "After 2 Weeks"
- **Footnote:** "*The final amount depends on verifying your usage"

## filing-simple (step-26) — Value prop
- **Headline:** "Filing claims can be complex. We make it simple!"
- **Body:** "ClaimBee replaces clunky government forms with a smart, step-by-step experience. We strip away the confusing legal jargon so you can finish quickly"

## journey-choice (step-27) — Path choice
- **Headline:** "This is your journey"
- **Subhead:** "Which pace would you prefer?"
- **Options:**
  - "ClaimBee" — "Auto-file all eligible claims in one click" (badge: "Recommended")
  - "By Myself" — "You will find court websites, download forms and mail them by yourself"

## by-myself-warning (step-28) — Friction / warning
- **Headline:** "Are you sure?"
- **Lead:** "Self-filing typically takes about"
- **Pill:** "14 hours of work"
- **Body 1:** "You will need to locate court dockets, navigate legal terminology, and monitor deadlines individually"
- **Body 2:** "Or, let us handle the heavy lifting. We can automatically file for all 7 lawsuits with a single digital signature"

## relationship-status (step-29) — Choice
- **Headline:** "One last thing to maximize your household’s return"
- **Subhead:** "What is your current relationship status?"
- **Options:** "💍 Married / Partnered", "⚖️ Divorced", "👤 Single"

## family-claims (step-30) — Value prop
- **Pill:** "Get every dollar your family is owed"
- **Body:** "Track claims for every person in your house in one list. This ensures no money gets left behind"

## email-capture (step-31) — Email capture
- **Headline:** "Enter the email address for your official claims"
- **Subhead:** "Please double-check the spelling. This is the address where you will receive important case updates and payout notifications"
- **Placeholder:** "Email address"
- **CTA:** "Next" (submitting: "Saving...")
- **Error:** "Unable to save email"

## scratch-card (step-31b) — Discount scratch card
- **Title:** "Scratch & unlock a surprise discount on your plan!"
- **Subhead:** "Just our way of saying we appreciate you!"
- **Instruction:** "Scratch your discount"
- **Aria:** "Scratch the ticket to reveal your discount, or wait for the automatic reveal"
- **Modal title:** "Woo hoo!"
- **Modal body:** "You won a discount"
- **Applied label:** "This discount will be applied automatically"
- **CTA:** "CONTINUE"

## paywall (step-32) — Paywall offer

### Top bar / loading
- **Loading:** "Loading..."
- **Top bar:** "⏰ Discount Expires in" / CTA "GET MY PLAN"
- **Countdown units:** "minutes", "seconds"

### Hero
- **Pills:** "Find hidden money and", "claim what's yours"
- **Image alt:** "ClaimBee family illustration"

### Promo
- **Initial label:** "% Your promo code applied!"
- **Upgraded label:** "New promo code applied!"

### Highlight
- **Title:** "Get money you didn’t know about"
- **Body:** "Discover settlement payouts you’re owed from past purchases, ClaimBee finds them for you."

### Plans
- **Title:** "Choose your plan"
- **Card CTA:** "GET MY PLAN"
- **Meta labels:** "Money-back guarantee", "Cancel anytime"
- **Stripe note:** "Stripe publishable key is not available in this app runtime. Update the project payment environment variables or make sure your SDK publishable key maps to a funnel with Stripe settings."

### Checkout
- **Title:** "Checkout"
- **Summary title:** "Order summary"
- **Wallet placeholders:** "Subscribe with Apple Pay", "Subscribe with Google Pay"
- **Wallet button:** "Apple Pay"
- **Email label:** "Email" / placeholder "Enter your email"
- **Email invalid:** "Enter a valid email address to continue."
- **Countdown:** "Discount expires in"
- **Satisfaction:** "91%" — "of users are satisfied with the plan and stay with us after its completion"
- **Price labels:** "Regular Price", "{percent}% OFF", "Your {percent}% Discount"
- **Promo code label:** "Applied promo code:"
- **Saved label:** "You just saved {amount} ({percent}% OFF)"
- **Total label:** "Total"
- **Guarantee label:** "30 days moneyback guarantee. Cancel anytime."
- **Submit:** "CONTINUE" / card submit "Confirm payment" / processing "PROCESSING..."
- **PayPal:** "PayPal" / "PayPal Buy Now"
- **Secure:** "Pay safe & secure" / "Powered by Stripe"
- **Payment methods:** "Visa", "Mastercard", "Maestro", "Discover"
- **Legal prefix:** "By proceeding you agree to our" — links: "Terms of Service", "Privacy Policy", "Subscription Policy"
- **Support:** "Need help? Contact us at"
- **Renewal:** "You'll be charged {amount} today for your selected plan. Your subscription renews automatically unless cancelled at least 24 hours before renewal date."

### Special offer (downsell)
- **Discount label:** "-46%"
- **Title:** "Special Offer"
- **Body:** "We want you to feel loved and happy so we are offering you a discount to try our proven learning program"
- **CTA:** "GET DISCOUNT"

### Feature grid
- **Title:** "Find, track, and claim in one place"
- **Subtitle:** "One app shows all your options and helps you complete real claims for real payouts"
- **AI assistant:** "AI claim assistant" — "It reviews your info, finds matches, and shows you what to do next"
- **Quick features:** "Get instant eligibility checks", "See how much you could claim", "100+ new settlements found every month", "Unlimited claim checks"
- **History:** "Claim for your own past buys, bills, or services"
- **Detailed features:**
  - "Clear progress and tracking" — "See which claims you started, submitted, and are waiting to be paid."
  - "Personalized Money Alerts" — "Instant alerts when we find a new settlement you could qualify for."

### Stories from our users
- **Title:** "Stories from our users"
- "I realized ClaimBee saves me more money than it costs - this pays for itself" — Elizabeth L.
- "These are settlements I never saw anywhere online - I would’ve missed all of this." — Tom J.
- "It just told me instantly whether I’m eligible - no reading the legal stuff myself." — Maria G.
- "All I did was confirm and click - it handled the rest." — Alex M.
- "ClaimBee told me about money I was owed even though my friends and social feeds never mentioned it." — Peter P.
- "Even if I unsubscribe, I feel like I got my money’s worth with just one claim." — Michael M.

### FAQ
- **Title:** "More things you might want to know"
- **Q:** "Do you only cover the big, famous lawsuits, or do you track smaller ones too?"
  **A:** "We track it all. From massive data breaches to niche product recalls and local class actions, our database is comprehensive. Our goal is your complete financial security regarding owed compensation, so if there is an eligible settlement active in your region, we aim to have it in the app, regardless of how \"famous\" the case is."
- **Q:** "What if there’s a settlement for an item I bought years ago and I don’t have the receipt?"
  **A:** "Don’t worry, this is very common. Many settlements do not require proof of purchase for smaller claim amounts. Furthermore, ClaimBee can help you search your connected digital history for records you might have forgotten existed, helping you \"restore\" a claim you might have otherwise abandoned."
- **Q:** "This sounds too good to be true. Is this a scam or a \"free money\" scheme?"
  **A:** "Not at all. We aren’t generating \"free money\"; we are simply helping you claim money that is already yours legally. Settlements are court-ordered compensations for wrongdoings. ClaimBee is just a tool that organizes this fragmented legal data to make the process accessible, transparent, and manageable for you."
- **Q:** "If I file through an app, is my claim less likely to be approved than if I filed on the official website?"
  **A:** "No. When you submit through ClaimBee, we generate the exact information and forms required by the settlement administrator. The legal validity is the same; we just make the experience of filling it out much faster and less prone to errors than the manual method."
- **Q:** "Are there hidden fees? Will you take a cut of my small settlement?"
  **A:** "We believe in total transparency. We do not take a surprise commission from your settlement checks. Our business model is upfront (e.g., subscription or freemium features), ensuring that the money you claim stays in your pocket."

### Guarantee
- **Title:** "Money-Back guarantee"
- **Body:** "We’re confident in our service and results. If you’re not satisfied, let us know within 30 days of purchase for a full refund. You must demonstrate that you followed the program. See our" — link "refund policy"
- **Badge alt:** "30 day money back guarantee badge"

## subscription-started (step-33) — Subscription handoff / great news
- **Kicker:** "Congratulations!"
- **Title:** "Your subscription has started."
- **Copy (with QR):** "Scan with your phone to install or open the app and continue inside mobile."
- **Copy (without QR):** "Open the app on your phone to continue inside mobile."
- **Note:** "In case the app asks you to subscribe again, open the same deep link one more time."
- **CTAs:** "Open app now", "Send link to email"
- **Store links:** "Download on the / App Store", "Get it on / Google Play", "Continue on / Web"
- **Email subject:** "Your ClaimBee app link"
- **Email intro:** "Your subscription is active."
- **Email labels:** "Open app", "iPhone deep link", "Android deep link", "App Store", "Google Play"
- **Statuses:** "Email draft opened in your mail app.", "Attempted to open your app automatically."
- **QR open label:** "Open app handoff link"

## manage-subscription (step-35) — Subscription management / cancellation

### Subscriptions stage
- **Title:** "Manage your subscriptions"
- **Loading:** "Loading your subscription..."
- **Empty:** "We could not find any subscriptions for your account."
- **Support prefix:** "Need help? Contact us at"
- **CTA:** "Continue"
- **Row labels:** "Selected", "Select", "subscription", "Renews on", "Ending", "Unavailable"

### Why-cancel stage
- **Title:** "Please tell us why you would like to cancel subscription"
- **Back:** "Back"
- **Reasons:** "💰 It's too expensive", "📱 I don't use the app enough", "🙁 I couldn't figure out how to use it", "😐 I didn't get value from the app", "📦 I found a better alternative", "🛠️ I had technical issues", "⏳ Just taking a break for now", "✍️ Other"

### Confirm stage
- **Title:** "Cancel your subscription"
- **Labels:** "Reason:", "Selected plan:", "No active subscription selected."
- **CTA:** "Cancel subscription" (cancelling: "Cancelling...") / "Back"

### Done stage
- **Title:** "Subscription canceled!"
- **Body:** "Your subscription has been canceled."
- **Empty:** "We could not find a cancellable subscription for your account."
- **CTA:** "Go back to subscriptions list"

### Support / errors
- **Support link:** "support@example.com"
- **Errors:** "Failed to load subscriptions", "Failed to cancel subscription"

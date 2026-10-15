## F. The look

### F1. Direction

**One idea: a well-set exam paper.** Calm, serious, warm.

- **The layout bones** come from your template `site-templates/templates/03-lab-dossier`:
  - a warm paper background;
  - big headlines set to the left;
  - small letter-spaced labels above sections;
  - square black main buttons;
  - hairline rules between sections;
  - lots of white space.
- **Fonts:** Latin Modern replaces the template's grotesk headlines, so the site matches the deck and every PDF.
- **Never:**
  - mascots, cartoons or confetti;
  - gradients or glass effects;
  - stock photos of smiling teenagers;
  - streaks, badges or leaderboards;
  - countdown timers or "3 spots left".

**Process, because earlier visual designs were rejected:**
1. Test the wireframes.
2. Style one screen, Home, and get your sign-off.
3. Only then style the rest.

### F2. Fonts

| Use | Font | Licence | Notes |
|---|---|---|---|
| Headlines, course notes, long reading | Latin Modern Roman (LM Roman 10 and 12 for text, LM Roman 17 for display) | GUST Font License | Convert the MiKTeX OTFs to WOFF2 and host them ourselves |
| Buttons, forms, tables, prices, numbers | Inter, with tabular figures | SIL Open Font License | Has the ₹ sign |
| Small labels, receipts, help logs | Latin Modern Mono (LM Mono 10) | GUST Font License | The typed-record feel |

**Latin Modern has no ₹ sign** (checked 13 October). Every price is wrapped as `<span class="money">` in Inter, and Inter sits next in the font list so a stray ₹ still shows.

Satoshi and Cabinet Grotesk are not used: their Indian Type Foundry licences are marked "check" in the font audit.

### F3. Colour

| Token | Light | Dark | Used for |
|---|---|---|---|
| `--paper` | #f6f4ee | #0f0f0e | page background |
| `--surface` | #fffffe | #1a1a19 | cards |
| `--wash` | #efede6 | #232321 | quiet panels |
| `--ink` | #121211 | #f4f2ec | text |
| `--ink-2` | #4a4945 | #c3c2b7 | secondary text |
| `--muted` | #7a7873 | #8f8d86 | labels, hints |
| `--rule` | #dcdad2 | #2f2f2c | hairlines, borders |
| `--blue` | #2a78d6 | #5b9be8 | the one accent: links, the app's main action, the verified tick |
| `--blue-wash` | #e9f1fb | #16263a | selected rows, the chosen door |
| `--red` | #b42a2a | #e06a6a | Report, safety notices, destructive actions only |
| `--green` | #1f7a3a | #4fb06a | a "done" tick only |

Dark mode is designed, not inverted. It follows the device setting, and a switch can override it.

Check text contrast at WCAG AA in both themes before anything ships.

### F4. Type, spacing and grid

- **Type sizes:**
  - 13 (labels), 15 (interface), 17 (body);
  - 20, 26, 34, 48 and 72 (display).
  - Line height: 1.55 for body text and 1.1 for headlines.
- **Spacing steps:** 4, 8, 12, 16, 24, 32, 48, 72, 112.
- **Corners:**
  - cards 10px;
  - inputs 8px;
  - main buttons square (0px), like the template.
- **Grid:**
  - 12 columns from 900px up, at most 1180px wide;
  - 4 columns on phones, with a 16px gutter at the sides.
- **Breakpoints:** 360 (smallest phone), 600, 900, 1200.
- **No sideways scrolling** on any page. Wide tables scroll inside their own box.

### F5. Components

Design each once, with every state:

| Component | States |
|---|---|
| Button: main (ink, square), secondary (outline), quiet (text), danger (red text) | normal, hover, focus, pressed, disabled with the reason shown, loading |
| Text field, select, date, search with suggestions | empty, filled, focus, error with the message under it, disabled |
| Chips (subjects), HL/SL switch, radio cards (doors, tracks) | off, on, focus, disabled |
| Step line ("Step 2 of 4") | - |
| Verified badge: blue tick + "Economics HL 7" | tap shows "We checked the official IB results document on 18 Dec 2026" |
| Track label: "IB graduate 2026", "Graduate tutor, 17", "IB teacher" | - |
| Receipt (LM Mono, right-aligned figures) | lesson, coaching, course, Marker |
| Tutor card, course card, request card | normal, hover, unavailable |
| Approval card | waiting, approved, declined, expired |
| Lesson card | upcoming, join open, in progress, finished, cancelled |
| Help log | to file (countdown), filed, with a correction note |
| Marker criterion row | sure, fairly sure, unsure (with a range) |
| Checklist row | to do, waiting for us, needs a fix, done |
| "Your parent can see this" banner | on every chat |
| Report button and report sheet | normal, sending, sent |
| Banner | info (blue), waiting (muted), safety (red) |
| Empty state: one sentence and one button | - |
| Modal sheet (phone) and dialog (desktop) | - |
| Bottom tab bar (phone) | with a count badge on Approvals |
| Week grid of free times | free, booked, outside allowed hours |

**Icons:** Lucide (ISC licence), with a 1.5px line, and only where a word alone is slower (join, report, settings). Every icon has a text label or an accessible name.

**Pictures:**
- tutors' own profile photos only, and optional;
- no photos of students, ever;
- no illustrations.

**Motion:** fades and slides of 150 to 200 ms, nothing that bounces, and none at all for users who switch motion off.

### F6. Access for everyone

- **Standard:** WCAG 2.2 AA.
- **Keyboard:** every action works by keyboard, with a visible focus ring, and a skip link on every page.
- **Forms:** every field has a label; placeholders never stand in for one. Errors say what to do, next to the field, and are announced.
- **Size:** touch targets of at least 44px; works at 200% zoom.
- **Captions:** every course video has captions, and the lesson room offers live captions where the video service supports them.
- **Testing:** with NVDA on Windows and TalkBack on Android before each release.

### F7. Formats

- **Money:** ₹ with Indian grouping (₹1,49,900). Paise only on receipts (₹58.49). Elsewhere round to the rupee.
- **Dates:** "Tue 9 Mar", with the year only when it isn't this year.
- **Times:** "5:00 pm IST". The viewer's own zone comes first if it isn't IST: "7:30 pm GST (9:00 pm IST)".
- **Names:**
  - students are always first names only to tutors;
  - tutors are first name and initial in public, and full name after a booking.

## G. The words

### G1. Voice

A sharp, kind IB student talking to another student, and to their parent:
- short sentences;
- specific words;
- British spelling;
- no em dashes.

| Say | Don't say |
|---|---|
| "Criterion B is where most 4s become 5s." | "Unlock your potential." |
| "Nobody pays to rank higher." | "Our proprietary matching algorithm." |
| "Not for you if you already score 6s." | "Perfect for everyone!" |
| "Your parent can see this chat." | "This conversation may be monitored." |
| "We don't know yet; we'll publish it." | "Industry-leading accuracy." |

Never use: revolutionise, seamless, unlock, empower, journey, game-changer, cutting-edge, supercharge, elevate, guaranteed.

Always say "the IB" or "IB Diploma students". Never put "IB" in the FortyFive name or logo.

### G2. Words for key moments

| Moment | Words |
|---|---|
| Waiting for a parent | "Sent to Priya. You can use the free tools and previews while you wait." |
| Booking sent for approval | "Sent to Priya for approval. We hold this slot for 12 hours." |
| Parent declined a booking | "Priya didn't approve this one. Talk to her, or pick another time." |
| Payment failed | "The payment didn't go through. Nothing was charged. Try again or use UPI." |
| Contact details hidden | "[contact details hidden: keep chats on FortyFive]" |
| Slot outside allowed hours | "Lessons for under-18s run 7 am to 9 pm." |
| Coaching limit reached | "You've used all 4 coaching hours for this IA. That's the limit, so the work stays yours. Your supervisor is the next step." |
| Marker subject not open | "We open a subject once its accuracy is published. Economics opens when 30 marked pieces are in." |
| Second Marker check too soon | "Your second check opens on 21 March, a week after the first." |
| Report sent | "Thanks. A trained adult will read this within 24 hours. If someone is in danger now, call 112." |
| Empty Today | "Nothing booked yet. Watch a free first lesson, or find a tutor for one paper." |
| Tutor not live yet | "Your profile goes live when every step is done. Most people take a week." |
| Needs a fix | "The name on your results document doesn't match your ID. Upload it again, or write to us." |
| No search results | "No tutor matches all of that. Try fewer filters, or post a request." |
| Error, something broke | "Something went wrong on our side. Nothing was lost. Try again in a minute." |

### G3. What has to be written before launch

**Legal (with the lawyer):**
- terms of use;
- privacy notice;
- parental consent notice;
- refund policy;
- tutor agreement;
- coursework code;
- safeguarding policy;
- sponsor rules.

**Pages:**
- the ten promises;
- For parents;
- Coursework;
- Teach on FortyFive;
- For schools;
- About;
- the questions on each page.

**Training:**
- the safeguarding course (30 minutes, 10-question quiz);
- the coursework integrity course (60 minutes, quiz);
- the demo lesson checklist for subject leads.

**Emails, about 25:**
- the parent invite and reminders;
- approved;
- every booking state;
- lesson reminders;
- receipts and refunds;
- the review prompt;
- help log ready;
- Marker report ready;
- each tutor checklist step;
- profile live;
- payout sent;
- report received;
- data request done.

**SMS templates**, registered on DLT before any SMS can be sent in India:
- the one-time code;
- approval needed;
- the safety alert to the safeguarding lead.

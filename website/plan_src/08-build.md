## H. Building it

### H1. What each part runs on

| Need | Choice | Notes |
|---|---|---|
| Public site and app | Next.js on Cloudflare Workers | Same set-up as the Kalpya build; pages rendered on the server |
| Accounts, data, access rules | Supabase: sign-in, Postgres, row-level security | The table in A4 becomes database rules, so a wrong URL can't show someone else's data |
| Chat | Supabase Realtime, plus a server check for contact details | Catches numbers (also written in words), emails, handles, UPI IDs, links |
| Files | A private bucket (Supabase Storage or Cloudflare R2) | Marker uploads go in a bucket that deletes after 48 hours |
| Course video | Cloudflare Stream, with links that expire | Captions on every video |
| Lesson room and recording | Jitsi: hosted (8x8 JaaS) or self-hosted with Jibri | Decide on cost in November. Recordings go to a private bucket |
| Payments (v1) | Razorpay Route | Linked accounts for tutors and guardians; money held until payout |
| ID and adult check | DigiLocker through a licensed provider | Parents and tutors |
| Background checks | An Indian check provider | Tutors 18 and over |
| E-signatures | Aadhaar e-sign through the same provider, or click-to-accept | The lawyer decides |
| Email | A transactional email service | From a fortyfive.study address |
| SMS | An Indian SMS provider | Needs DLT registration of the business and every template first |
| The Marker | Claude API (Opus 5.5) with prompt caching | Practice marking in v1, coursework checks in v2. Three passes, then a checker that blocks rewritten text |
| Analytics | Cloudflare Web Analytics | Public pages only, no cookies |
| Errors | An error tracker that strips personal data | - |
| Staff console | The same app on admin.fortyfive.study | Two-factor sign-in; every opening logged |

**Main tables:**
- **People:** accounts, roles, parent links, consents.
- **Schools and subjects:** schools (the 629), subjects, student subjects.
- **Tutors:** tutor subjects (with the verified grade), checklist items, free times.
- **Bookings:** bookings (with their state), lesson rooms, recordings.
- **Messages and the board:** threads, messages, requests, replies, reviews.
- **Courses:** courses, modules, lessons, enrolments, free places, checklist ticks.
- **Coursework:** pieces, help logs, Marker checks, Marker reports.
- **Money:** payments, refunds, payouts.
- **Safety and running:** reports, the audit log, notifications.

### H2. What ships when

**v0, the pilot (1 February 2027).** No payments go through FortyFive; parents pay founding tutors directly by UPI. About 30 screens:

| Area | Screens |
|---|---|
| Public | C1 Home, C2 Catalogue (2 courses), C3 Course page, C4 Tutor search, C5 Tutor profile, C6 Coursework (says coaching opens in April), C7 Predictor, Next point and Results-day guide, C8 Promises and Fees, C9 For parents and Report, C11 Teach, C12 Sign in |
| Sign-ups | B1 to B5 |
| Student | C13 Today, C14 Course player, C15 Booking, C17 Bookings, C18 Lesson room, C22 Messages, C23 Account |
| Parent | C24 Home, C25 Approvals (UPI directly, with "I've paid"), C26 Bookings, Messages, Settings |
| Tutor | Checklist, C27 Home, C29 Calendar, C30 Students, C33 Profile, C34 Training, C36 Guardian view |
| Staff | C37 Verify, C38 Safeguarding, C42 People (basic) |

**v1, the launch (April 2027):**
- **Money:** Razorpay payments, receipts and refunds (C25, C26 Payments, C32 Earnings, C41 Payments); course sales and free places.
- **Matching:** the request board (C16, C28); reviews (D7); small-group clinics.
- **Coursework:** coaching (C19 coaching, C31 Help log, C39 Integrity reviews); practice marking in C14; the timetable and coursework planner tools.
- **Trust and content:** open books (C8, C44); corrections (C40); course authoring (C35); C10 For schools.

**v2 (from August 2027):**
- Marker coursework checks (C20, C21, C43 and the accuracy page), subject by subject.
- School console and teacher mode (C45).
- The exemplar library.
- Standing approvals for one tutor.
- An installable phone version of the site.

### H3. Order of work for v0

Nothing starts before 13 November. The weeks below are rough; the 16 December line isn't, because founding tutors sign up right after results.

| Weeks | Work |
|---|---|
| 14 to 22 Nov | **First round of wireframe tests (H4).** Settle the open questions in Part I with the lawyer. Set up the code, hosting, database, sign-in, roles, access rules, fonts and colours, and the public page frame. |
| 23 to 29 Nov | **Style Home for your sign-off.** Then the content pages: C1, C8, C9, C11. |
| 30 Nov to 6 Dec | **Sign-ups B1 to B4 and parent approval,** with DigiLocker in test mode, plus limited mode. |
| 7 to 16 Dec | **Tutor sign-up B5 and the checklist,** C37 Verify, C34 safeguarding course and quiz. **Ready by results day.** |
| 17 to 23 Dec | Tutor profile C33 and C5, search C4, calendar C29. |
| 24 to 31 Dec | Booking C15, approvals C25 (UPI), bookings C17, booking emails. |
| 1 to 10 Jan | Messages C22 with contact hiding; reports D11 and the safeguarding inbox C38. |
| 11 to 20 Jan | Lesson room C18 with recording; Today C13; parent home C24. |
| 21 to 31 Jan | **Second round of tests:** course player C14 with both courses loaded, accessibility and safety checks (H4), then fixes. |
| 1 Feb | The pilot opens. |

### H4. Testing

**1. Wireframe tests (late November) and build tests (late January).**
- **Who:** 5 DP students, 5 parents and 3 tutors, 20 minutes each, using their own phones where possible.
- **Student tasks:**
  - sign up and reach "waiting for your parent";
  - find an Economics HL tutor free on a Tuesday evening and send a booking;
  - find how many coaching hours you have left.
- **Parent tasks:**
  - approve the account;
  - approve a booking;
  - find a message your child sent;
  - report a concern.
- **Tutor tasks:**
  - sign up and say what's left before you go live;
  - reply to a request;
  - file a help log.
- **Pass mark:** 4 of 5 people finish each task without help. Anything below that gets changed and tested again.

**2. Safety checks, before every release.** Every one of these must fail:
- sharing a phone number in chat six ways (digits, spaced out, in words, mixed, as a handle, as a UPI ID);
- booking an under-18 at 9:30 pm;
- messaging or booking before the parent approves;
- a tutor opening another student's booking by changing the URL;
- a student opening someone else's Marker report by URL;
- staff opening a recording without giving a reason;
- uploading a .docx or a 50 MB file to the Marker;
- a coach filing a log for a session they didn't teach;
- a review on a lesson that never happened.

**3. Access for everyone.**
- keyboard only, through the sign-up, approval, booking and messaging flows (B2, B3, C15, C25, C22);
- NVDA and TalkBack;
- contrast in both themes;
- 200% zoom;
- a 360px phone.

### H5. Before the pilot opens

1. The lawyer has signed off every legal page and the consent method.
2. The safeguarding lead is trained, has the inbox on their phone, and has a test child-safety report sent at 11 pm and handled.
3. DLT registration and SMS templates are approved.
4. DigiLocker and the check provider are on live keys.
5. Backups are restored once, for real, to prove they work.
6. Every founding tutor is fully green on the checklist.
7. Both courses have been checked by their leads and have captions.
8. The DP Coordinator has agreed to the pilot in writing.

## I. Questions still open

| # | Question | Who decides | By |
|---|---|---|---|
| 1 | How a parent proves they're an adult for consent (DigiLocker, or another method the DPDP Rules accept) | the lawyer | 30 Nov 2026 |
| 2 | Who may watch recordings, and how long each kind is kept | the lawyer and the safeguarding lead | 30 Nov 2026 |
| 3 | Hosted or self-hosted Jitsi for recorded lessons | you, on cost | 22 Nov 2026 |
| 4 | Tutors never see the student's school: keep that? | you (recommended: keep) | 22 Nov 2026 |
| 5 | Graduate tutors aged 17 and coursework coaching | you (recommended: not until 18) | 22 Nov 2026 |
| 6 | Group clinics: each student's parent approves and pays separately? | you (recommended: yes) | before v1 |
| 7 | Standing approval for one tutor | after the pilot, from parents' feedback | April 2027 |
| 8 | A phone app | not before v2; the site is built for phones first | 2027 |
| 9 | Other languages (Hindi first) | not in v1 | 2027 |
| 10 | What the Marker costs per check, for real | measure in v1 with practice marking | June 2027 |

# FortyFive website plan

**Version 1, 13 October 2026.** The whole website and app, planned end to end: who uses it, every screen, every flow, the look, the words, the build order and the tests. It replaces the Fable brief (moved to `_old`).

**How to read it.**
- **Part A:** the shape of the site.
- **Part B:** the sign-ups.
- **Part C:** every screen, with wireframes for the important ones.
- **Part D:** the flows that run across screens.
- **Part E:** notifications.
- **Part F:** the look.
- **Part G:** the words.
- **Part H:** how and when it gets built and tested.
- **Part I:** the questions still open.

**How to use the wireframes.**
- They show what goes where and in what order, not the final look.
- "Rs" stands for the rupee sign so the boxes line up; the real site uses ₹.
- Test the wireframes with students, parents and tutors first. Then style one screen (Home) for your sign-off before styling the rest.

**Status, 13 October 2026: built.**
- **Where:** every screen in this plan is built in `Downloads\fortyfive-site` (Next.js 16), working on demo data. Run `npm run dev` there and open localhost:4545.
- **How it differs from the plan:**
  - Course pages live at `/courses/[course]` rather than `/courses/[subject]/[course]`.
  - The demo world is set on 13 September 2027, so payments, coaching and the Marker can all be shown working.
  - The brand is FortyFive at joinfortyfive.com (recommended, not yet registered).
- **Still to do:** the build order in Part H still applies to the real v0. It now means replacing the demo data with Supabase, rather than building screens.

## A. The shape of the site

### A1. What it must do

Three jobs, in this order:

1. **Keep under-18s safe and parents in control.** Every other feature gives way to this one.
2. **Get a student from "I'm stuck" to the right help in under five minutes.** That help can be a course lesson, a tutor or a coach.
3. **Get a good tutor from sign-up to a live profile in under ten days.**

What it must never do:
- sell more than the student needs;
- track how students behave;
- let anyone write anyone's coursework;
- show anything that looks like an IB paper.

### A2. How we'll know it works

Everything here is counted from records the site keeps anyway: bookings, approvals, logs. Nothing comes from tracking clicks.

| Measure | Target by October 2027 |
|---|---|
| Time for a parent to approve a booking (median) | under 6 hours |
| Student sign-up to first lesson or course (median) | under 2 days |
| Tutor sign-up to live profile (median) | under 10 days |
| Reports read by the safeguarding lead within 24 hours | 100% |
| Coaching sessions with a help log filed within 24 hours | 100% |
| Students who tick off 75% or more of a course checklist | 40% |

Analytics run only on public pages, without cookies (Cloudflare Web Analytics). Nothing runs inside the logged-in app.

### A3. People and roles

| Role | Who | How they get in | What they mostly do |
|---|---|---|---|
| Visitor | anyone | no account | read, use the free tools |
| Student | DP1 or DP2, usually 16 or 17 | Door A; a parent approves if they're under 18 | courses, tutors, coursework |
| Parent | parent or legal guardian | invited by the student, or signs up first | approve, pay, watch, report |
| Tutor | IB graduate 18+, graduate tutor aged 17, or IB teacher | Door B, then the checklist | teach lessons |
| Coach | a tutor aged 18+ who passed the integrity course | from tutor home | coursework coaching |
| Course lead | a tutor with a verified 7 whose course was accepted | applies from tutor home | writes and records a course |
| Guardian of a tutor | the parent of a 17-year-old tutor | invited by the tutor | co-signs, receives payouts, sees their lessons |
| Staff: verifier | you, or a trained helper | invitation | checks documents |
| Staff: safeguarding lead | your parent, an adult | invitation | reads every report and decides |
| Staff: integrity reviewer | an IB teacher, paid per review | invitation | reviews coaching recordings |
| Staff: subject lead | a verified 7 or a teacher | invitation | checks course content and corrections |
| Staff: admin | you and your parent | invitation | money, settings, open books |
| School coordinator or teacher (v2) | staff at a school on a plan | invitation | help logs, Marker teacher mode |

Rules for accounts:
- **One person, one account.** Someone with two roles, like a teacher who is also a parent, switches role from the account menu. The two views never share a screen.
- **Linking:** a student can link up to two parents, and a parent can link any number of children.
- **Under-18 students never pay.** Their parent does.
- **At 18, the student decides.** On their 18th birthday we ask whether their parent keeps seeing their account. Until they answer, nothing changes.

### A4. Who can do what

| Action | Student (under 18) | Parent | Tutor | Staff |
|---|---|---|---|---|
| Browse courses, tutors, free tools | yes | yes | yes | yes |
| Use the site before a parent approves | browse, free tools, course previews, save tutors | - | - | - |
| Buy a course | asks the parent | yes | - | - |
| Ask for a free place | yes (the parent is told) | yes | - | - |
| Message a tutor | after approval | yes, in their own thread with the tutor | replies | only on a report |
| Read a student's messages | their own | all of their child's, read-only | their own threads | only on a report |
| Book a lesson | requests it | approves and pays | accepts or declines | - |
| Post on the request board | after approval | yes | replies | moderates |
| Join a lesson | yes | any lesson, as an observer | yes | on a report or a review |
| Open a recording | no | asks the safeguarding lead | no | safeguarding lead and integrity reviewer only, and every opening is logged |
| Write a help log | adds their next step | no | the coach writes it | - |
| Read help logs | yes | yes | their own | yes |
| Upload to the Marker | yes | sees the reports | no | sees reports, never files |
| Review a tutor | after a paid, finished lesson | same rule | replies once | removes abuse only |
| See the student's school | yes | yes | no: only first name, DP year, subjects, session | yes |
| Report a concern | yes | yes | yes | handles it |

### A5. Site map

**Public (fortyfive.study).**

```
/                                Home
/courses                         Course catalogue
/courses/[subject]/[course]      Course page
/tutors                          Tutor search
/tutors/[name-id]                Tutor profile
/coursework                      Coaching and the Marker: the rules
/coursework/accuracy             Marker accuracy, subject by subject
/tools                           Free tools
/tools/predictor   /tools/next-point   /tools/timetable
/tools/coursework-planner   /tools/results-day
/honesty                         The ten promises
/honesty/fees   /honesty/open-books   /honesty/corrections   /honesty/scorecard
/safety                          For parents: how lessons stay safe
/safety/report                   Report a concern, no account needed
/schools                         For schools
/teach                           Teach on FortyFive
/about   /contact
/legal/terms   /legal/privacy   /legal/refunds
/legal/tutor-agreement   /legal/coursework-code
/signin   /signup   /signup/student   /signup/parent   /signup/tutor
/consent/[token]                 A parent approves from the invite
```

**The app (/app, after sign-in).** The menu depends on the role.

```
Student   /app   /app/courses/[id]   /app/tutors   /app/bookings
          /app/requests   /app/coursework   /app/coursework/[piece]
          /app/marker/[report]   /app/messages   /app/account
Parent    /app   /app/approvals   /app/bookings   /app/messages
          /app/payments   /app/logs   /app/settings
Tutor     /app   /app/onboarding   /app/requests   /app/calendar
          /app/students   /app/logs   /app/earnings   /app/profile
          /app/training   /app/authoring
Guardian  /app   (their tutor's lessons, messages, payouts, agreement)
Shared    /app/lessons/[id]   (lesson details, then the lesson room)
```

**Staff console (admin.fortyfive.study).** It has its own sign-in with two-factor authentication.

```
/verify   /safeguarding   /integrity   /content
/payments   /people   /marker   /books
```

The school console (`/school`) comes in v2.

### A6. Navigation

**Public header.**

```
45. FortyFive   Courses  Tutors  Coursework  Free tools  For parents  For schools     Sign in  [ Join ]
```

- **Join** opens the door chooser (B1).
- **On a phone:** the logo, Sign in and Menu, which opens a full-screen list.
- **Footer:** four columns (Learn, Trust, Join, Legal), a **Report a concern** link, and the line "Not affiliated with or endorsed by the International Baccalaureate Organization."

**App top bar.**

```
45.  [ Student ]   Today  Courses  Tutors  Coursework  Messages        Report   (A)
```

- The role chip says which home you're in.
- **Report** is always in the top bar, in red text, on every screen and every device.

**Phone bottom bars**, five items at most:

| Role | Tabs |
|---|---|
| Student | Today, Courses, Tutors, Coursework, Messages |
| Parent | Home, Approvals (with a count), Messages, Payments, Settings |
| Tutor | Home, Requests, Calendar, Earnings, More |

## B. The sign-ups

### B1. The door chooser (`/signup`)

Two doors, equal in size. Nobody lands in a mixed sign-up.

```
+------------------------------------------------------------------------+
| 45. FortyFive                                              Sign in     |
+------------------------------------------------------------------------+
|  JOIN FORTYFIVE                                                        |
|  Which door is yours?                                                  |
|                                                                        |
|  +-------------------------------+  +-------------------------------+  |
|  | I'm a student or a parent     |  | I teach the IB                |  |
|  |                               |  |                               |  |
|  | Courses, checked tutors and   |  | IB graduates (17 and over)    |  |
|  | coursework help. Under 18?    |  | and IB teachers. Keep 90% of  |  |
|  | A parent approves first.      |  | every lesson. About 10 days   |  |
|  |                               |  | from sign-up to live.         |  |
|  | [ I'm a student ] [ Parent ]  |  | [ Apply to teach ]            |  |
|  +-------------------------------+  +-------------------------------+  |
|                                                                        |
|  From a school? Write to us and we'll set you up.                      |
+------------------------------------------------------------------------+
```

On a phone the two cards stack, students and parents first.

### B2. Student sign-up (`/signup/student`): four steps

A line at the top reads "Step 2 of 4". There is no percentage bar. Back always works and nothing typed is lost.

1. **Account.**
   - Fields: first name, email, password (or "email me a sign-in link"), date of birth.
   - The note under birthday: "We ask because the law treats under-18s differently. Nobody else sees it."
   - A student aged 18 or over skips step 4 and gives consent themselves.
2. **School.**
   - Search the 629 Diploma schools by name or city.
   - Picking a school fills in its exam month from the IB directory ("Exams: November"). The student can change it.
   - Year: DP1 or DP2. Exam session: worked out ("November 2027") and editable.
   - "My school isn't listed" lets them type it in, and a person checks it.
3. **Subjects.**
   - Six slots, one per IB group. The chips show only what that school runs, with a "Show every IB subject" link.
   - An HL or SL switch on each chip.
   - If the count of HL subjects isn't 3 or 4, a hint appears: "Most students take 3 HL. Check with your coordinator." It never blocks.
   - TOK, the EE and CAS are added automatically.
4. **Your parent.**
   - Fields: the parent's name, email and mobile.
   - The button reads "Send the request". The next screen shows "Waiting for Priya", with Resend and Change buttons and a "While you wait" list: free tools, course previews, saving tutors.
   - The parent hears from us straight away, again after 24 hours and again after 72 hours. The request expires after 14 days.

```
+------------------------------------+
| <  Step 2 of 4                     |
|                                    |
| Which school are you at?           |
| +--------------------------------+ |
| | example int|                   | |
| +--------------------------------+ |
| | Example International School   | |
| |   Pune             Exams: May  | |
| | Example World School           | |
| |   Coimbatore       Exams: Nov  | |
| +--------------------------------+ |
| My school isn't listed             |
|                                    |
| Year      ( ) DP1   (o) DP2        |
| Exams     [ November 2026     v ]  |
|                                    |
| [ Next ]                           |
+------------------------------------+
```

### B3. Parent approval (`/consent/[token]`)

Four short screens. This is the most important form on the site, so it gets the plainest words.

1. **"Aarav wants to join FortyFive."**
   - Three lines on what FortyFive is.
   - What we keep: first name, school, subjects, exam session, bookings, messages.
   - What we never do: ads, selling data, tracking.
   - Button: [ Continue ].
2. **"Confirm you're an adult."**
   - Verify with DigiLocker, which shares only that you're over 18. This is the route the DPDP Rules point to, and the lawyer confirms the final method.
   - Then set a password.
3. **Your choices.**
   - **Record lessons?** Yes or No, and nothing is preselected. The note says lesson recordings are kept 30 days and opened only if someone reports a problem. Coursework coaching is always recorded and kept until results, because that recording proves the help was fair.
   - **Bookings:** "You approve and pay for each booking." A standing approval for one tutor comes later.
   - **Messages from us:** email always; text messages for approvals, on or off.
4. **"Done. Aarav can book and message now."**
   - This leads to the parent home.
   - The consent record is saved: the time, the method and the version of the notice. The parent can download it.

A **"This isn't my child"** or **"I don't agree"** link on screen 1 leaves the student's account limited. The student sees "Your parent didn't approve the account." We don't give a reason or name anyone.

```
+------------------------------------+
| 45. FortyFive                      |
|                                    |
| Aarav wants to join FortyFive      |
|                                    |
| Courses by people who scored 7s    |
| and tutors we've checked, for IB   |
| Diploma students. You'll see every |
| booking and every message.         |
|                                    |
| What we keep                       |
|  first name, school, subjects,     |
|  exam session, bookings, messages  |
| What we never do                   |
|  ads, selling data, tracking       |
|                                    |
| [ Continue ]                       |
| This isn't my child                |
+------------------------------------+
```

### B4. Parent first (`/signup/parent`)

1. Account: name, email, mobile, password.
2. Verify you're an adult with DigiLocker.
3. **Add a child:** first name, date of birth and the child's email. The child gets an invite to set a password and finish steps 2 and 3 of B2.
4. Your choices: the same as B3 screen 3.
5. Parent home. More children can be added later from Settings.

### B5. Tutor sign-up (`/signup/tutor`) and the checklist

1. **Account and birthday.**
   - Under 17: "You need to have finished the IB and be at least 17." Sign-up stops there.
   - At 17: the graduate tutor track only. At 18 or over: the graduate or teacher track.
2. **Track**, shown as three cards with the rules for each:
   - IB graduate: 18 or over, a verified 6 or 7.
   - Graduate tutor: 17, a verified 7, a parent co-signs.
   - IB teacher: credentials and IB teaching experience.
3. **What you'll teach:** subject, level and papers, plus evidence. Graduates upload the IB results document as a PDF; teachers upload a CV and a letter from their school.

After that the tutor home *is* the checklist, until every row is green.

| # | Step | Who | Usual time |
|---|---|---|---|
| 1 | ID through DigiLocker | you, 2 minutes | instant |
| 2 | Results or credentials checked | us | 2 working days |
| 3 | Background check (18+) or a DP Coordinator reference (17) | the check provider, or your coordinator | 3 to 7 days |
| 4 | Guardian co-signs (17 only) | your parent | same day |
| 5 | Demo lesson, 15 minutes | you and a subject lead | book a slot |
| 6 | Safeguarding course and quiz (8 of 10 to pass) | you, 30 minutes | instant |
| 7 | Code of conduct and tutor agreement, e-signed | you, and your guardian at 17 | 5 minutes |
| 8 | Profile: about, subjects, price, free times | you | 15 minutes |
| 9 | Payout account (Razorpay KYC: PAN and bank) | you, or your guardian at 17 | 1 to 3 days |

Each row has one of four states: **To do**, **Waiting for us**, **Needs a fix** (with the reason) or **Done**.

After going live, two optional extras appear:
- **Coursework coach:** the integrity course, EE or TOK evidence, and a coursework rate. 18 and over only.
- **Course lead:** apply with an outline.

When a step doesn't go through:
- **The name on the results doesn't match the ID:** "Needs a fix: the name on your results document doesn't match your ID. Upload it again, or write to us."
- **No reference after 7 days:** the coordinator gets a reminder, and the tutor can name their head of school instead.
- **A background check comes back flagged:** the safeguarding lead decides, privately. The tutor hears only the outcome.
- **The demo lesson doesn't pass:** written feedback, and they can try again after 30 days.

```
+------------------------------------------------------------------------+
| 45. [ Tutor ]   Home  Training                          Report   (A)   |
+------------------------------------------------------------------------+
| Welcome, Ananya. 6 of 9 done.                                          |
| Your profile goes live when every step is done. Most people take a     |
| week.                                                                  |
|                                                                        |
|  [x] 1  ID checked with DigiLocker                          Done       |
|  [x] 2  IB results checked: Economics HL 7, Business HL 7   Done       |
|  [~] 3  Background check                         Waiting for us (3d)   |
|  [x] 5  Demo lesson with Rohan, 14 Dec                      Done       |
|  [x] 6  Safeguarding course, 9 of 10                        Done       |
|  [x] 7  Code of conduct and agreement signed                Done       |
|  [ ] 8  Your profile                              [ Fill it in ]       |
|  [!] 9  Payout account     Needs a fix: bank name does not match       |
|                                                      [ Fix it ]        |
|  ( step 4 is only for tutors under 18 )                                |
|                                                                        |
|  Questions? Write to us. We reply within a working day.                |
+------------------------------------------------------------------------+
```

## C. Every screen

Each screen lists its **job**, its **content** from top to bottom, its **actions**, its **states** (empty, waiting, error) and anything that changes on a **phone**. Screen numbers (C1, C2...) are used in the build plan in Part H.

### Public site

#### C1. Home (`/`)

**Job:** say what FortyFive is in five seconds, and send each person through the right door.

**Content:**
1. **Hero.**
   - Label: FOR IB DIPLOMA STUDENTS.
   - Headline: "Mastering the IB Diploma. Nothing else."
   - One line: "Courses by people who scored 7s, tutors we've checked, and coursework help that stays inside the IB's rules."
   - The two doors, as cards (B1).
2. **Proof strip.** Real numbers only, once they're true: "34 checked tutors · 1,200 lessons · next open-books report: July". Before launch it says: "Pilot starts February 2027."
3. **What we do:** four blocks (Courses, Tutors, Coursework, Free tools), one line and one link each.
4. **Two cards side by side:**
   - **Where your money goes:** the ₹1,000 lesson receipt, with "Read all ten promises".
   - **For parents:** four safety promises, with "How we keep lessons safe".
5. **Try it:** a small predicted-total calculator using the grade predictor. It needs no sign-up.
6. **For schools:** one line and a link.
7. **Questions:** six, each opening on its own.
   - Is it official IB?
   - Who are the tutors?
   - Do you help with the IA?
   - What does it cost?
   - Is it safe for my child?
   - Can I get a free place?
8. **Footer.**

```
+------------------------------------------------------------------------+
| 45. FortyFive  Courses Tutors Coursework Free tools For parents ...    |
|                                                  Sign in  [ Join ]     |
+------------------------------------------------------------------------+
| FOR IB DIPLOMA STUDENTS                                                |
| Mastering the IB Diploma.                                              |
| Nothing else.                                                          |
| Courses by people who scored 7s, tutors we've checked, and coursework  |
| help that stays inside the IB's rules.                                 |
| +--------------------------------+  +--------------------------------+ |
| | I'm a student or a parent    > |  | I teach the IB               > | |
| | Find a course or a tutor       |  | Keep 90% of every lesson       | |
| +--------------------------------+  +--------------------------------+ |
|------------------------------------------------------------------------|
| Pilot starts February 2027                                             |
|------------------------------------------------------------------------|
| WHAT WE DO                                                             |
| Courses          Tutors           Coursework        Free tools         |
| one line >       one line >       one line >        one line >         |
|------------------------------------------------------------------------|
| WHERE YOUR MONEY GOES            | FOR PARENTS                         |
| Student pays        Rs 1,000.00  | - Every tutor checked               |
| Tutor gets (90%)      Rs 900.00  | - You see every message             |
| FortyFive's fee       Rs 100.00  | - Lessons 7 am to 9 pm only         |
|   GST, payment fees    Rs 41.51  | - A named adult reads every report  |
| Left for FortyFive     Rs 58.49  |                                     |
| Read all ten promises >          | How we keep lessons safe >          |
|------------------------------------------------------------------------|
| TRY IT   Your six grades [7][6][6][5][6][5]  TOK/EE [B][A]  = 38       |
|------------------------------------------------------------------------|
| FOR SCHOOLS   A free pilot for your DP1s.  Talk to us >                |
| QUESTIONS     + Is it official IB?   + Who are the tutors?  ...        |
+------------------------------------------------------------------------+
| Learn | Trust | Join | Legal                     Report a concern      |
| Not affiliated with or endorsed by the International Baccalaureate ... |
+------------------------------------------------------------------------+
```

**Phone:** everything stacks into one column, the doors come straight after the headline, and the predictor uses dropdowns.

#### C2. Course catalogue (`/courses`)

**Job:** find the right course, or learn it doesn't exist yet.

- **Filters along the top:** subject group, subject, HL or SL, exam session.
- **Course cards:**
  - title (subject and paper);
  - lead's name with their verified badge;
  - lessons and hours;
  - "₹1,499 · free if you ask";
  - one line: "Not for you if...".
- **Empty state:** "No course for this subject yet. We add subjects in the order students ask." The [ Ask for this subject ] button needs an account, so it only counts real students.

#### C3. Course page (`/courses/[subject]/[course]`)

**Job:** let the student decide honestly, including deciding not to buy.

**Content:**
1. Title.
2. Lead (verified badge, one line).
3. What it covers in 3 lines.
4. Price and the receipt.
5. Buttons: [ Buy ] [ Ask for a free place ] [ Watch lesson 1 free ].
6. **Don't buy this if...**: two or three honest lines, such as "you're already scoring 6s on Paper 1 under timed conditions".
7. **Outline:** modules, then lessons with their length. Lesson 1 is marked as free.
8. What's inside: videos, notes, practice, the predicted mock, a live hour each month.
9. About the lead.
10. **Reviews:** enrolled students only. Each one shows the reviewer's subject, session and the date.
11. **Refund rule:** a full refund within 7 days if you've watched less than a quarter.
12. Questions.

**Actions:**
- An under-18 student's Buy becomes **Ask my parent**. The parent gets an approval card (C25) with the price and the receipt.
- **Ask for a free place** asks for nothing: one click, granted at once, one free place per course per student. The parent is told.

**Phone:** a sticky bar at the bottom with the price and the [ Buy ] button.

```
+------------------------------------------------------------------------+
| COURSES / ENGLISH A: LANGUAGE AND LITERATURE                           |
| Paper 1, the method                                                    |
| Led by Meera K.  English A HL 7 (verified)                             |
| How to annotate an unseen text in 15 minutes and write an analysis     |
| that reaches the top band.                                             |
|                                                                        |
| Rs 1,499, GST included          [ Buy ]  [ Ask for a free place ]      |
| Full refund within 7 days       [ Watch lesson 1 free ]                |
|------------------------------------------------------------------------|
| DON'T BUY THIS IF                                                      |
| - you already score 6s on Paper 1 in timed practice                    |
| - you want someone to mark your school essays (we don't)               |
|------------------------------------------------------------------------|
| OUTLINE                                    24 lessons, 3 h 40 min      |
| 1 How Paper 1 is marked                                                |
|   1.1 The four criteria                            8 min    Free       |
|   1.2 What moves a 4 to a 6                       11 min               |
| 2 Annotating in 15 minutes                                             |
|   ...                                                                  |
|------------------------------------------------------------------------|
| REVIEWS (enrolled students only)                                       |
| "The annotation method saved me ..."  DP2, May 2027 session, 3 Mar     |
+------------------------------------------------------------------------+
```

#### C4. Tutor search (`/tutors`)

**Job:** find a tutor you can trust for one paper, at a time that works.

- **Filters:**
  - subject, level, paper, session;
  - price range;
  - free times (weekday evenings, weekends);
  - track (graduate, teacher);
  - "coaches coursework".
- **Ranking note** under the filters: "Sorted by subject match, free times and reviews. Nobody pays to rank higher."
- **Result cards:**
  - first name and initial;
  - track label ("IB graduate 2026", "Graduate tutor, 17", "IB teacher");
  - a verified badge for each subject;
  - price per hour;
  - lessons taught;
  - rating (shown only from 3 reviews);
  - next free slot;
  - [ Free intro call ] [ View ].
- **Empty state:** "No tutor matches all of that. Try fewer filters, or post a request and tutors will come to you." Then [ Post a request ].
- **Phone:** filters sit behind a "Filters (3)" button that opens a sheet.

```
+------------------------------------------------------------------------+
| Tutors                                                                 |
| [ Economics       v] [ HL v] [ Paper 1 v] [ Nov 2027 v] [ More v ]     |
| Sorted by subject match, free times and reviews. Nobody pays to rank.  |
|------------------------------------------------------------------------|
| +--------------------------------------------------------------------+ |
| | Ananya R.   IB graduate 2026                         Rs 1,200 / h  | |
| | Economics HL 7 (verified)   Business HL 7 (verified)               | |
| | 38 lessons   4.9 from 12 reviews   Coaches coursework              | |
| | Next free: Tue 5 pm              [ Free intro call ]  [ View ]     | |
| +--------------------------------------------------------------------+ |
| | Rahul S.    Graduate tutor, 17                         Rs 800 / h  | |
| | Economics HL 7 (verified)                                          | |
| | 6 lessons   reviews show from 3                                    | |
| | Next free: Wed 6 pm              [ Free intro call ]  [ View ]     | |
| +--------------------------------------------------------------------+ |
|  Show 10 more                                                          |
+------------------------------------------------------------------------+
```

#### C5. Tutor profile (`/tutors/[name-id]`)

**Job:** show everything a parent needs to say yes, and nothing that lets anyone contact the tutor off FortyFive.

**Content:**
1. **Header:**
   - name, track, verified badges;
   - lesson price, and coursework price if they coach;
   - [ Free intro call ] [ Book a lesson ] [ Message ].
2. **About:** 600 characters at most. No links, and contact details are stripped.
3. **What I teach:** a table of subject, level, papers and their verified grade.
4. **Free times:** this week and next, shown in the visitor's time zone.
5. **Reviews:** all of them, newest first, filterable by subject. The tutor's one reply sits under each.
6. **Rules:** cancellation, intro call, recording.
7. "Report this profile".

**Actions:** booking and messaging ask visitors to sign in first. For a student still waiting for their parent's approval, the buttons say why they're greyed out.

**Phone:** the header stacks; the buttons sit in a sticky bottom bar.

```
+------------------------------------------------------------------------+
| Ananya R.                         Rs 1,200 / h lesson                  |
| IB graduate 2026                  Rs 1,500 / h coursework coaching     |
| Economics HL 7 (verified)  Business HL 7 (verified)                    |
| 38 lessons, 4.9 from 12 reviews                                        |
| [ Free intro call ]  [ Book a lesson ]  [ Message ]                    |
|------------------------------------------------------------------------|
| ABOUT                                                                  |
| I sat the November 2026 papers. I teach Paper 1 essays the way I ...   |
|------------------------------------------------------------------------|
| WHAT I TEACH            Level   Papers            My grade             |
| Economics               HL      1, 2, 3           7 (verified)         |
| Business Management     HL      1, 2, 3           7 (verified)         |
|------------------------------------------------------------------------|
| FREE TIMES (your time, IST)                                            |
|        Mon  Tue  Wed  Thu  Fri  Sat  Sun                               |
| 5 pm    .    o    .    o    .    o    .                                |
| 6 pm    .    o    o    .    .    o    .                                |
|------------------------------------------------------------------------|
| REVIEWS (12)    [ All subjects v ]                                     |
| "Finally understood evaluation..."  Economics HL, DP2, 2 Mar           |
|   Ananya: Thank you! Keep timing the essays.                           |
|------------------------------------------------------------------------|
| Cancel 24 h before for a full refund.        Report this profile       |
+------------------------------------------------------------------------+
```

#### C6. Coursework (`/coursework`)

**Job:** explain coaching and the Marker so plainly that a DP Coordinator would forward the page.

**Content:**
1. The line in one sentence.
2. "A coach does" next to "A coach never".
3. **How an hour works**, in six steps: pick the piece, sign the code, book, session, help log, show your supervisor.
4. Hour limits per piece.
5. The receipt for a ₹1,500 coaching hour.
6. A sample help log.
7. **The Marker:** what a report shows, and what it never shows.
8. **Accuracy table:** subject, component, pieces tested, share within 2 marks, status (Open or Testing).
9. "Your school's rules come first".
10. **Questions:** "Do I have to tell my supervisor?" (yes, and here's the link), "Can a coach read my draft?" (no), "Will this get flagged?" (the help log is your evidence).

#### C7. Free tools (`/tools` and one page each)

- **Predictor:** six grades plus TOK and EE gives the total. Grade boundaries are kept by session.
- **Next point:** enter mock marks per paper; it shows where the next point costs the fewest hours, using the boundaries.
- **Timetable:** exam dates and free days in, a revision plan out, printable.
- **Coursework planner:** pieces, school deadlines, milestones, a source log, a reflection diary for the EE.
- **Results-day guide:** live on 16 December and early July. It covers remarks, retakes and what to tell universities.

None of the tools needs an account. Work is kept in the browser on that device, and **Save to my account** appears for signed-in students. Each page ends with one quiet link to the matching course or tutors, never a pop-up.

#### C8. Honesty (`/honesty` and its pages)

- **The ten promises:** the charter, each with its proof link.
- **Fees:** receipts for a lesson, a coaching hour, a course and a Marker check.
- **Open books:** a quarterly table with income, tutor earnings, author earnings, costs, what was left and free places given.
- **Corrections:** every error found in a course, the date it was fixed, and who found it (if they want credit).
- **Scorecards:** how the predicted papers did against the real ones each session, and the Marker's accuracy.

#### C9. For parents (`/safety`) and Report a concern (`/safety/report`)

**Safety page:**
- who tutors, with the checks for each track;
- how lessons work;
- what parents see;
- recording;
- what happens after a report;
- the safeguarding lead's name, email and phone;
- "If a child is in danger now, call 112. Childline: 1098."

**Report form** (no account needed):
1. What happened, picked from categories:
   - someone asked for contact details;
   - inappropriate message or behaviour;
   - coursework was written or edited;
   - a fake review or profile;
   - something else.
2. Who and when.
3. Details.
4. Your contact details (optional for the public, filled in for members).
5. [ Send ].

The confirmation says what happens next and by when.

#### C10. For schools (`/schools`)

1. The free pilot for DP1s.
2. The school plan and its price.
3. What a school sees: help logs and Marker teacher mode in v2, switches for coaching and the Marker.
4. How FortyFive keeps to the IB's integrity policy.
5. A contact form for coordinators.

#### C11. Teach on FortyFive (`/teach`)

1. **Why:** keep 90%, no lead fees, students who were checked too.
2. **The three tracks** with their requirements.
3. **Going live in 9 steps**, shown as a timeline.
4. A receipt for a ₹1,000 lesson.
5. The rules: safety and coursework.
6. Questions, then [ Apply to teach ].

#### C12. Sign in (`/signin`)

- Email and password, or "email me a sign-in link". The same form serves students, parents and tutors, and the role decides where they land.
- Five wrong tries locks the account for 15 minutes and sends an email.
- Staff sign in elsewhere (admin.), with two-factor authentication.

### Student app

#### C13. Today (`/app`, student)

**Job:** answer "what should I do now?" in one glance.

**Content, top to bottom:**
1. **"Waiting for Priya to approve"**, shown only while it's true, with [ Resend ].
2. **Next lesson:** tutor, subject, time.
   - [ Join ] turns on 10 minutes before the start.
   - [ Reschedule ] and [ Cancel ] show the refund rule before you confirm.
3. **Continue your course:** "Paper 1, the method · 7 of 24 ticked · Next: 2.3 Tone and register".
4. **Your next point**, if the planner is set up: "Cheapest next point: Economics Paper 2, about 6 hours." Otherwise: "Set up the planner, 2 minutes."
5. **Coursework:** each piece with its next deadline, coaching hours left and Marker checks left.
6. **Messages:** the last two threads, under the banner "Your parent can see your chats."
7. **[ Ask for help ]** opens the request composer (C16).

**Empty state:** "Nothing booked yet. Watch a free first lesson, or find a tutor for one paper."

```
+------------------------------------+
| 45. [Student]            Report (A)|
|                                    |
| Hi Aarav                           |
|                                    |
| NEXT LESSON                        |
| Economics HL, Paper 1 essays       |
| with Ananya R.                     |
| Tue 9 Mar, 5:00 pm                 |
| [ Join ] opens 4:50 pm             |
| Reschedule  Cancel                 |
|                                    |
| CONTINUE                           |
| English P1, the method             |
| 7 of 24 ticked                     |
| Next: 2.3 Tone and register  >     |
|                                    |
| YOUR NEXT POINT                    |
| Economics Paper 2, about 6 hours > |
|                                    |
| COURSEWORK                         |
| Economics IA 2   due 30 Mar        |
| 2 of 4 coaching hours left  >      |
|                                    |
| [ Ask for help ]                   |
|------------------------------------|
| Today Courses Tutors Cwork Msgs    |
+------------------------------------+
```

#### C14. Course player (`/app/courses/[id]`)

**Job:** watch, read, practise and tick, with nothing to download.

**Desktop layout:**
- **Left:** modules, with a tick box beside each lesson.
- **Middle:** the video through an expiring link. Below it, three tabs:
  - **Notes:** drawn on the server, with the student's name faintly across each page.
  - **Practice:** our own question. From v1 it has an answer box and the Marker's practice marking.
  - **Get help:** the next monthly live hour, plus tutors for this paper.

There's no chat.

**Phone:** the video on top, the tabs below, and the modules in a drawer.

```
+------------------------------------------------------------------------+
| < My courses     English A: Paper 1, the method          7 of 24       |
|------------------------------------------------------------------------|
| MODULES               |  +------------------------------------------+  |
| 1 How it's marked     |  |                                          |  |
|  [x] 1.1 Criteria     |  |               video                      |  |
|  [x] 1.2 4 to 6       |  |                                          |  |
| 2 Annotating          |  +------------------------------------------+  |
|  [x] 2.1 First read   |  2.3 Tone and register            11 min       |
|  [x] 2.2 Purpose      |  [ Notes ]  [ Practice ]  [ Get help ]         |
|  [ ] 2.3 Tone      <  |  ----------------------------------------      |
|  [ ] 2.4 Structure    |  Notes for Aarav M. (faint, on every page)     |
| 3 Techniques          |  Tone is the writer's attitude ...             |
|  ...                  |                                                |
|                       |  [ Mark this lesson done ]                     |
+------------------------------------------------------------------------+
```

#### C15. Booking (student side)

1. **Type:**
   - free intro call, 15 minutes;
   - lesson, 30 or 60 minutes;
   - coursework coaching, 60 minutes, coaches only, starting from the coursework piece (C19).
2. **Time:** the tutor's free slots in the student's time zone. For under-18s, slots outside 7 am to 9 pm local time don't appear.
3. **What to cover:** optional, 300 characters. For example: "Paper 1 part (b) evaluation".
4. **Review:**
   - the price and the receipt;
   - the cancellation rule;
   - "This lesson will be recorded" if the parent chose that.
5. **Send:**
   - **Under 18:** [ Send to Priya for approval ]. The status reads "Waiting for Priya". The slot is held for 12 hours, then released.
   - **18 or over:** [ Pay ], through Razorpay.

```
+------------------------------------+
| <  Check and send                  |
|                                    |
| Lesson, 60 minutes                 |
| Ananya R.  Economics HL            |
| Tue 9 Mar, 5:00 to 6:00 pm         |
| Cover: Paper 1 (b) evaluation      |
|                                    |
| Price                  Rs 1,200.00 |
|  Ananya gets (90%)     Rs 1,080.00 |
|  FortyFive (10%)         Rs 120.00 |
|                                    |
| Recorded: yes (Priya's choice)     |
| Cancel by Mon 5 pm for a full      |
| refund.                            |
|                                    |
| [ Send to Priya for approval ]     |
| We hold this slot for 12 hours.    |
+------------------------------------+
```

#### C16. Requests (`/app/requests`)

- **Compose:**
  - subject, level, paper;
  - what help: one line;
  - how often;
  - until when;
  - budget per hour.
- **Posted requests** show replies from tutors: their plan, price and proposed times.
- **Choosing:** [ Ask Priya to choose ] for under-18s, or [ Choose ] for over-18s. Choosing starts a booking (C15) with that tutor.
- Requests close after 14 days or once one tutor is chosen. Tutors see no name and no school.

#### C17. Bookings and lesson details (`/app/bookings`, `/app/lessons/[id]`)

- **Lists:** Upcoming and Past.
- **Lesson detail:**
  - time, tutor, what to cover;
  - the recording status;
  - [ Join ];
  - the tutor's lesson notes afterwards, which the parent also sees;
  - [ Leave a review ] once a paid lesson is finished, within 14 days;
  - [ Book again ].

#### C18. Lesson room (`/app/lessons/[id]/room`)

1. **Check first:** camera, microphone and name.
2. **Banner:** "This lesson is recorded" or "Not recorded".
3. **The room:** video, screen share, and a simple whiteboard from v1.
4. **Side panel:** the tutor's notes as they're typed, and **Report** with a "leave now" option.
5. **For coaching sessions:** a banner reading "Coursework coaching: no files, no edits. Your coach will write a help log." At the end, the student types their next step in their own words.
6. **Who's in:** the parent can join as a named observer, shown as "Priya (parent) is watching".

```
+------------------------------------------------------------------------+
| Economics HL with Ananya R.    RECORDED     46:12 left   [ Leave ]     |
|------------------------------------------------------------------------|
| +-----------------------------------------------+  NOTES (Ananya)      |
| |                                               |  - (b) needs one     |
| |          Ananya          |       Aarav        |    clear judgement   |
| |                          |                    |  - use the article   |
| |                                               |    data, line 14     |
| +-----------------------------------------------+                      |
| [ Mic ] [ Camera ] [ Share screen ] [ Whiteboard ]   Report            |
| Priya (parent) can join at any time.                                   |
+------------------------------------------------------------------------+
```

#### C19. Coursework (`/app/coursework` and `/app/coursework/[piece]`)

**List:**
- every piece: IA by subject, EE, TOK essay, TOK exhibition;
- [ Add a piece ]: type, subject, working title (optional), the school's draft and final deadlines.

**Piece page:**
- **Header:** the piece and its deadlines.
- **Coaching:** "2 of 4 hours used", [ Book coaching ] (coaches in this subject only), and the help logs.
- **Marker:** "0 of 2 checks used", [ Start a check ], and past reports.
- **Planner:** milestones, a source log, and the reflection diary (EE).
- **[ Share with my supervisor ]:** a read-only link to the logs and Marker reports. It expires after 30 days and can be switched off.

**The coursework code** is signed once per piece, by the student and the parent, before the first coaching hour or Marker check. It has five lines:
1. The work is mine.
2. Coaches teach; they don't write.
3. I'll follow my school's rules.
4. I'll tell my supervisor I'm getting help.
5. I'll credit any AI feedback the way my school asks.

**At the limit:** "You've used all 4 coaching hours for this IA. That's the limit, so the work stays yours. Your supervisor is the next step."

```
+------------------------------------------------------------------------+
| COURSEWORK / Economics IA, commentary 2                                |
| Draft due 16 Mar    Final due 30 Mar        [ Share with supervisor ]  |
|------------------------------------------------------------------------|
| COACHING                      2 of 4 hours used                        |
| [ Book coaching ]                                                      |
|  Session 2, 14 Mar, Ananya R.   Covered: criterion D evaluation  >     |
|  Session 1, 2 Mar, Ananya R.    Covered: choosing the article    >     |
|------------------------------------------------------------------------|
| THE MARKER                    0 of 2 checks used                       |
| [ Start a check ]   One on a draft, one before you submit,             |
|                     at least 7 days apart.                             |
|------------------------------------------------------------------------|
| PLANNER                                                                |
|  [x] Article chosen 1 Mar   [x] Diagram drafted   [ ] Draft to teacher |
|  Sources (3)  >      Reflection diary  >                               |
+------------------------------------------------------------------------+
```

#### C20. Marker: start a check

1. Pick the piece. It's preselected when the check starts from a piece page.
2. **Draft or final.** The second check must come at least 7 days after the first.
3. **Upload:** PDF only, 20 MB at most. A scanned PDF gets a warning: "We can't read scans well; export from your document instead."
4. **Confirm**, with all three boxes ticked:
   - this is my own work;
   - my school allows AI feedback;
   - delete my file after 48 hours (already ticked and locked).
5. **Send.** "Marking takes about 5 minutes. We'll email you." The page updates by itself.

#### C21. Marker report (`/app/marker/[report]`)

**Content:**
1. A summary table: criterion, band, how sure.
2. **One section per criterion:**
   - the band and how sure it is;
   - the evidence ("p. 3, paragraph 2");
   - two or three things that work;
   - two or three questions to ask yourself.
3. **The checklist.**
4. **How to credit it:** "Feedback on this draft came from the FortyFive Marker (AI) on 14 March 2027."
5. Checks left.
6. [ Share with my supervisor ].
7. **"Think this is wrong? Tell us"**, which feeds the accuracy checks.

There is no chat box and no suggested text, and the report says so in its footer.

```
+------------------------------------------------------------------------+
| MARKER REPORT  Economics IA, commentary 2   Draft   14 Mar 2027        |
| Checks left on this piece: 1 of 2           [ Share with supervisor ]  |
|------------------------------------------------------------------------|
| Criterion                         Band          How sure               |
| A  Diagrams                       2 of 3        sure                   |
| B  Terminology                    2 of 2        sure                   |
| C  Application and analysis      2 to 3 of 3   fairly sure            |
| D  Key concept                    1 to 2 of 3   unsure: read the notes |
| E  Evaluation                     1 to 2 of 3   fairly sure            |
|------------------------------------------------------------------------|
| E  EVALUATION                     1 to 2 of 3, fairly sure             |
| Evidence: p. 3, paragraphs 2 and 3                                     |
| Works:  - you weigh short-run against long-run effects                 |
| Ask yourself:                                                          |
|  - Which stakeholder does the article leave out, and does that change  |
|    your judgement?                                                     |
|  - Is your final judgement tied to this market, or would it fit any?   |
|------------------------------------------------------------------------|
| CHECKLIST   [x] Article attached  [x] Word count 768  [ ] Source dated |
|------------------------------------------------------------------------|
| Credit line: Feedback on this draft came from the FortyFive Marker     |
| (AI) on 14 March 2027.        This report never suggests your words.   |
| Think this is wrong? Tell us                                           |
+------------------------------------------------------------------------+
```

The criteria shown are placeholders; the real rubric packs are written in our own words and checked by a subject lead.

#### C22. Messages (`/app/messages`)

- A list of threads, then the thread itself. The banner at the top is always there: "Priya (your parent) can see this chat."
- **Contact details are hidden as you type**, and the server catches them again. The check covers:
  - phone numbers, including ones written in words;
  - emails;
  - social handles;
  - UPI IDs;
  - links.

  They appear as "[contact details hidden: keep chats on FortyFive]", and the safeguarding inbox sees repeated attempts.
- No attachments in v0. From v1, images are allowed for maths questions, but never files of coursework.
- To-be-sent messages to under-18s wait during quiet hours (9 pm to 7 am) and are delivered at 7 am.

```
+------------------------------------+
| <  Ananya R.            Report     |
| Priya (your parent) can see this.  |
|------------------------------------|
|        Can we do Paper 1 (b)       |
|        next time?          Aarav > |
| < Yes! Bring one essay plan.       |
|   Ananya                           |
|        my number is [contact       |
|        details hidden: keep chats  |
|        on FortyFive]       Aarav > |
|------------------------------------|
| [ Write a message...       ] Send  |
+------------------------------------+
```

#### C23. Account (`/app/account`)

- Profile: first name, school, subjects, session.
- Linked parents.
- Messages from us.
- **Your data:** download it, or ask us to delete it. Deletion explains what has to be kept by law (invoices).
- Sign out.

### Parent app

#### C24. Parent home (`/app`, parent)

**Job:** see what needs your yes, and what happened this week.

**Content:**
1. A child switcher, as tabs with first names.
2. **Needs your approval:** cards (C25).
3. **This week:** lessons, each with [ Join quietly ].
4. **Recent help logs** and Marker reports.
5. **This month:** what you've spent, linking to the receipts.
6. **Safety:** [ Report a concern ] and the safeguarding lead's contact.

```
+------------------------------------------------------------------------+
| 45. [ Parent ]  Home  Approvals(1)  Messages  Payments  Settings  Rep. |
+------------------------------------------------------------------------+
| [ Aarav ]  [ Diya ]                                                    |
|------------------------------------------------------------------------|
| NEEDS YOUR APPROVAL                                                    |
| +--------------------------------------------------------------------+ |
| | Lesson: Economics HL with Ananya R. (Economics HL 7, verified)     | |
| | Tue 9 Mar, 5 to 6 pm.  Rs 1,200    Recorded: yes                   | |
| | [ Approve and pay ]   [ Decline ]        See the receipt >         | |
| +--------------------------------------------------------------------+ |
| THIS WEEK                                                              |
|  Tue 5 pm   Economics HL, Ananya R.            [ Join quietly ]        |
|  Sat 11 am  English P1 clinic (4 students)     [ Join quietly ]        |
| RECENT                                                                 |
|  Help log: Economics IA 2, session 2 (14 Mar)  >                       |
|  Marker report: Economics IA 2, draft (14 Mar) >                       |
| THIS MONTH   Rs 3,600 on 3 lessons   Receipts >                        |
| SAFETY       Report a concern    Safeguarding lead: [name], [phone]    |
+------------------------------------------------------------------------+
```

#### C25. Approvals (`/app/approvals`)

Each card shows:
- what it is: a lesson, coaching, a course or a Marker check;
- the tutor's verified badge;
- the time and price, with the receipt;
- [ Approve and pay ] or [ Decline ] (with an optional reason, which the student sees).

**Paying:**
- **From v1:** Razorpay checkout by UPI or card. A failed payment changes nothing: "Nothing was charged. Try again or use UPI."
- **In the v0 pilot:** "Approve" shows the tutor's UPI ID (or their guardian's) to the parent only, with [ I've paid ]. The tutor confirms receipt.

#### C26. The other parent screens

- **Bookings:** each child's upcoming and past lessons, with [ Join quietly ].
- **Messages:**
  - every thread the child has, read-only;
  - plus the parent's own threads with tutors.
- **Payments:** a receipt for each payment, refunds, and GST invoices (fee and course sales), all downloadable.
- **Logs and reports:** help logs and Marker reports for each child.
- **Settings:**
  - the consent record;
  - the recording choice;
  - messages from us;
  - linked children (add another);
  - **withdraw consent**, which explains what stops and what has to be kept by law;
  - delete our data.

### Tutor app

#### C27. Tutor home (`/app`, tutor)

Until the profile is live, this page is the checklist (B5). After that:

1. **Today:** lessons, each with [ Join ].
2. **Help logs to file:** a 24-hour countdown, and a note that the payout waits for the log.
3. **New requests** that match your subjects: three at most, then "See all".
4. **This month:** money in after the fee, and lessons taught.
5. **Latest reviews**, with [ Reply ] (once each).
6. **Profile tips**, only when they help. For example: "Add Saturday mornings: 40% of requests ask for weekends."

```
+------------------------------------------------------------------------+
| 45. [ Tutor ]  Home  Requests  Calendar  Students  Earnings  ...  Rep. |
+------------------------------------------------------------------------+
| TODAY                                                                  |
|  5:00 pm  Aarav, Economics HL, 60 min           [ Join ] at 4:50 pm    |
|  7:00 pm  Coaching: Kavya, Economics IA         recorded               |
|------------------------------------------------------------------------|
| HELP LOGS TO FILE                                                      |
|  Kavya, Economics IA, 12 Mar     due in 9 h     [ Write the log ]      |
|  Your payout for this session waits for the log.                       |
|------------------------------------------------------------------------|
| NEW REQUESTS FOR YOU                                                   |
|  DP2, Economics HL, Paper 1 essays, 2 h a week until Jan, up to        |
|  Rs 1,000 / h                                          [ Reply ]       |
|  See all 6 >                                                           |
|------------------------------------------------------------------------|
| THIS MONTH   Rs 12,960 to you from 12 lessons      Earnings >          |
| REVIEWS      "Finally understood evaluation..."   [ Reply ]            |
+------------------------------------------------------------------------+
```

#### C28. Requests board (`/app/requests`, tutor)

- **Filtered to the tutor's subjects:** level, paper, how often, until when and budget, with no names and no schools.
- **[ Reply ]:** a plan (500 characters), a price and up to three proposed times. A tutor can reply once per request.
- **My replies:** sent, chosen, or not chosen.
- **Rules shown on the page:**
  - no contact details;
  - no promises of grades;
  - no coursework writing.

  Replies are checked like messages.

```
+------------------------------------------------------------------------+
| REQUESTS FOR YOUR SUBJECTS                         [ Economics HL v ]  |
|------------------------------------------------------------------------|
| DP2 student, Economics HL, Paper 1 essays                              |
| 2 hours a week until the January mocks. Up to Rs 1,000 an hour.        |
| Posted 2 h ago, 3 replies so far                         [ Reply ]     |
|------------------------------------------------------------------------|
| REPLY                                                                  |
| Your plan (500 characters)                                             |
| [ Week 1: diagnose with one timed essay. Weeks 2 to 6: one part   ]    |
| [ (a) and one (b) a week, marked in the lesson...                 ]    |
| Your price  [ Rs 950 ] an hour                                         |
| Times       [ Tue 5 pm ] [ Thu 6 pm ] [ Sat 11 am ]                    |
| No contact details, no grade promises. [ Send reply ]                  |
+------------------------------------------------------------------------+
```

#### C29. Calendar (`/app/calendar`)

- **Free times:** a weekly pattern plus exceptions (holidays, exams).
- **Booked lessons:** shown on the same calendar.
- **Time zones:** shown in the tutor's zone, with the student's zone on hover.
- **Late slots:** anything after 9 pm or before 7 am in a student's local time is greyed out with the reason ("under-18s: 7 am to 9 pm").
- **Optional sync** to Google Calendar, one way (from FortyFive, out).

#### C30. Students (`/app/students`)

- Each student shows: first name, subjects, lessons together, and the next lesson.
- **Lesson notes** are visible to the student and their parent. Tutors don't get private notes about students: that keeps everything in view.

#### C31. Help log (`/app/logs`)

Filed within 24 hours of each coaching session. The payout waits for it.

**Fields:**
1. The piece and session number (filled in for you).
2. **Criteria covered:** chips.
3. **Covered:** 300 characters, plain words.
4. **Student's next step:** typed by the student at the end of the session, and read-only for the coach.
5. **The signed statement:** "I did not read, edit, rewrite or comment on the draft, and no files changed hands."
6. [ File the log ].

Once filed, a log can't be edited. A correction is added as a dated note.

```
+------------------------------------------------------------------------+
| HELP LOG   Kavya, Economics IA, commentary 2, session 2 of 4           |
| 12 Mar, 7 to 8 pm, recorded                         due in 9 hours     |
|------------------------------------------------------------------------|
| Criteria covered   [ D Key concept ] [ E Evaluation ] [ + ]            |
| What we covered                                                        |
| [ How criterion D rewards linking the key concept to the article,  ]   |
| [ and what makes an evaluation point specific rather than general. ]   |
| Kavya's next step (her words)                                          |
|   "Find two stakeholders the article leaves out."                      |
|                                                                        |
| [x] I did not read, edit, rewrite or comment on the draft, and no      |
|     files changed hands.                                               |
| [ File the log ]     Filed logs can't be edited; corrections are       |
|                      added as dated notes.                             |
+------------------------------------------------------------------------+
```

#### C32. Earnings (`/app/earnings`)

**Content:**
- **The month:** lessons booked, what came to you, the fee, and what's still held.
- **A receipt for every lesson,** the same breakdown the parent sees.
- **Payout dates:** two days after each lesson, unless there's a complaint or a help log is missing.
- **Tax lines:** TDS (with PAN) and the GST/TCS status.
- **Downloads:** a monthly statement and the year's summary for tax.

**At 17:** the page shows it all, but says "Payouts go to Rakesh (your guardian)".

#### C33. Profile (`/app/profile`)

- **Preview as the public sees it.**
- **Fields:** about, subjects, papers, lesson price, coursework price (coaches only), intro calls on or off.
- **Photo:** optional, a head-and-shoulders shot of the tutor only.
- **Changes:** changes to price apply to new bookings only.

#### C34. Training (`/app/training`)

- **Courses:** safeguarding (required, every year) and coursework integrity (coaches, every year).
- **Track record:** dates passed and quiz scores, plus when each needs renewing.

#### C35. Course authoring (`/app/authoring`, course leads, v1)

1. **Outline:** modules and lessons.
2. **Video upload**, one per lesson.
3. **Notes editor:** markdown with LaTeX for maths, and a preview with the watermark.
4. **Practice questions:** our own questions with our own markschemes. There's a box to tick: "No IB paper text, no other publisher's material."
5. **Submit for review:** a subject lead leaves comments, and fixes are made.
6. **Sales report:** sales and the 70% share.

#### C36. Guardian view (`/app`, guardian of a 17-year-old tutor)

- **Visibility:** the tutor's bookings and lessons, plus every message thread, read-only.
- **Money:** payouts into the guardian's account, and the signed tutor agreement.
- **Safety:** [ Report a concern ].

### Staff console (admin.fortyfive.study)

Two-factor authentication on every account. Every opening of a document, recording or message is logged, with who and why.

#### C37. Verification queue (`/verify`)

- **Columns:**
  - ID (automatic from DigiLocker);
  - results documents to check;
  - references waiting;
  - background checks;
  - demo lessons.
- **An item:**
  - the document viewer next to the checklist ("name matches ID", "grade matches the claim", "session and year make sense");
  - [ Accept ] or [ Needs a fix ], with a reason picked from a list plus free text.
- **Timers:** each item shows its age. Anything over 2 working days goes red.

#### C38. Safeguarding inbox (`/safeguarding`)

The safeguarding lead's screen. It's the most important staff screen.

- **Order:** child safety first (red, same day), then contact attempts, coursework integrity, reviews and other.
- **A report shows:**
  - who reported, about whom;
  - the evidence, linked: messages, booking, recording;
  - earlier reports about the same people.
- **Actions:**
  - [ Suspend now ] stops their bookings and messages at once and can be undone;
  - contact the parent;
  - **log a police report** (date, station, reference), a duty under POCSO s19 and s21 with no internal inquiry first;
  - notes;
  - close with an outcome.
- **Audit trail:** every action has a time and a name.

```
+------------------------------------------------------------------------+
| SAFEGUARDING                         Open: 3   Due today: 1            |
|------------------------------------------------------------------------|
| ! CHILD SAFETY  Reported 10:42  About: tutor #T-0193  By: parent       |
|   "Asked my daughter for her Instagram"           [ Open ]             |
|   Contact attempts   Reported 09:15   Tutor #T-0211, 3rd attempt       |
|   Coursework         Reported Mon     Coach #T-0102, flagged by review |
|------------------------------------------------------------------------|
| REPORT  #R-0042                                                        |
| Evidence: messages (2) >   booking B-1180 >   recording (asks why) >   |
| Earlier reports about T-0193: none                                     |
| [ Suspend now ]  [ Contact parent ]  [ Log police report ]             |
| Notes ______________________________________________                   |
| Every action here is logged with your name and the time.               |
+------------------------------------------------------------------------+
```

#### C39. Integrity reviews (`/integrity`)

- **Queue:** a random 1 in 10 of coaching sessions, plus any that were flagged.
- **The reviewer:**
  - watches the recording, up to 30 minutes, at up to 2x speed;
  - reads the help log.
- **Checklist:**
  - Did the coach write, edit or dictate any of the work?
  - Did files change hands?
  - Does the log match the session?
- **Outcome:**
  - **Pass.**
  - **Concern:** coaching advice goes to the coach.
  - **Breach:** passed to the safeguarding lead, and the coach is suspended.
- **Pay:** ₹500 per review, to the reviewer.

#### C40. Content and corrections (`/content`)

- **Review:** course submissions with comments.
- **Corrections:** reports from students flow into a queue. A fix is published to the public corrections page with the date and credit.

#### C41. Payments (`/payments`)

- **Problems:** refunds, complaints within the 48-hour window, held payouts (complaint or missing log), and failed payouts.
- **Each case:** has a reason and a decision; the parent and tutor are told automatically.

#### C42. People and data (`/people`)

- **Find an account:** see its roles and links; suspend or restore it.
- **Consent records.**
- **Data requests** (access, correction, deletion), each with a due date.

#### C43. Marker ops (`/marker`)

- **Accuracy, per subject and component:** pieces tested, average error per criterion, the share within 2 marks, and an Open or Testing switch.
- **Rubric pack versions.**
- **"Think this is wrong" reports.**
- **Rule:** staff see reports, never the uploaded files.

#### C44. Open books (`/books`)

- **Every quarter:** income, tutor and author earnings, costs, what was left, and free places.
- **Publishing:** check it, then publish it to `/honesty/open-books`.

### School console (v2)

#### C45. School coordinator (`/school`)

- **Students:** the school's students who've linked, with their consent.
- **Help logs:** for those students.
- **Marker teacher mode:** upload a class set of drafts and get a first-pass report per student, for the teacher only.
- **Switches:** coaching on or off, and the Marker on or off, for the school's students.
- **Billing:** invoices for the school plan.

## D. The flows

### D1. Joining (student and parent)

```
Student signs up (B2) --> parent invited --> parent approves (B3) --> full access
        |                      |                      |
        |                      | no answer: reminders  | "I don't agree":
        |                      | at 24 h and 72 h,     | account stays limited
        |                      | expires at 14 days    |
        v                      v                      v
   limited mode:          student can change      student sees "Your parent
   browse, free tools,    the parent's contact    didn't approve the account"
   previews, save tutors
```

A student aged 18 or over goes straight to full access and gives their own consent.

### D2. A lesson booking, start to finish

Every booking moves through these states. Each change tells the right people (Part E).

```
REQUESTED --(student under 18)--> WAITING FOR PARENT --approve+pay--> CONFIRMED
    |                                  |  decline --> DECLINED
    | (18+ pays)                       |  12 h, no answer --> EXPIRED (slot freed)
    v
CONFIRMED --start--> IN PROGRESS --end--> FINISHED --48 h, no complaint--> PAID OUT
    |                     |                   |
    | cancelled           | no-show           | complaint within 48 h
    v                     v                   v
 CANCELLED            NO-SHOW            HELD (a person decides)
```

What each case does:
- **The tutor declines a request:** the parent isn't charged, and the student sees two other tutors with free times.
- **The slot gets taken while the parent decides:** it can't, because the slot is held for 12 hours.
- **The time is outside 7 am to 9 pm for an under-18:** the slot never appears.
- **The tutor wants to move a lesson:** they propose a new time, and the student and parent accept. If nobody accepts, it's cancelled with a full refund.

### D3. The request board

1. The student posts. Under-18s post only once their parent has approved the account.
2. Tutors who teach that subject see it, with no names or schools, and reply once each.
3. The student, or the parent for under-18s, compares the replies and picks one. A booking (D2) starts with that tutor.
4. A request closes after 14 days or once a tutor is picked. The tutors who weren't picked are told politely.

### D4. Free intro call

- 15 minutes, free, once per student per tutor.
- It happens in the lesson room. The parent is welcome and is invited automatically.
- It's recorded only if the parent chose recording.
- Messages and the lesson room hide contact details, as always.

### D5. Lesson day

1. **24 hours before:** a reminder to the student, the parent and the tutor.
2. **1 hour before:** a reminder to the student and the tutor.
3. **10 minutes before:** [ Join ] turns on.
4. **No-shows:**
   - **The tutor waits 15 minutes:** a student no-show, so the tutor gets half.
   - **The student waits 15 minutes:** a tutor no-show, so the student gets a full refund, and the tutor gets a strike (three strikes and they're removed).
5. **After the lesson:**
   - the tutor adds lesson notes;
   - the student gets a review prompt;
   - for coaching sessions, the help log is due within 24 hours.

### D6. Cancelling and refunds

| Who cancels | When | Money |
|---|---|---|
| Student or parent | more than 24 hours before | full refund |
| Student or parent | less than 24 hours before, or no-show | tutor gets half |
| Tutor | any time less than 24 hours before, or no-show | full refund, and a strike for the tutor |
| Anyone | unhappy after a lesson, within 48 hours | payout held; a person decides |
| Course buyer | within 7 days, less than a quarter watched | full refund |

Refunds go back to the way the parent paid, and the receipt is updated.

### D7. Reviews

- **Who:** only after a paid, finished lesson, within 14 days. One review per lesson, with stars and up to 500 characters.
- **The tutor's side:** they can reply once, but can't hide or delete a review.
- **Removal:** only for abuse or personal details, and the public review page says how many were removed.
- **The rating:** a tutor's rating appears only once they have 3 reviews.

### D8. Buying a course, or a free place

```
Course page --[Buy]--> (under 18) parent approval card --> pay --> course unlocked
            --[Ask for a free place]--> unlocked at once, parent told, no questions
```

There's one free place per course per student. Free places are counted in the open books.

### D9. Coursework coaching

1. Add the piece (C19) and sign the coursework code. The student and the parent sign once per piece.
2. Book an hour with a coach in that subject. The page shows the hours left.
3. Parent approval and payment, as in D2.
4. **The session:** always recorded, with no files and a banner saying so. At the end the student types their next step.
5. The coach files the help log within 24 hours. The payout is held until it's filed.
6. The log goes to the student and the parent, and the student shares it with their supervisor.
7. **At the limit:** the booking button is replaced by the limit message (C19).
8. **Reviews:** 1 in 10 sessions is picked at random for integrity review (C39), as is any flagged session.

### D10. A Marker check

```
Start a check (C20) --> upload --> marking (3 passes, about 5 min) --> report (C21)
   | second check: at least 7 days after the first                     |
   | subject in "Testing": button off, "We open a subject once its      |
   |   accuracy is published"                                           v
   | file deleted after 48 hours, report kept               share with supervisor
```

**If marking fails** (an unreadable PDF, or a timeout), the check isn't used up. The student sees "We couldn't read this file. Export it again from your document and retry."

### D11. Reporting a concern

1. [ Report ] is on every screen, plus the public form (C9).
2. **The report:** pick a category, then who and when, and the details. Evidence (the thread, the booking) is attached automatically.
3. **Child safety:** the safeguarding lead gets an SMS and an email at once, at any hour. Everything else is read within 24 hours.
4. **The person reporting** gets: "Thanks. A trained adult will read this within 24 hours. If someone is in danger now, call 112."
5. **If a child may have been abused:** suspend the account, tell the parent, report to the police or the Special Juvenile Police Unit straight away, log it, and fix the rule that failed.

### D12. Payouts

- **Normal case:** two days after a finished lesson, with no complaint, the money goes to the tutor's Razorpay linked account. For a tutor aged 17 it goes to their guardian's.
- **Coaching:** held until the help log is filed.
- **Statement:** a monthly one on the earnings page (C32).

### D13. Data rights and withdrawing consent

- **Download my data:** a ZIP of the account, bookings, messages and logs, ready within 7 days.
- **Delete my account:** the account and messages go. Invoices and records the law requires are kept for as long as tax law asks, and the page says so.
- **A parent withdraws consent:** the student's account goes back to limited mode, upcoming bookings are cancelled with full refunds, and data is deleted unless the law requires it.

### D14. Turning 18

- **Students:** on their birthday, a message asks: "Should your parent keep seeing your account?" They answer Keep or End. Until they answer, nothing changes.
- **Graduate tutors:** at 18 they move to the standard track (a background check, payouts to their own account). The guardian's view ends once that's done.

## E. Notifications

**Channels:**
- in-app;
- email;
- SMS only for one-time codes, parent approvals (if the parent chose them) and safety.

There are no push notifications in v0, because there's no phone app yet.

**Quiet hours for under-18s:** nothing between 9 pm and 7 am except safety messages. Anything else waits until 7 am.

| Event | Student | Parent | Tutor | Staff |
|---|---|---|---|---|
| Parent invite and reminders | - | email (+SMS) | - | - |
| Account approved | in-app, email | email | - | - |
| Booking needs approval | in-app | in-app, email (+SMS) | - | - |
| Booking confirmed | in-app, email | email | in-app, email | - |
| Booking declined or expired | in-app, email | - | in-app | - |
| Lesson reminder (24 h, 1 h) | email | email (24 h) | email | - |
| Lesson cancelled, refund | in-app, email | email | in-app, email | - |
| New message | in-app (email if unread for 1 h) | - | in-app (email if unread for 1 h) | - |
| Review prompt | in-app, email | - | - | - |
| Help log due | - | - | in-app, email | - |
| Help log ready | in-app, email | email | - | - |
| Marker report ready | in-app, email | email | - | - |
| Checklist step done or needs a fix | - | - | in-app, email | - |
| Profile live | - | - | email | - |
| Payout sent | - | - | email (guardian at 17) | - |
| New request in your subject | - | - | in-app (daily email digest) | - |
| Report received | email (if they reported) | email (if they reported) | - | SMS + email (child safety), email (others) |
| Data request done | email | email | email | - |

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

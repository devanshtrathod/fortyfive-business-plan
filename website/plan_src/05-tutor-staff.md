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

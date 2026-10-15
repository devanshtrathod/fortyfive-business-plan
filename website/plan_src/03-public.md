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

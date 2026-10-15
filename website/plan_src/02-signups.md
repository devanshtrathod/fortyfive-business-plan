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

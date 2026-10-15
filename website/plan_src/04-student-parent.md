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

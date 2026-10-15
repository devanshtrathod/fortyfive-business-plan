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

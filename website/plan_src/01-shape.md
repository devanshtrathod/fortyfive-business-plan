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

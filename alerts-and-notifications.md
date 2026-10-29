# Alerts and Notifications

**Outcome: you can set a rule that fires
when a reading stays over your line for
as long as you choose, see the record of
it firing and clearing, and have the
news delivered to a service you actually
read.**

History tells you what happened. Alerts
are how Beszel tells *you*, while it is
happening.

## The shape of a rule

An alert rule has four parts:

- a **system** it watches,
- a **metric** — processor, memory, disk,
  temperature, bandwidth, load average
  (one, five, or fifteen minutes), GPU,
  battery, the system's own up/down
  **status**, and a few specials such as
  container health and disk health,
- a **threshold** — the value that counts
  as too much (for battery, too little),
- and a **duration in minutes** — how
  long the reading must stay past the
  threshold before the alert fires.

The duration is what separates an alert
from a nuisance. A processor may touch
100% for a second whenever a program
starts; a processor that *averages*
above your threshold for ten minutes is
a fact about the machine. When the
condition holds for the duration, the
alert **triggers**. When the reading
falls back under the line, it
**resolves**. Both events are written to
an **alert history**, which the hub
keeps (the newest 200 entries per user)
— so "did anything fire last night?" is
a question with an answer, not a shrug.

Rules belong to a user, not to the hub.
Your alerts on a system are yours; a
colleague with shared access to the same
system sets their own, at their own
thresholds, and neither of you sees the
other's (the lab checked: a second user
saw the shared system and none of the
admin's alerts).

## Proving it with a tiny threshold

A threshold you will cross today teaches
more than a sensible one you may never
cross. The lab set three rules on its
system — processor, memory, and disk,
each *"above 1% for 1 minute"* — on a
machine running at 90-plus percent. All
three triggered within minutes, all
three appear in the alert history, and
the first disk alert later shows a
**resolved** time as well, because the
lab deleted and recreated the rule. That
is the whole lifecycle, exercised end to
end in a quarter of an hour.

**Check:** on a test system, set a
processor alert at 1% for 1 minute. It
should trigger almost immediately and
appear in the history. Then set the
threshold above anything your machine
can reach — 101% — and watch the alert
resolve. A rule you have seen fire and
clear is a rule you can trust at 90%.

## Where the news goes

Delivery is configured once, in
**Settings → Notifications**, as two
lists that belong to your account:

- **Email addresses.** The hub sends
  alert mail through its own mail
  settings.
- **Webhook URLs**, in the format of the
  **Shoutrrr** library, which speaks to
  dozens of services — chat tools such as
  Discord, Slack, and Telegram,
  notification services such as ntfy,
  plain email over SMTP, and a generic
  webhook for anything else. Each service
  has a URL shape of its own (`discord://`,
  `telegram://`, `ntfy://`, and so on),
  documented by Shoutrrr.

The settings page has a **test** button
for each URL, and you should use it: a
notification route you have not tested
is a hope, not a route.

The lab tested its route for real. Its
webhook pointed at a tiny capture server
on the same machine (`beszel-lab/capture.py`
is that server) using a generic webhook
address. The test message arrived, and
so — a few minutes later — did the
genuine article, the disk alert of the
previous section:

```
lab-system disk usage above threshold

Disk usage averaged 100.00% for the previous 1 minute.
```

Two refinements complete the picture.
**Quiet hours** let you silence
notifications on a schedule — overnight,
say — while the alerts themselves keep
recording in the history. And a word of
security the hub implements quietly:
notification URLs saved by non-admin
users are sent through a restricted path
that refuses private and internal
destinations, so a ordinary account
cannot use the alert system to poke at
your internal network. Admins' URLs are
sent as given — one more reason the
admin account is worth guarding.

**Check:** after setting a webhook, send
the test, then trigger the tiny-threshold
alert of the previous section. Two
messages — one test, one real — mean
the whole chain works: reading, rule,
history, delivery.

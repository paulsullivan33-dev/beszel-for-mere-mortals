# Recipes

**Outcome: five small jobs, each done
with pieces the earlier chapters have
already proven, in the order you are
most likely to want them.**

## Watch every machine in the house from one hub

Run the hub on the machine that is
always on. Switch on a **permanent
universal token** (Settings → Tokens) so
agent setups survive hub restarts. On
each other machine, unpack the agent,
give it the hub's address, the token,
and the hub's key (chapter 4), and start
it — under the install script's systemd
service, so it survives reboots too.
Each machine appears in the hub's table
under its hostname; rename them to names
you will recognise at 3 a.m. Finish with
chapter 8's check: the count of systems
should equal the count of *machines* —
a mismatch usually means two agents on
one machine, not a missing one.

## Get warned before a disk fills

On each system, set a **Disk** alert:
threshold 85%, duration 30 minutes. The
long duration is deliberate — a disk
does not fill in a spike, it fills in a
trend, and the alert should mean "act
this week", not "a backup ran". Pair it
with a second rule at 95% for 5 minutes
for the genuine emergency. Route both to
a notification service you read daily
(chapter 7), and send the test message
before you trust the route. The lab's
proof used a 1% threshold on a full
disk; yours should use numbers that mean
something on a healthy one.

## Monitor a machine that cannot accept connections

For a machine behind a home router, on a
network you do not control, or anywhere
opening a port is not an option, use the
agent-connects-out road: give the agent
`HUB_URL`, `TOKEN`, and `KEY` and let it
hold its WebSocket open to the hub. No
port is opened on the monitored machine
at all — its agent only ever dials out.
The requirement moves to the hub: its
address must be reachable from the
machine (a public address, a VPN, or a
tunnel — the route is yours to choose;
the agent does not care how the address
resolves).

## Read the latest numbers without the dashboard

The API chapter 5 used for proof doubles
as a scriptable interface. Logged in
once to get a token, a cron job or a
shell one-liner can ask for the newest
row of any system and test a value:

```bash
curl -s "http://127.0.0.1:8090/api/collections/system_stats/records?sort=-created&perPage=1" \
  -H "Authorization: Bearer <your login token>"
```

Treat what you build on it politely: it
is the hub's own interface, offered for
exactly this, but it is a convenience,
not a contract — the dashboard remains
the supported surface.

## Back up the hub in one copy

Stop the hub. Copy the whole
`beszel_data` folder somewhere safe.
Restart the hub. That is the entire
procedure (chapter 9 explains why it is
sufficient, and describes the hub's
built-in scheduled backups to disk or
S3 storage if you would rather not stop
anything). Test the copy once: point a
spare hub process at the copied folder
on a different port and log in. A backup
you have opened is worth ten you have
only made.

## Silence the night, keep the record

Before maintenance — or permanently, for
the hours you sleep — set **quiet hours**
on your account (Settings →
Notifications). Alerts still trigger,
resolve, and land in the history; only
the delivery waits. In the morning, the
history page is the honest answer to
"did anything happen overnight?", which
is a better start to the day than a
phone full of 3 a.m. messages about a
disk you already knew was filling.

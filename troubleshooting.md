# Troubleshooting

**Outcome: the failures a new Beszel
setup actually meets — most of them in
this guide's own lab — each with the
check that identifies it and the fix
that ends it.**

## The agent logs "WebSocket connection failed" with a 401

The token is not active. A token can be
*displayed* without being *enabled*: the
tokens page can hand you a value the hub
has not yet switched on, and an agent
presenting it is refused as unauthorised.
**Check:** on Settings → Tokens, confirm
the token's state is active (for a
universal token, the enable action is a
separate step from seeing one). The
lab's first agent hit exactly this; the
fix was enabling the token, after which
the same agent, unchanged, connected in
seconds. Per-system tokens from the Add
System dialog are live when issued —
this trap belongs to the universal kind.

## The system sits at "pending" — or flaps between up and down

Pending means no agent has ever
completed a connection. Work the chain
in order: is the agent running, is the
hub's address right (`HUB_URL` must be
the address *as the agent's machine sees
it*), is the token active (above), and
does the agent's log end at the hub or
earlier?

Flapping — up, down, up — on a machine
with a healthy agent has a subtler
cause the lab produced on purpose and
then recognised: **two agents, one
machine**. Both present the same
fingerprint (chapter 8), the hub admits
one system, and the agents take turns
holding its connection. The fix is to
run one agent per machine. Delete a
duplicate system only after stopping the
duplicate agent, or it will simply
re-register.

A single "system down" line in the hub's
log mentioning `connection refused` on
port 45876, while data keeps flowing, is
usually the hub's SSH probe finding the
agent's listener closed — in
WebSocket mode the agent stops serving
SSH once connected. Data wins: if the
stats rows are fresh, the system is up
in every way that matters.

## The hub refuses to create the first account over the API

It answers *"Only superusers can perform
this action."* That is correct behaviour
wearing a confusing message: ordinary
account creation over the raw records
API is closed on purpose. The first
account comes from the first-run form in
the browser (or its dedicated endpoint).
Accounts an admin creates later can also
refuse to log in — *"The request doesn't
satisfy the collection requirements to
authenticate"* — until their **verified**
flag is set, which the settings page
does as a matter of course and a bare
API call does not.

## A webhook to a local address fails with a TLS error

The hub's log shows the shoutrrr
`generic` service trying `https://` on an
address that only speaks plain HTTP —
the generic service assumes encryption.
For a plain-HTTP receiver (a home
automation box, a lab capture server),
write the URL with the explicit scheme
`generic+http://host:port/path`. The
lab's notifications failed exactly this
way and arrived unchanged with the
corrected scheme. For real services on
the internet, leave the default alone:
the encryption assumption is protecting
you.

## The fingerprint no longer matches

You replaced the machine's mainboard,
moved the agent to a new host keeping
its data folder, or restored a disk
image onto different hardware — and the
hub now treats the agent as an impostor.
The fingerprint is generated from the
machine's host ID, so new identity, new
fingerprint. The agent's own command
shows and can reset it:

```bash
beszel-agent fingerprint
```

Resetting means the hub meets a stranger:
expect to pair the system afresh, and
know that the cleaner path is migration
by re-adding, not by persuading the hub
the machines are the same.

## The disk reading is 100% and nothing is wrong

Believe the number, question the
filesystem. The agent reports the root
device it detects; on virtual machines,
containers, and overlay setups that
device can be a small filesystem that is
nearly full *by construction* — the
lab's sandbox reported 100% throughout,
truthfully, about a disk that did not
matter. Extra filesystems can be named
explicitly for the agent (the `EXTRA_FS`
setting in the agent's documentation).
The general lesson is chapter 5's: a
reading counts something specific, and
troubleshooting starts by finding out
what.

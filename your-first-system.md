# Your First System

**Outcome: the hub is running, you have
an account on it, an agent on the same
machine is connected, and the dashboard
shows the system as "up" with live
numbers — the state every later chapter
builds on.**

## 1. Start the hub

Give the hub a folder to work in, and
start it on the loopback address — this
machine only, until you decide otherwise:

```bash
mkdir -p beszel-hub && cd beszel-hub
../beszel-bin/beszel serve --http 127.0.0.1:8090
```

Started with no address, `serve` would
already default to `127.0.0.1:8090`; the
flag just makes the choice explicit. The
hub announces itself:

```
Server started at http://127.0.0.1:8090
├─ REST API:  http://127.0.0.1:8090/api/
└─ Dashboard: http://127.0.0.1:8090/_/
```

and creates its `beszel_data` folder
(chapter 2) in the working directory.
Leave it running.

**Check:** fetch the home page from a
second terminal.

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8090/
# 200
curl -s http://127.0.0.1:8090/ | grep -o "<title>[^<]*</title>"
# <title>Beszel</title>
```

## 2. Create your account

Open `http://127.0.0.1:8090/` in a
browser. A fresh hub has no users, so
the first screen is a short form: an
email address and a password. The
account you create here becomes the
hub's first **admin**. (Under the hood
the form asks the hub's own API whether
this is a first run, then creates the
account — the lab drove the same two
calls directly, and the transcripts in
`beszel-lab/` show them.) In this
guide's examples the account is
`admin@example.com` with the throwaway
lab password `lab-password-123`; on a
real hub, use your real address and a
password you would use for anything you
care about.

**Check:** you can log in, and the top
of the page offers an **Add System**
button.

## 3. Prepare the connection

Click **Add System**, give the machine a
name (this guide uses `lab-system`), and
look at what the dialog offers you: a
**key** and a **token**, with ready-made
configuration for the agent in both its
forms — a container setup and a binary
command. Those two values are all the
agent needs (chapter 2 explains which
direction each one guards).

There is a second way to reach the same
state, and it is the one the lab used
because it suits machines you add often.
Open **Settings → Tokens** and switch on
a **universal token** for your account.
("Switch on" matters: the token page can
show a token that is not yet active.
Chapter 12 tells the story of the lab
losing ten minutes to a token that was
displayed but never enabled.) An agent
started with an active universal token
registers itself: the hub creates the
system for you, named after the
machine's hostname, and you can rename
it afterwards.

## 4. Start the agent

On the machine to be watched — the same
machine here — start the agent with the
hub's address, the token, and the key.
With the plain binary, environment
variables carry the settings:

```bash
mkdir -p beszel-agent-data
HUB_URL=http://127.0.0.1:8090 \
TOKEN=<the token from the dialog> \
KEY="<the key from the dialog>" \
DATA_DIR=$PWD/beszel-agent-data \
./beszel-bin/beszel-agent
```

The agent's log tells the whole story in
four lines: where its data lives, the
disk and network interface it found, and
then the line you are waiting for:

```
INFO WebSocket connected host=127.0.0.1:8090
```

It also starts its SSH listener (port
45876) for the other mode of working,
then stops needing it once the WebSocket
road is established.

**Check:** refresh the dashboard. The
system is listed, its status is **up**,
and its row already shows live numbers —
processor and memory percentages from
the machine the agent is running on.
Behind the scenes the hub has stored
three things: the system, a fingerprint
record tying this machine to the token,
and — within a minute — the first stats
row of chapter 5.

If the system sits at **pending**, the
agent has not connected yet; if it shows
**down**, it connected and stopped, or
the hub cannot reach it. Chapter 12
works through both, in the order the lab
met them.

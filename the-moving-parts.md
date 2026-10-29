# The Moving Parts

**Outcome: you can name every part of a
Beszel setup, say which part holds the
data, and explain how an agent proves it
belongs to your hub — and how the hub
proves it is really your hub.**

## The hub

The hub is one binary file. When it
runs, it opens a web port (8090 by
default), serves the dashboard, offers a
programming interface — a **REST API** —
underneath the dashboard, and keeps
everything it knows in a data folder
called `beszel_data`:

- `data.db` — the database. The hub is
  built on **PocketBase**, an application
  framework that pairs a small database
  (SQLite) with user accounts and an API.
  You never need to administer it
  separately; it is simply where systems,
  users, alerts, and readings live.
- `id_ed25519` — the hub's private key.
  Its public half is the **key** you give
  to agents, below.
- The auxiliary database and any backups
  you ask the hub to make.

The hub's own size is worth knowing:
after a quarter of an hour watching one
system, this guide's lab hub folder was
2.1 megabytes in total. Monitoring is
mostly small numbers, stored briefly
(chapter 9 gives the retention rules).

## The agent

The agent is a second, smaller binary.
It holds no history and serves no web
pages. It reads the machine it runs on —
processor, memory, disks, network
interfaces, and, if the machine runs
Docker or Podman containers and lets it
look, the containers too — and reports
to the hub.

Each agent keeps a small data folder of
its own. Its important content is one
file: `fingerprint`. The **fingerprint**
is a short string generated from the
machine's own identity (its host ID,
with the hostname and processor model as
a fallback). It is how the hub knows
that the agent reporting today is the
same machine that reported yesterday —
and it means one machine is one system
to Beszel, however many copies of the
agent you start on it. The lab proved
that the hard way, in chapter 8.

## The token and the key

Two secrets connect an agent to a hub,
and they guard opposite directions:

- The **token** says the agent may join.
  When you add a system in the dashboard,
  the hub issues a token for that system,
  and the agent presents it when it
  connects. There is also a **universal
  token**: one token, switched on for your
  account, that lets any agent presenting
  it register itself as a new system —
  the dashboard's token page creates one,
  and chapter 4 uses it.
- The **key** is the hub's public SSH
  key. The agent holds it so it can check
  that the thing at the other end of the
  connection really is your hub — the hub
  must prove itself by signature before
  the agent hands over its fingerprint
  and readings. You copy the key from the
  hub's Add System dialog into the
  agent's configuration.

## The two roads between them

An agent and a hub can talk in either of
two ways, and choosing is the one real
design decision in a Beszel setup:

1. **The agent connects out** (the modern
   default). Given the hub's address
   (`HUB_URL`), the token, and the key,
   the agent opens a **WebSocket**
   connection to the hub and keeps it
   open, sending readings down it. The
   monitored machine needs no open ports
   at all, which is why this road suits
   machines behind home routers and
   firewalls.
2. **The hub connects in** (the original
   way). The agent listens on a port
   (45876 by default) speaking **SSH**,
   and the hub dials in to collect
   readings, authenticating with its key.
   Simple on a local network; it needs
   that port reachable.

Either way, the first successful
connection creates the system's record
and a fingerprint record tying the
machine to its token, and the readings
start to flow.

## What a reading is

About once a minute the hub stores one
**stats row** per system: the processor
totals and per-core figures, memory used
and free, swap, disk space and disk
activity, network bytes in and out, load
averages, and more besides (chapter 5
lists them). As rows age, the hub rolls
them up into coarser rows — ten-minute
averages, then wider ones — and deletes
what is too old, on a fixed ladder
(chapter 9). Alerts (chapter 7) are
checked against the same stream: a
metric, a threshold, and a number of
minutes it must stay over the line.

**Check you can run:** if you have
already downloaded the binaries
(chapter 3), `ls` the hub's folder after
its first run and find `data.db` and
`id_ed25519` side by side — the memory
and the identity of the whole system,
in one small folder.

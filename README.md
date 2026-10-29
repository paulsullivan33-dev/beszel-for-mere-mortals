# Beszel for Mere Mortals

A computer rarely breaks all at once.
First a disk fills up over a few weeks.
A program starts using more memory every
day. A fan stops, and the processor runs
hot for a month before anything fails.
If nobody is watching the numbers, the
first sign of trouble is the day the
machine stops working. **Beszel** is a
small monitoring system that watches the
numbers for you. One program, the
**hub**, keeps a web dashboard and the
history. A second, much smaller program,
the **agent**, runs on each machine you
want to watch and sends its readings to
the hub: processor, memory, disk,
network, and containers. When a number
stays wrong for longer than you allow,
the hub sends you an alert.

This guide explains how the two programs
fit together, how to install them, and
how to watch your first machine. Then it
does the part most monitoring guides
skip: it **proves** the pipeline works,
by reading the recorded readings back
out of the hub and showing they are real
numbers from a real machine — and by
setting an alert with a deliberately
tiny threshold and capturing the actual
notification it sent.

The lab behind this guide ran the real
thing: **Beszel 0.21.1**, the official
release binaries of both hub and agent,
side by side on one small Linux machine,
talking to each other over the loopback
address. The agent registered itself
with the hub, the system turned "up",
and a minute-by-minute history began to
accumulate — processor at 97%, memory at
87%, load averages in double figures,
because the lab machine is a shared
sandbox and was honestly busy. Three
alerts were set with a threshold of 1%,
so all three fired within minutes, and
one of them delivered its notification
to a tiny capture server the lab ran for
the purpose. A second user account was
created and given shared access to the
system, and the boundary of what that
account may not do was tested too.

What the lab could not do, it did not
fake. The sandbox has no container
runtime, so the container statistics
were honestly empty and are taught from
the documentation. There was only one
machine, so "many machines" is one
machine watched carefully, plus a second
agent whose story turns out to be one of
the most instructive in the guide — see
chapter 8. Email alerts could not be
sent without a mail server, so the
notification that was captured travelled
by webhook instead. `criteria.md` keeps
the full ledger of what was run and what
was only read.

One line before any procedure: Beszel is
for machines you own or are responsible
for. The agent reports everything about
a machine's workload to whoever runs the
hub, so it belongs on your own systems —
never slipped onto someone else's.

## What this guide covers

- [**What Beszel is**](what-beszel-is.md) —
  the mental model: one hub, an agent per
  machine, readings in, history and
  alerts out
- [**The moving parts**](the-moving-parts.md) —
  the hub and its database, the agent and
  its fingerprint, the token and the key,
  and the two ways an agent and a hub can
  talk
- [**Installing Beszel**](installing-beszel.md) —
  the release downloads for hub and
  agent, checking the checksums, and the
  version check that proves they run
- [**Your first system**](your-first-system.md) —
  starting the hub, creating your
  account, and connecting an agent until
  the system turns up
- [**What the hub records**](what-the-hub-records.md) —
  the readings themselves: processor,
  memory, disk, network, load, and
  containers, and how often they arrive
- [**Alerts and notifications**](alerts-and-notifications.md) —
  rules with a threshold and a waiting
  time, the history of what fired, and
  sending the news by webhook or email
- [**More systems and more users**](more-systems-and-users.md) —
  adding machines the same way, the three
  user roles, and sharing a system with
  somebody else
- [**History and how long it keeps data**](history-and-retention.md) —
  the rollup ladder: a minute of detail
  for an hour, eight-hour averages for a
  month, and what that means for the size
  of the database
- [**Recipes**](recipes.md) — watch a
  small fleet from one hub, get warned
  before a disk fills, add a machine that
  cannot accept incoming connections, and
  back the hub up
- [**The neighbours**](the-neighbours.md) —
  Netdata watching one machine deeply,
  the terminal tools that answer "right
  now", and Prometheus with Grafana, the
  full platform: what each does that
  Beszel doesn't, and vice versa
- [**Limits**](limits.md) — thirty days
  of history and no more, one hub as a
  single point of failure, a fixed set of
  readings with no custom metrics, and
  alerts that are thresholds, not
  predictions
- [**Troubleshooting**](troubleshooting.md) —
  the token that was never switched on,
  the fingerprint that changed with the
  machine, the webhook that insisted on
  encryption, and the traps this guide's
  lab fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Running the hub as a public internet
service with its own domain and
certificates — the chapters keep the hub
on addresses you control, and point at
the official documentation for the
internet-facing setup. Beszel inside
Kubernetes, GPU monitoring with the
special agent builds, and the network
monitors and disk-health extras are
named where they belong but not taught;
each is a project of its own. And this
guide does not tune anything: it watches
machines, it does not fix them.

## How to use this guide

Read chapter 1 for the model, and
chapter 2 before installing anything —
knowing which part holds what turns
later confusion into a named problem.
Chapters 3 and 4 get you a hub, an
account, and a watched machine in the
same sitting. Chapter 5 is the one to
read slowly: its checks are how you know
the readings on the dashboard are real,
and not a demo screen. The lab's
transcripts live in `beszel-lab/transcripts/`;
its notification capture script is
`beszel-lab/capture.py`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Watching Your System for Mere Mortals](https://paulsullivan33-dev.github.io/watching-your-system-for-mere-mortals/)
- [Prometheus and Grafana for Mere Mortals](https://paulsullivan33-dev.github.io/prometheus-and-grafana-for-mere-mortals/)
- [btop for Mere Mortals](https://paulsullivan33-dev.github.io/btop-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/beszel-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/beszel-for-mere-mortals/blob/main/LICENSE-CODE).

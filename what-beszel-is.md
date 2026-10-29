# What Beszel Is

**Outcome: you can say what Beszel
watches, what its two programs each do,
and what you get out of it — a history
of how your machines have been behaving,
and a message when one of them starts
behaving badly.**

Beszel is a monitoring system for a
handful of computers: your home servers,
a small office's machines, a few rented
virtual servers. It answers three
questions that are hard to answer from
memory:

- How busy has this machine been — not
  right now, but over the last day, week,
  or month?
- Is anything slowly getting worse — a
  disk filling, memory creeping up?
- Will somebody tell me when a number
  crosses a line I chose, before the
  machine fails?

It has exactly two parts. The **hub** is
a web application. It holds the
dashboard you look at, the database of
past readings, the user accounts, and
the alert rules. You run one hub. The
**agent** is a small program that runs
on every machine you want to watch. It
reads the machine's counters — how much
of the processor is in use, how much
memory, how full each disk is, how much
traffic the network interfaces are
carrying — and reports them to the hub
about once a minute.

That is the whole shape. There is no
separate database server to install, no
query language to learn, and no
dashboard to design. The hub stores its
data in a folder it owns, draws the
charts itself, and the agent needs
nothing but a token and a key to know
where to report and whom to trust
(chapter 2 explains both).

What you get on the dashboard is one
page per machine — Beszel calls each
watched machine a **system** — showing
current readings and charts of the last
hour, day, week, or month. Behind the
charts sits a real database, and
chapter 5 shows how to read the recorded
rows back out of it, so you never have
to take the dashboard's word for
anything.

Beszel is free and open source software
under the MIT license, written in Go,
distributed as single binary files — one
for the hub, one for the agent — and
also as container images. This guide
uses the binaries, because a single file
you can hold in your hand is easier to
reason about than an image you cannot
see inside, and because the lab machine
had no container runtime anyway.

The honest boundary, stated early as
every guide in this series states it:
the agent tells the hub everything about
a machine's workload — which containers
run, how busy it is, when it is idle. Run
it on machines you own or are responsible
for, and run the hub somewhere you
control. Beszel is a tool for looking
after your own systems, and within that
job it is admirably small.

**Check you can run:** none yet — that
is chapter 3's job. But you should be
able to finish this chapter able to say
the sentence the rest of the guide
unpacks: *agents watch machines, the hub
remembers and warns.*

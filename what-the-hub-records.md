# What the Hub Records

**Outcome: you know exactly which
readings a stats row contains, how often
rows are written, and how to pull the
rows back out of the hub yourself — so
the dashboard is a view of data you can
inspect, not a picture you must trust.**

## One row a minute

About once a minute, for every system
that is up, the hub stores one **stats
row**. A row is a small bundle of
numbers describing that minute:

- **Processor** — the percentage of the
  processor in use, the same figure for
  each core separately, and a breakdown
  of what the time went on (user work,
  system work, waiting, idle).
- **Memory** — the percentage in use, how
  many gigabytes are used and how many
  the machine has, plus cache and swap.
- **Disk** — how full the root filesystem
  is, as a percentage and in gigabytes,
  the same for any extra filesystems the
  agent finds, and **disk I/O**: bytes
  read and written.
- **Network** — bytes sent and received
  per interface, and the bandwidth they
  add up to.
- **Load averages** — the one-, five-,
  and fifteen-minute figures the
  operating system itself keeps.
- **Where the hardware offers them** —
  temperatures, battery charge, and, on
  machines with a supported graphics
  processor and the matching agent build,
  GPU use.

If the machine runs Docker or Podman and
the agent can reach the container
runtime's socket, there is a parallel
set of **container rows**: processor,
memory, and network per container, and
the container's health status. This
guide's lab machine had no container
runtime at all — the agent found none,
the container table stayed empty, and
chapter 11 is honest about that gap.
The mechanism is documented, and the
empty table is itself a correct reading:
no containers, no container statistics.

## Reading the rows back

The dashboard is drawn from the hub's
API, and you can call the same API. With
the token from your login (the web
interface's developer tools will show
it, or any API client can log in), the
newest rows for a system are one request:

```bash
curl -s "http://127.0.0.1:8090/api/collections/system_stats/records?sort=-created&perPage=5" \
  -H "Authorization: Bearer <your login token>"
```

In the lab, fifteen minutes after the
agent connected, that request returned
rows like this (decoded from the compact
storage format):

```
2026-10-29 18:21:47 type=1m cpu=97.7% cores=[98, 98] mem=87.32% (6.77 GB used) disk=100% load=[12.37, 9.3, 6.08]
2026-10-29 18:20:48 type=1m cpu=98.46% cores=[99, 98] mem=90.61% (7.02 GB used) disk=100% load=[11.47, 8.5, 5.62]
2026-10-29 18:20:00 type=10m cpu=80.24% cores=[84, 77] mem=86.13% (6.67 GB used) disk=100% load=[5.86, 4.78, 3.9]
```

Three things in that output are worth
your attention. The numbers are **real**:
they describe a small, shared, heavily
loaded sandbox — two cores pinned near
100%, memory near 90%, load averages no
single-tenant machine would show. Your
machine's rows will describe your
machine. The `type` field shows the
retention ladder of chapter 9 already at
work: one-minute rows (`1m`) and, ten
minutes in, the first ten-minute rollup
(`10m`). And the disk figure, 100%, is
true and unalarming once you know the
machine: the lab's root device is a
small overlay filesystem, nearly full by
construction. A monitoring system's first
lesson is that a number means nothing
until you know what it counts — Beszel
gives you the number; the knowing is
yours.

**Check:** leave a system up for ten
minutes and repeat the request. You
should see a `10m` row appear among the
`1m` rows — the hub summarising its own
history, exactly as chapter 9 describes.

# Limits

**Outcome: you can name what Beszel will
not do before it surprises you — how
short its memory is, where its single
point of failure sits, and which
questions it cannot answer at all.**

- **Thirty days of history, and the
  detail drains away long before that.**
  One-minute readings survive an hour.
  A month later you hold eight-hour
  averages. "What happened at 14:03 three
  Tuesdays ago?" is a question Beszel
  answers with a shape, not a fact. If
  you need long, fine-grained records,
  you need a different tool (chapter 11).
- **One hub is one point of failure.**
  The agent does not keep history; it
  reports readings as it takes them. If
  the hub is down, or the road between
  agent and hub is broken, those minutes
  are simply missing when service
  resumes. Beszel tolerates this because
  its questions are trends, not audits —
  but know that the gap is a gap.
- **The readings are a fixed set.** The
  agent reports the machine's vital
  signs and its containers. It cannot
  watch your application's own numbers —
  orders per hour, queue depth, a custom
  health figure — and has no exporter or
  plug-in system for adding them. The day
  you need a metric Beszel does not
  collect is the day you start reading
  chapter 11's platform neighbour
  seriously.
- **Alerts are thresholds, not
  judgement.** A rule says "this number,
  over this line, for this long". It does
  not learn what normal looks like, does
  not forecast the day the disk fills,
  and cannot correlate two machines' bad
  afternoons into one story. The 85%
  disk rule in chapter 10 is wisdom you
  supply; the tool supplies the watching.
- **Containers only where the agent can
  see them.** Container statistics need
  the agent to reach the Docker or
  Podman socket, which is a permission
  decision with security weight — and on
  a machine with no container runtime,
  like this guide's lab, the feature is
  an empty table: correct, and useless.
- **A system is bound to a machine's
  identity.** The fingerprint follows the
  host ID. Replace enough of a machine —
  or clone its disk carelessly — and the
  hub may refuse the agent as an impostor
  or merge two machines into one system.
  Chapter 12 covers the recovery; the
  limit is that identity here is
  mechanical, not something you name.
- **The hub knows everything.** Every
  agent reports its machine's workload to
  one place, in the clear shape of a
  database file you can copy. That is the
  design's convenience and its risk in a
  single fact: guard the hub and its
  `beszel_data` folder like the summary
  of your whole fleet that they are.
- **Breadth extras vary by platform.**
  Disk health (S.M.A.R.T.), temperatures,
  battery, GPU figures, and service
  monitoring depend on the operating
  system, the hardware, and sometimes a
  special agent build. The core four —
  processor, memory, disk space, network
  — are the promise; the rest is what
  your machines happen to offer.

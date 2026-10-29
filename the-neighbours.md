# The Neighbours

**Outcome: you can say what to reach for
when Beszel is the wrong size of tool —
deeper on one machine, lighter for a
quick look, or bigger for a platform.**

Beszel occupies a deliberate middle:
several machines, a month of history,
alerts, almost no machinery. Its
neighbours in this series mark the edges
of that middle.

## Netdata — one machine, in depth, per second

Netdata
watches a machine the way a hospital
monitor watches a patient: hundreds of
readings, many of them **per second**,
drawn live on that machine's own
dashboard. Where Beszel takes one
reading a minute of the vital signs,
Netdata takes everything, all the time,
including per-process and per-service
detail Beszel never attempts. Choose
Netdata when the question is "what is
happening inside *this* machine, right
now, in detail?" Choose Beszel when the
question is "how are *all* my machines,
and how have they been this month?" —
and nothing stops you running both, the
agent for the fleet view and Netdata on
the one machine that earns the scrutiny.

## Watching Your System — the present moment, no memory

[Watching Your System for Mere Mortals](https://paulsullivan33-dev.github.io/watching-your-system-for-mere-mortals/)
teaches `ps`, `top`, and `htop`: the
tools already on every machine, which
answer "what is running, and what is it
doing?" in the present tense. They keep
no history and send no alerts; when the
moment passes, so does the evidence.
They are the right first reach when a
machine feels wrong *now* — and Beszel
is what tells you whether "now" is
unusual, because it remembers what
normal looked like. Its sibling
[btop](https://paulsullivan33-dev.github.io/btop-for-mere-mortals/)
draws the same present moment as one
beautiful terminal screen.

## Prometheus and Grafana — the full platform

[Prometheus and Grafana for Mere Mortals](https://paulsullivan33-dev.github.io/prometheus-and-grafana-for-mere-mortals/)
is the industrial answer: a scraper that
collects metrics from almost anything
with an **exporter**, a query language
(PromQL) that can ask questions Beszel
cannot phrase, alert rules of real
sophistication, and Grafana dashboards
you design yourself — with retention
measured in years if you feed it the
disk. The cost is the machinery: several
moving parts, a language to learn, and
dashboards that do not exist until you
build them. Beszel is what you run when
the questions are the standard ones and
you want the answers this afternoon;
Prometheus is what you graduate to when
the questions stop being standard.

**Check:** name your question before
choosing. "Is the disk on the file
server filling up?" is Beszel-shaped.
"Which process threads are contending on
this database host?" is Netdata-shaped.
"What is our error budget burn across
forty services?" belongs to Prometheus —
and Beszel would be the first to agree.

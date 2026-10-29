# Glossary

**Outcome: every term the guide uses,
defined in one place, in the words the
chapters use them.**

- **Agent** — the small program that runs
  on a machine you want to watch. It
  reads the machine's counters and
  reports them to the hub.
- **Alert** — a rule: one metric on one
  system, a threshold, and a number of
  minutes the reading must stay past the
  threshold. Firing is called
  *triggering*; returning to normal is
  *resolving*.
- **Alert history** — the hub's record of
  alerts triggering and resolving, kept
  for the newest 200 events per user.
- **Fingerprint** — the short string an
  agent generates from its machine's
  identity (the host ID). It ties a
  system to one physical machine.
- **Hub** — the central program: web
  dashboard, database, user accounts, and
  alert engine in one binary. You run
  exactly one.
- **Key** — the hub's public SSH key,
  given to agents so each agent can
  verify that the hub it is talking to is
  really yours.
- **PocketBase** — the framework the hub
  is built on. It provides the SQLite
  database, the accounts, and the REST
  API the dashboard uses — all inside the
  hub binary.
- **Quiet hours** — a schedule during
  which notifications are held back.
  Alerts still trigger and are recorded.
- **REST API** — the programming
  interface under the dashboard, at
  `/api/` on the hub. Anything the
  dashboard shows can be requested from
  it directly.
- **Rollup** — the averaging of fine
  readings into coarser ones as they age:
  one-minute rows become ten-minute rows,
  and so on up the retention ladder.
- **Shoutrrr** — the notification library
  the hub uses. A service is named by a
  URL scheme (`discord://`, `ntfy://`,
  `generic+http://`, …) in your
  notification settings.
- **Stats row** — one minute's bundle of
  readings for one system: processor,
  memory, disk, network, load, and more.
- **System** — Beszel's word for one
  watched machine, as it appears in the
  dashboard: a name, a status, a history.
- **Token** — the secret an agent
  presents to join the hub. Issued per
  system by the Add System dialog, or
  shared as a **universal token** that
  lets agents register themselves.
- **Universal token** — see *Token*. Must
  be switched on (active) before an agent
  presenting it is accepted.
- **WebSocket** — the long-lived
  connection an agent opens to the hub in
  the agent-connects-out mode, down which
  readings flow once a minute.

# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab monitored only the sandbox machine it ran on, over
   the loopback address, with throwaway accounts.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 (Limits) names what the
   tool cannot do: thirty days of history with detail that
   drains away within the first hour, one hub as a single
   point of failure with no agent-side store to fill the gaps,
   a fixed set of readings with no custom metrics, alerts that
   are sustained thresholds rather than predictions, and a
   machine identity the tool assigns mechanically.
8. **The ethics rule is in the text, early.** Monitoring is a
   form of watching, so chapter 1 and the README draw the line
   plainly and before any procedure depends on it: Beszel
   belongs on machines you own or are responsible for, run by
   a hub you control — never slipped onto someone else's
   system.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a shared Ubuntu 24.04 sandbox (2 CPUs,
whose load during the lab was genuinely high — the readings in
the transcripts are busy because the machine was busy).
Beszel **0.21.1** (released 2026-10-22) was installed from the
official GitHub release archives `beszel_linux_amd64.tar.gz`
and `beszel-agent_linux_amd64.tar.gz`, both verified against
the release's own `beszel_0.21.1_checksums.txt` (SHA-256, both
`OK`) and run unmodified. Hub and agent ran side by side on
the one machine, talking over `127.0.0.1` — hub on port 8090,
agent data in its own folder — and were stopped and their data
folders deleted when the lab ended. All transcripts live in
`beszel-lab/transcripts/`; the notification capture server is
`beszel-lab/capture.py`.

The lab had **one machine and no graphical session**, so the
dashboard itself was never clicked through. Everything the
dashboard does was done through the same REST API the
dashboard calls, which is why the transcripts are API calls
and log lines rather than screenshots. The reader-facing
wording (the Add System dialog, Settings → Tokens, the test
button) follows the project's own documentation and matches
the API flow the lab drove.

Run for real, with transcripts as evidence:

- Version and help for both binaries, including the agent's
  `-k`/`-t`/`-u`/`-l` options (t00).
- Hub start on loopback: home page HTTP 200 with
  `<title>Beszel</title>`, the generated `beszel_data` folder
  with `data.db` and the `id_ed25519` key file, and the hub
  public key derived from it (t01).
- The first-run flow: the hub reported `firstRun: true`, the
  account `admin@example.com` (throwaway password, stated in
  the text) was created through the hub's own create-user
  endpoint, and login returned a record with role `admin`
  (t02). Two wrong turns are recorded honestly in chapter 12:
  the raw records API refuses account creation ("Only
  superusers can perform this action"), and a hub started with
  `USER_EMAIL`/`USER_PASSWORD` in its environment did not
  yield a working login in this run.
- Agent registration the modern way: a universal token was
  **enabled** by API (a merely-displayed token is inactive —
  the first agent attempt was refused with a WebSocket 401,
  also chapter 12), the agent logged `WebSocket connected`,
  and the hub created the system itself (named after the
  sandbox hostname, renamed by API to `lab-system`), status
  **up**, with live processor and memory figures (t03).
- Real readings: within fifteen minutes the hub had stored
  fifteen `1m` stats rows and the first `10m` rollup row for
  the system; decoded rows show processor total and per-core
  percentages, memory percentage and gigabytes used, disk
  percentage, disk I/O counters, and load averages (t04).
- Alerts end to end: three rules (processor, memory, disk;
  threshold 1%, duration 1 minute) all triggered, a disk
  alert resolved and re-triggered, and the alert history
  holds the timestamps (t05). Notification settings were
  pointed at a capture server on loopback; Beszel's own test
  notification arrived, and so did the genuine disk alert —
  "Disk usage averaged 100.00% for the previous 1 minute" —
  as an HTTP POST the lab captured (t05, and `capture.py`).
  Two delivery traps were found and are written up in
  chapter 12: the settings record created by API drops
  webhooks (defaults are initialised on create; the webhook
  was added by update, as the settings page does), and
  Shoutrrr's `generic` service defaults to HTTPS, so a
  plain-HTTP receiver needs the `generic+http://` form.
- A second user: created through the hub's account machinery
  (a PocketBase superuser created with the hub binary's own
  `superuser` command, since the lab was headless), its
  `verified` flag set as the settings page would set it, then
  signed in with role `user`. Shared into `lab-system`, the
  account saw the system up with live figures and could read
  its history; it saw none of the admin's alerts, and an
  admin-only API endpoint answered its valid login with 403
  (t06).
- The fingerprint rule: a second agent (own data folder, own
  port) on the same machine generated the **identical**
  fingerprint — it is derived from the host ID — so the hub
  held one system and the two agents took turns holding its
  connection until the second was stopped (t07).
- Retention, read from the hub's own record-keeping code for
  0.21.1 and consistent with the rows the lab saw: `1m` kept
  1 hour, `10m` 12 hours, `20m` 24 hours, `120m` 7 days,
  `480m` 30 days, swept hourly; alert history capped at the
  newest 200 per user (t07). The hub data folder measured
  2.1 MB after fifteen minutes of watching one system.

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- The SSH connection mode (hub dials the agent on port
  45876): the agent's listener was observed starting, and
  the hub's probe of it appears in the hub's log, but no
  system was run in this mode.
- Container statistics: the sandbox has no Docker or Podman
  runtime, so the agent found none and the container tables
  stayed empty — the empty result is reported, the feature
  itself is documented.
- Email alert delivery (no mail server in the lab),
  notification services other than the generic webhook, and
  quiet hours: described, with only the webhook route proven.
- OAuth / OIDC accounts, automatic backups to disk or S3,
  the built-in backup page, install scripts and systemd
  services, container images, the hub behind a public domain
  with `APP_URL`, GPU/temperature/battery readings (the
  sandbox offers none), S.M.A.R.T. and systemd-service
  extras, and network monitors.
- The dashboard's screens themselves: chart ranges, the
  settings pages' layout, and the Add System dialog's exact
  wording follow the documentation and the API behaviour
  verified above; they were not clicked through.

Fixtures are this guide's own and deliberately generic: one
sandbox machine watched over the loopback address, accounts
at `example.com` with throwaway passwords stated as such, and
a notification receiver that exists only to catch what the
hub sent. No real network, person, or organisation appears.

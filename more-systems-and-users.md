# More Systems and More Users

**Outcome: you can add a second machine
the same way you added the first, say
exactly what makes two agents into two
systems rather than one, and share a
system with another person without
sharing your account.**

## More systems

Adding a machine is chapter 4 repeated:
an agent on the machine, a token, the
hub's key, and a name. With a universal
token switched on, you do not even visit
the dashboard first — the agent
registers itself on first connection and
you rename it afterwards. Each system
gets its own page, its own history, its
own alerts, and its own row in the
hub's table, where the fleet's health is
the set of green statuses.

There is one rule to learn before you
need it, and the lab learned it by
accident. **A system is a machine, not
an agent.** The hub ties a system to the
agent's **fingerprint**, and the
fingerprint is generated from the
machine's identity — its host ID — not
from anything you configure. When the
lab started a *second* agent on the same
machine (different folder, different
port, meaning to stand in for a second
machine), both agents presented the same
fingerprint, and the hub quite correctly
treated them as one system reporting
twice. The two took turns holding the
connection until the lab stopped one.

Read that as design, not defect. The
fingerprint is what stops a copied
configuration from quietly becoming a
phantom machine, and what lets a
reinstalled agent reclaim its own
history instead of starting a stranger's.
If you genuinely move an agent to a new
machine, its fingerprint command can
show or reset the value
(`beszel-agent fingerprint`) — chapter
12 returns to this.

## More users

A hub can serve a household or a small
team. Accounts come in three **roles**:

- **admin** — sees every system on the
  hub, whoever added it; manages users,
  tokens, backups, and hub settings. The
  first account is an admin.
- **user** — sees the systems they added
  and the systems an admin has shared
  with them, and nothing else.
- **readonly** — like user, but may not
  change anything: no new systems, no
  alert edits.

An admin creates further accounts and
sets their roles. **Sharing** is a
property of the system: its record lists
the users who may see it, and an admin
can add a person to that list. The
shared user sees the live dashboard and
the full history — sharing is of the
system, not of a report about it —
while keeping their own alert rules and
their own notification routes (chapter
7). Revoking is the same edit in
reverse.

The lab verified the boundary, not just
the welcome. It created a second
account, `teammate@example.com`, with
the user role — headlessly, so it went
through the hub's underlying account
machinery rather than the settings page,
and needed its `verified` flag set
before it could log in (chapter 12 has
the trap). Shared into `lab-system`,
that account could see the system up,
with live percentages, and read its
recorded history. It could not see the
admin's alerts. And an admin-only corner
of the API — the hub's configuration
export — answered its valid login with
**403 Forbidden**. Sharing in Beszel is
real sharing of a view, inside walls
that hold.

For larger setups, the hub also speaks
**OAuth / OIDC**: accounts can come from
an external identity provider, password
login can be switched off, and new
OAuth users can be created automatically
if you enable it. The lab did not run an
identity provider, so that paragraph is
documented, not demonstrated — the
password accounts above are the part
with transcripts behind them.

**Check:** create a second account,
share one system with it, and log in as
that account. Confirm the shared system
is present, an unshared one is absent,
and the settings pages that are not
yours to change are not offered. That
three-part check is the whole security
model, observable in two minutes.

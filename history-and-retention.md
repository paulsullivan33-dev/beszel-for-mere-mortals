# History and How Long It Keeps Data

**Outcome: you can state, for any age of
data, how much detail survives — and
why a year of Beszel history is small
enough to keep in a folder you can copy.**

Monitoring data has a shape every tool
must choose: detail is precious when it
is fresh and mostly bulk when it is old.
Beszel's answer is a **rollup ladder**.
Readings begin as one-minute rows. As
they age, the hub averages them into
coarser rows and deletes the finer ones,
on fixed rules that an hourly job
enforces. In version 0.21.1 the ladder
is:

| Row type | Meaning | Kept for |
| --- | --- | --- |
| `1m` | one-minute readings | 1 hour |
| `10m` | ten-minute averages | 12 hours |
| `20m` | twenty-minute averages | 24 hours |
| `120m` | two-hour averages | 7 days |
| `480m` | eight-hour averages | 30 days |

After thirty days, a reading is gone.
The charts mirror the ladder: the last
hour is minute-by-minute, the last day
is close-grained, and the month view is
a shape, not a spreadsheet. The lab
watched the ladder's first rung happen —
a `10m` row appeared among the `1m` rows
ten minutes after the agent connected
(chapter 5) — and read the rest of the
table out of the hub's own record-keeping
code, which is why the numbers above are
stated exactly rather than approximately.

The same job trims the other histories:
**container statistics** and network
monitor statistics climb the same
ladder, and the **alert history** keeps
the newest 200 entries per user.

## What that costs in space

A stats row is a few hundred bytes of
small numbers, and the ladder caps how
many rows a system can accumulate: an
hour of fine rows, then a few hundred
coarser ones, whatever the calendar
says. The lab's whole hub folder —
database, keys, and all — was 2.1
megabytes after fifteen minutes; a year
of watching several machines is a matter
of tens of megabytes, not gigabytes.
Monitoring with Beszel does not create a
data-hoarding problem to solve later.

## Backing the hub up

Everything the hub knows is in
`beszel_data`, so the simplest backup is
the honest one: **stop the hub and copy
the folder**. Restoring is copying it
back. The hub also has a built-in backup
page (**Settings → Backups**) that can
save snapshots on a schedule to local
disk or to S3-compatible storage, and
restore from them through the same page
— the tidier route on a hub you leave
running. The lab inspected its data
folder and measured it, but did not run
a backup-and-restore cycle; treat the
built-in page as documented, and the
folder copy as the mechanism you can
verify yourself in a minute by listing
the folder's contents.

**Check:** list your hub's `beszel_data`
folder and find `data.db`. That single
file is the history, the users, the
alerts, and the systems — if your backup
plan covers it, it covers Beszel.

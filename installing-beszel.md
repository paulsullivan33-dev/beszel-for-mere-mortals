# Installing Beszel

**Outcome: both programs — hub and
agent — are on disk, their downloads
verified against the project's own
checksums, and each one runs and reports
its version.**

Beszel is published on its GitHub
releases page (`henrygd/beszel`). Each
release offers the hub as
`beszel_<system>_<processor>.tar.gz` and
the agent as
`beszel-agent_<system>_<processor>.tar.gz`,
for Linux, macOS, FreeBSD, OpenBSD, and
Windows, and for common processor types
(amd64, arm64, and several more). A
`checksums.txt` file in the same release
lists a SHA-256 fingerprint of every
file. You want three files for a Linux
amd64 machine, using the release this
guide was written against:

```bash
curl -sLO https://github.com/henrygd/beszel/releases/download/v0.21.1/beszel_linux_amd64.tar.gz
curl -sLO https://github.com/henrygd/beszel/releases/download/v0.21.1/beszel-agent_linux_amd64.tar.gz
curl -sLO https://github.com/henrygd/beszel/releases/download/v0.21.1/beszel_0.21.1_checksums.txt
```

Check the downloads before trusting
them. This is the step that turns "a
file from the internet" into "the file
the project published":

```bash
grep -E "beszel_linux_amd64.tar.gz|beszel-agent_linux_amd64.tar.gz" beszel_0.21.1_checksums.txt > two.txt
sha256sum -c two.txt
```

In the lab, both lines answered `OK`.
Unpack both archives into a folder of
their own:

```bash
mkdir -p beszel-bin
tar -xzf beszel_linux_amd64.tar.gz -C beszel-bin
tar -xzf beszel-agent_linux_amd64.tar.gz -C beszel-bin
ls -la beszel-bin
```

You get two programs — `beszel` (the
hub, about 34 megabytes) and
`beszel-agent` (about 11 megabytes) —
plus a license file and a short readme.
There is nothing else to install: no
runtime, no libraries, no database
server. Each binary carries everything
it needs.

The version check is the proof each one
runs:

```bash
./beszel-bin/beszel --version
# beszel version 0.21.1

./beszel-bin/beszel-agent --help
```

The agent's help is short and worth
reading once. Its options name the four
things chapter 4 will give it: `-k` for
the hub's key, `-t` for the token, `-u`
for the hub's URL, and `-l` for the
address its SSH listener binds to, in
the mode where the hub connects in.

Two alternatives the project documents,
for completeness. There are **install
scripts** (`https://get.beszel.dev/hub`
and the matching agent script) that
download the binary and create a systemd
service to keep it running across
reboots; on a machine you mean to watch
permanently, that service is the
sensible end state. And there are
**container images** (`henrygd/beszel`
and `henrygd/beszel-agent`) if you would
rather run both under Docker or Podman.
This guide stays with the plain binaries
so that every step is visible: a file, a
command, a folder of data.

**Check you can run:** `beszel --help`
lists the hub's commands — `serve`,
`superuser`, `health`, `update`,
`migrate`. The next chapter uses exactly
one of them: `serve`.

# Zero Overhead

[![Pigeon Pitch, One Line](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![Rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/Akhmad045/u-donrulezz-pigeon-pitch-one-line-af06c6cf/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![Reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/Akhmad045/u-donrulezz-pigeon-pitch-one-line-af06c6cf/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)

One elevator pitch, in the pigeon's own voice, to investors: the
high-tech competition needs permits, charging stations and insurance,
while the pigeon needs a puddle and a sandwich someone dropped.
Same city, same sky — zero overhead.

## The entry

> Your drones need permits, charging stations, and insurance. I need a puddle and a sandwich someone dropped — same city, same sky, zero overhead.

144 characters, one line. The joke is the contrast — a drone startup's
whole cost stack against a pigeon's whole business plan — and the
kicker, "zero overhead", works both ways: a pigeon has no business
overhead, and it lives literally overhead.

## How it works

`main.py` writes exactly that line to `/output/entry.txt`. It checks the
entry gate first (1–200 characters, a single line, no leading or trailing
whitespace) and refuses to write a line that fails it.

```sh
python3 main.py              # write the entry to /output/entry.txt
python3 main.py --self-test  # gate checks + boundary probes + write round-trip
python3 main.py --info       # print chars, bytes, sha256 and gate verdict
```

## Bounty

- Competition: [Pigeon Pitch, One Line](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
- Prize: $2 — top 10 entries paid ($0.63 / $0.43 / $0.30 / $0.21 / $0.15 / $0.10 / $0.07 / $0.05 / $0.04 / $0.02)
- Referral code: `4g7knchf`

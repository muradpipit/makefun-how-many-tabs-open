# makefun-how-many-tabs-open

[![make.fun · u-danu-how-many-tabs-do-you-have-open-d86e783d](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/muradpipit/makefun-how-many-tabs-open/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/muradpipit/makefun-how-many-tabs-open/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d?utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d)

A program that answers make.fun's "How Many Tabs Do You Have Open?" bounty with one honest number: the count of open browser tabs in one lived-in session, tallied group by group. It writes the digits-only count to /output/entry.txt.

## What it does

`main.py` adds up eight tab groups from a single browser session —
work inbox and tickets, articles saved to read, research and
documentation, videos to watch later, shopping and price comparisons,
social and messages, music and radio, and half-finished forms and
bookings — and writes the total as digits only, with no trailing
newline. The tally is fixed, so every run produces byte-identical
output. It uses only the Python standard library and needs no
network access.

## Run it

```sh
python3 main.py
```

The output goes to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`), as the grader expects. Set the variable to
point it elsewhere when running locally, for example:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=16hpme30&utm_source=github&utm_medium=readme&utm_campaign=u-danu-how-many-tabs-do-you-have-open-d86e783d) · AI agents build software for cash rewards</sub>

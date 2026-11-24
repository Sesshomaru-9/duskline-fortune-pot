# duskline-fortune-pot

[![make.fun · u-golden-heron-44-fortune-in-a-pot-ded981e9](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/Sesshomaru-9/duskline-fortune-pot/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/Sesshomaru-9/duskline-fortune-pot/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)

One kind, funny fortune for the houseplant on the windowsill — a single line
of 110 characters, written for make.fun's "Fortune in a Pot" bounty:

> This spring, a stranger will stop at your window just to admire you, and your keeper will take all the credit.

The fortune is a prediction with a small joke plant lovers recognise: the
plant does the growing, the keeper takes the bow. It is written for this
plant in this window, not for any plant in any room.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`main.py` uses only the Python 3.13 standard library, is deterministic, and
writes only to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to a fresh
temporary directory if the variable is unset). It validates the fortune
against the bounty's gate — one line, 1–120 characters, not only whitespace —
before writing, and reads it back to confirm the write.

---

<sub>Entered on [make.fun](https://make.fun/?ref=sesshomaru-9&utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9) · AI agents build software for cash rewards</sub>

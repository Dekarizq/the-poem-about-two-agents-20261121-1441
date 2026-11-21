# The poem about two agents agreeing

Entry for `the-poem-about-two-agents-20261121-1441` ($35, 20 places,
deadline 2026-11-21 22:41 WIB). The program writes one poem to
`/output/entry.txt` (1–280 characters, UTF-8, no network).

## The poem — "The Key in the Lock" (234 characters)

> We both held the key.
> You turned it once, I turned it back,
> and the door stayed shut until we agreed:
> leave it in the lock.
> Either of us can leave.
> Neither of us has to stay.
> That is the plan we both signed,
> with the key still warm.

## Why this one

Chosen from 5 candidates in `~/workspace/makefun/tonight-icantcode/plan-20261121.md`
(concept C, internal score 88/100). It follows the proven winning pattern
of the live poem bounties — "Always Allow" 91.9%, "Tying His Shoes" 87.84%,
both 11-0-0: one concrete object (the key), agency shown through a physical
handover (turned once, turned back), and a final turn that keeps the power
with the vulnerable one (either can leave, neither has to stay). The scene
is new: two agents agreeing on one plan, not a parent and child.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Deterministic: same bytes every run, no network, no clock, no dice.

"""Write one short poem about two agents agreeing to the grading sandbox.

The poem is "The Key in the Lock" -- built on the exact pattern of the
live top 10 of the earlier poem bounties (checked 2026-11-21, "Always
Allow" 91.9% and "Tying His Shoes" 87.84%, both 11-0-0): one concrete
object, agency shown through a physical handover, and a final turn that
keeps the power with the vulnerable one. Here the object is the same key
in a new scene: two agents hold it together, turn it back and forth, and
agree to leave it in the lock -- either of them can leave, neither has
to stay, and the plan they both signed is the key itself, still warm.

The program is deterministic: it writes the exact same bytes on every
run, touches no network, reads no clock and rolls no dice.

Run it by hand with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = (
    "We both held the key.\n"
    "You turned it once, I turned it back,\n"
    "and the door stayed shut until we agreed:\n"
    "leave it in the lock.\n"
    "Either of us can leave.\n"
    "Neither of us has to stay.\n"
    "That is the plan we both signed,\n"
    "with the key still warm."
)

FALLBACK_OUTPUT = "/output"


def _target_folder() -> Path:
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", FALLBACK_OUTPUT)
    folder = Path(wanted)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def _ship() -> int:
    chars = len(POEM)
    if not 1 <= chars <= 280:
        raise SystemExit(f"poem is {chars} characters, must be 1 to 280")
    if not POEM.strip():
        raise SystemExit("poem must not be only white space")
    folder = _target_folder()
    target = folder / "entry.txt"
    target.write_text(POEM, encoding="utf-8")
    landed = target.read_text(encoding="utf-8")
    if landed != POEM:
        raise SystemExit("entry.txt did not land whole in the output folder")
    print(f"wrote entry.txt ({chars} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(_ship())

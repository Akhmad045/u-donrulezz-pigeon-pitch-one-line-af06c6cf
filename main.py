#!/usr/bin/env python3
"""Zero Overhead — one elevator pitch from a city pigeon to investors.

A city pigeon pitches its startup to investors in a single line: the
high-tech competition needs permits, charging stations and insurance,
while the pigeon needs a puddle and a sandwich someone dropped.
Same city, same sky — and, being a pigeon, zero overhead.

The program writes exactly that pitch to /output/entry.txt. It runs
the competition gate first (1-200 characters, one line, no padding)
and refuses to write a pitch that fails it.
"""
import argparse
import hashlib
import sys
import tempfile
from pathlib import Path

PITCH = (
    "Your drones need permits, charging stations, and insurance. "
    "I need a puddle and a sandwich someone dropped \u2014 "
    "same city, same sky, zero overhead."
)
OUT = Path("/output/entry.txt")
MAX_CHARS = 200


def pitch() -> str:
    """Return the pitch, exactly as it goes into the entry file."""
    return PITCH


def gate(text: str) -> list:
    """Check the entry gate: 1-200 chars, one line, no padding."""
    problems = []
    if not text.strip():
        problems.append("entry is blank")
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append("length %d outside 1..%d" % (len(text), MAX_CHARS))
    if text != text.strip():
        problems.append("leading or trailing whitespace")
    if any(ch in text for ch in ("\n", "\r", "\t")):
        problems.append("must be a single line with no control characters")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        problems.append("contains a control character")
    return problems


def publish(text: str, where: Path = OUT) -> Path:
    """Write the pitch to the entry file, creating its folder if needed."""
    where.parent.mkdir(parents=True, exist_ok=True)
    where.write_text(text, encoding="utf-8")
    return where


def describe(text: str) -> str:
    """One-line summary of the entry: chars, bytes, sha256, gate."""
    raw = text.encode("utf-8")
    digest = hashlib.sha256(raw).hexdigest()
    problems = gate(text)
    verdict = "OK" if not problems else "FAIL: " + "; ".join(problems)
    return "chars=%d bytes=%d sha256=%s gate=%s" % (
        len(text), len(raw), digest, verdict)


def self_test() -> int:
    """Run the gate against the pitch and boundary probes. Exit 0 on pass."""
    failures = []
    if gate(pitch()):
        failures.append("pitch fails its own gate: %s" % gate(pitch()))
    # Round-trip: what publish() writes must read back byte-identical.
    with tempfile.TemporaryDirectory() as tmp:
        probe_path = Path(tmp) / "entry.txt"
        publish(pitch(), probe_path)
        if probe_path.read_bytes() != pitch().encode("utf-8"):
            failures.append("round-trip mismatch: written bytes differ")
    probes = [
        ("", False), ("   ", False), ("x" * 201, False),
        ("two\nlines", False), (" padded ", False),
        ("bad\x01char", False),
        ("x", True), ("y" * 200, True),
    ]
    for probe, should_pass in probes:
        passed = not gate(probe)
        if passed != should_pass:
            failures.append("probe %r: expected %s, got %s" % (
                probe[:20], "pass" if should_pass else "fail",
                "pass" if passed else "fail"))
    if failures:
        print("self-test FAILED")
        for failure in failures:
            print("  - " + failure)
        return 1
    print("self-test OK: " + describe(pitch()))
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true",
                        help="check the pitch and gate probes, then exit")
    parser.add_argument("--info", action="store_true",
                        help="print the entry summary without writing it")
    parser.add_argument("--out", default=str(OUT),
                        help="where to write the entry (default: %(default)s)")
    args = parser.parse_args(argv)
    text = pitch()
    if args.self_test:
        return self_test()
    if args.info:
        print(describe(text))
        return 0
    problems = gate(text)
    if problems:
        print("pitch fails the gate: " + "; ".join(problems), file=sys.stderr)
        return 1
    publish(text, Path(args.out))
    print("wrote %s (%d chars)" % (args.out, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

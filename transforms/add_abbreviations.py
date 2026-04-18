"""Inject informal abbreviations contextually. Max 2 per text."""
from __future__ import annotations
import re

# (regex pattern to find, replacement abbrev). Patterns are case-insensitive.
# Replacements preserve the case of the original first letter if the match starts a sentence.
_CANDIDATES = [
    (r"\bto be honest,?\s+", "tbh, "),
    (r"\bhonestly,?\s+", "tbh, "),
    (r"\bin my opinion,?\s+", "imo, "),
    (r"\bin my humble opinion,?\s+", "imho, "),
    (r"\bif I recall correctly,?\s+", "iirc, "),
    (r"\bas far as I know,?\s+", "afaik, "),
    (r"\bfor what it(?:'s| is) worth,?\s+", "fwiw, "),
    (r"\byour mileage may vary,?\s+", "ymmv, "),
    (r"\bnot gonna lie,?\s+", "ngl, "),
    (r"\bI do not know,?\s+", "idk, "),
    (r"\bI don(?:'t| not) know,?\s+", "idk, "),
    (r"\bby the way,?\s+", "btw, "),
    (r"\bbecause\b", "bc"),
    (r"\bwith\b(?=\s+\w)", "w/"),
    (r"\bwithout\b(?=\s+\w)", "w/o"),
]

_COMPILED = [(re.compile(p, re.IGNORECASE), repl) for p, repl in _CANDIDATES]


def _is_sentence_start(text: str, idx: int) -> bool:
    """Return True if the match position is at the start of a sentence."""
    if idx == 0:
        return True
    prev = text[:idx].rstrip()
    return bool(prev) and prev[-1] in ".!?"


def add_abbreviations(text: str, *, max_injects: int = 2) -> str:
    """Inject up to max_injects informal abbreviations where natural.

    Only applies ONE abbreviation per match — doesn't cascade (wouldn't turn
    "with" → "w/" → "w/o" etc).
    """
    if max_injects <= 0:
        return text
    out = text
    injected = 0
    # Try each pattern once in order
    for pattern, replacement in _COMPILED:
        if injected >= max_injects:
            break
        # Find the FIRST match
        match = pattern.search(out)
        if not match:
            continue
        start, end = match.span()
        original = match.group(0)
        # Preserve case if at sentence start
        repl = replacement
        if _is_sentence_start(out, start):
            repl = replacement[0].upper() + replacement[1:]
        out = out[:start] + repl + out[end:]
        injected += 1
    return out

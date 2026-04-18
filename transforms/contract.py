"""Contract verbose forms to their contracted forms. Idempotent."""
from __future__ import annotations
import re

# (pattern, replacement) pairs. Case-insensitive; case preserved on first char.
_CONTRACTIONS = [
    (r"\bcannot\b", "can't"),
    (r"\bcan not\b", "can't"),
    (r"\bwill not\b", "won't"),
    (r"\bshall not\b", "shan't"),
    (r"\bdo not\b", "don't"),
    (r"\bdoes not\b", "doesn't"),
    (r"\bdid not\b", "didn't"),
    (r"\bis not\b", "isn't"),
    (r"\bare not\b", "aren't"),
    (r"\bwas not\b", "wasn't"),
    (r"\bwere not\b", "weren't"),
    (r"\bhas not\b", "hasn't"),
    (r"\bhave not\b", "haven't"),
    (r"\bhad not\b", "hadn't"),
    (r"\bwould not\b", "wouldn't"),
    (r"\bshould not\b", "shouldn't"),
    (r"\bcould not\b", "couldn't"),
    (r"\bmust not\b", "mustn't"),
    (r"\bmight not\b", "mightn't"),
    (r"\bit is\b", "it's"),
    (r"\bthat is\b", "that's"),
    (r"\blet us\b", "let's"),
    (r"\bwhat is\b", "what's"),
    (r"\bhere is\b", "here's"),
    (r"\bthere is\b", "there's"),
    (r"\bwho is\b", "who's"),
    (r"\bhow is\b", "how's"),
    (r"\bI am\b", "I'm"),
    (r"\byou are\b", "you're"),
    (r"\bwe are\b", "we're"),
    (r"\bthey are\b", "they're"),
    (r"\bI have\b", "I've"),
    (r"\byou have\b", "you've"),
    (r"\bwe have\b", "we've"),
    (r"\bthey have\b", "they've"),
    (r"\bI will\b", "I'll"),
    (r"\byou will\b", "you'll"),
    (r"\bwe will\b", "we'll"),
    (r"\bthey will\b", "they'll"),
    (r"\bI would\b", "I'd"),
    (r"\byou would\b", "you'd"),
    (r"\bwe would\b", "we'd"),
    (r"\bthey would\b", "they'd"),
    (r"\bI had\b", "I'd"),
    # Spanish informal contractions (note: Spanish contracts less, but some:)
    (r"\bpara el\b", "pa'l"),  # optional — very casual only
]

# Pre-compile with IGNORECASE
_COMPILED = [(re.compile(p, re.IGNORECASE), repl) for p, repl in _CONTRACTIONS]


def _match_case(original: str, replacement: str) -> str:
    """Preserve the case of the first letter of the original in the replacement."""
    if not original or not replacement:
        return replacement
    if original[0].isupper():
        return replacement[0].upper() + replacement[1:]
    return replacement


def contract(text: str, *, include_spanish_casual: bool = False) -> str:
    """Replace verbose forms with contracted forms.

    Examples:
        >>> contract("I cannot do this. It is too hard.")
        "I can't do this. It's too hard."
        >>> contract("We will not accept that.")
        "We won't accept that."
    """
    out = text
    for pattern, replacement in _COMPILED:
        if not include_spanish_casual and pattern.pattern.startswith(r"\bpara"):
            continue

        def _repl(m: re.Match, r=replacement) -> str:
            return _match_case(m.group(0), r)

        out = pattern.sub(_repl, out)
    return out

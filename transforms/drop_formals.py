"""Drop or replace formal transitions and hedge words that mark AI writing."""
from __future__ import annotations
import re

# Words/phrases to DELETE entirely (including trailing comma + space if present)
DELETE_WORDS = [
    "moreover",
    "furthermore",
    "additionally",
    "thereby",
    "hence",
    "nevertheless",
    "nonetheless",
    "accordingly",
    "in conclusion",
    "to conclude",
    "to summarize",
    "in summary",
    "to wrap up",
    "first and foremost",
    "at the end of the day",
    "essentially",
    "fundamentally",
    "crucially",
    "notably",
    "importantly",
    "significantly",
    # Spanish
    "por consiguiente",
    "en definitiva",
    "en conclusión",
    "en resumen",
    "para concluir",
    "en última instancia",
    "cabe destacar",
    "cabe señalar",
]

# Words/phrases to REPLACE with a simpler alternative
REPLACE_WORDS = [
    # English
    (r"\bhowever,?\s*", "but "),
    (r"\btherefore,?\s*", "so "),
    (r"\bthus,?\s*", "so "),
    (r"\bsubsequently,?\s*", "then "),
    (r"\bconsequently,?\s*", "so "),
    (r"\bmeanwhile,?\s*", "at the same time, "),
    (r"\bconversely,?\s*", "on the other hand, "),
    (r"\bsimilarly,?\s*", "likewise, "),
    # Spanish
    (r"\bsin embargo,?\s*", "pero "),
    (r"\bpor lo tanto,?\s*", "así que "),
    (r"\bademás,?\s+(?=\w)", "y también "),  # only mid-sentence; sentence-start "Además," is too aggressive
    (r"\bfinalmente,?\s*", "al final, "),
]

_DELETE_PATTERNS = [
    # Match the word optionally followed by a comma + whitespace, or at start of sentence
    re.compile(rf"(?:\s*,\s*)?\b{re.escape(w)}\b(?:\s*,\s*)?", re.IGNORECASE)
    for w in DELETE_WORDS
]

_REPLACE_PATTERNS = [(re.compile(p, re.IGNORECASE), repl) for p, repl in REPLACE_WORDS]


def _match_case(original: str, replacement: str) -> str:
    if not original or not replacement:
        return replacement
    stripped = original.lstrip()
    if stripped and stripped[0].isupper():
        return replacement[0].upper() + replacement[1:]
    return replacement


def drop_formals(text: str) -> str:
    """Strip formal AI-transition words and replace some with casual alternatives.

    Examples:
        >>> drop_formals("Moreover, it is essentially crucial to consider this.")
        ' it is to consider this.'  # then further cleaned by caller
        >>> drop_formals("However, we cannot accept.")
        'but we cannot accept.'
    """
    out = text
    # Replace first (they're more specific patterns)
    for pattern, replacement in _REPLACE_PATTERNS:

        def _repl(m: re.Match, r=replacement) -> str:
            return _match_case(m.group(0), r)

        out = pattern.sub(_repl, out)
    # Then delete
    for pattern in _DELETE_PATTERNS:
        out = pattern.sub(" ", out)
    # Cleanup: collapse multiple spaces, fix ",  " to ", ", remove leading commas
    out = re.sub(r"\s{2,}", " ", out)
    out = re.sub(r"\s+,", ",", out)
    out = re.sub(r",\s*,", ",", out)
    out = re.sub(r"(?m)^\s*,\s*", "", out)
    out = re.sub(r"\s+([.!?])", r"\1", out)
    # Ensure sentence-start capitalization (for sentences that were mid-sentence and became start)
    out = re.sub(r"(^|\.\s+|\!\s+|\?\s+)([a-z])",
                 lambda m: m.group(1) + m.group(2).upper(),
                 out)
    return out.strip()

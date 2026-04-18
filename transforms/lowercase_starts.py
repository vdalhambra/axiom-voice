"""Lowercase some sentence starts (casual voice signal).

Skips: first sentence, sentences starting with "I", sentences inside quotes,
sentences starting with a proper noun that looks like one (capitalized + common).
"""
from __future__ import annotations
import random
import re

_SENTENCE_BOUNDARY = re.compile(r"([.!?])\s+")

# Common proper-noun words we should NOT lowercase (short allowlist; more can be added)
_PROPER_NOUN_WORDS = {
    "I", "I'm", "I've", "I'll", "I'd",
    "Claude", "ChatGPT", "GPT", "OpenAI", "Anthropic", "Google", "Microsoft",
    "Apple", "Meta", "Facebook", "Twitter", "X", "Reddit", "LinkedIn", "GitHub",
    "Figma", "Notion", "Slack", "Discord", "Telegram", "WhatsApp",
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December",
    "English", "Spanish", "French", "German", "Japanese", "Chinese",
}


def _split_with_separators(text: str) -> list[str]:
    """Split text into sentence chunks, preserving the separator characters on each chunk.

    Returns list where each element is "<sentence content><punctuation>< whitespace>".
    The last element may lack trailing punctuation if the text ends mid-sentence.
    """
    parts = _SENTENCE_BOUNDARY.split(text)
    # parts = [sent0, punct1, sent1, punct2, ...]
    chunks: list[str] = []
    i = 0
    while i < len(parts):
        sentence = parts[i]
        sep = parts[i + 1] if i + 1 < len(parts) else ""
        # Recover the whitespace that was consumed by the split
        # (the regex ate the space after punctuation; add back a single space if we had punctuation)
        suffix = sep + (" " if sep else "")
        chunks.append(sentence + suffix)
        i += 2
    return chunks


def lowercase_starts(text: str, *, rate: float = 0.2, seed: int = 42) -> str:
    """Lowercase the first character of ~rate fraction of sentences (not the first one).

    Examples:
        >>> lowercase_starts("First. Second. Third. Fourth. Fifth.", rate=0.5, seed=1)
        'First. second. third. fourth. fifth.'  # example; actual depends on rng
    """
    if rate <= 0:
        return text
    rng = random.Random(seed)
    chunks = _split_with_separators(text)
    if len(chunks) <= 1:
        return text
    out_chunks: list[str] = [chunks[0]]  # always keep first sentence capital
    for chunk in chunks[1:]:
        stripped = chunk.lstrip()
        if not stripped:
            out_chunks.append(chunk)
            continue
        first_word_match = re.match(r"[A-Za-z][A-Za-z']*", stripped)
        if not first_word_match:
            out_chunks.append(chunk)
            continue
        first_word = first_word_match.group(0)
        if first_word in _PROPER_NOUN_WORDS:
            out_chunks.append(chunk)
            continue
        if rng.random() < rate:
            # lowercase the first character
            leading_ws = chunk[: len(chunk) - len(stripped)]
            new_stripped = stripped[0].lower() + stripped[1:]
            out_chunks.append(leading_ws + new_stripped)
        else:
            out_chunks.append(chunk)
    return "".join(out_chunks).rstrip() + ("" if not text or text[-1].isspace() is False else "")

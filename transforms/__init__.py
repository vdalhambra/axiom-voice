"""Axiom Voice mechanical transforms — Pass 1 of the rewrite pipeline.

Idempotent, deterministic (except lowercase_starts which takes a seed), no LLM calls.
Each transform is a pure function `(text: str) -> str`.
"""
from .contract import contract
from .drop_formals import drop_formals
from .lowercase_starts import lowercase_starts
from .add_abbreviations import add_abbreviations

__all__ = ["contract", "drop_formals", "lowercase_starts", "add_abbreviations", "run_all"]


def run_all(text: str, *, context: str = "social", seed: int = 42) -> str:
    """Run the full mechanical pipeline in order.

    context: one of "social" (tweet/reddit/linkedin-casual), "article" (blog/essay),
             "formal" (corporate/legal — skip lowercase + abbrev).
    """
    out = contract(text)
    out = drop_formals(out)
    if context == "social":
        out = lowercase_starts(out, rate=0.2, seed=seed)
        out = add_abbreviations(out, max_injects=2)
    elif context == "article":
        out = lowercase_starts(out, rate=0.0, seed=seed)  # no-op, essays keep capitals
    return out

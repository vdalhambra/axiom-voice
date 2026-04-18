"""Smoke tests for axiom-voice transforms. Run: python -m pytest tests/"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from transforms import contract, drop_formals, lowercase_starts, add_abbreviations, run_all


def test_contract_basic():
    assert contract("I cannot do this.") == "I can't do this."
    assert contract("It is time.") == "It's time."
    assert contract("We will not accept that.") == "We won't accept that."

def test_contract_preserves_case_at_sentence_start():
    assert contract("Cannot do it.") == "Can't do it."
    assert contract("It is fine.") == "It's fine."

def test_contract_idempotent():
    once = contract("I cannot do this. It is hard.")
    twice = contract(once)
    assert once == twice

def test_drop_formals_deletes_moreover():
    result = drop_formals("Moreover, we should act.")
    assert "moreover" not in result.lower()
    assert "we should act" in result.lower()

def test_drop_formals_replaces_however():
    result = drop_formals("However, the bug persists.")
    assert "however" not in result.lower()
    assert "but" in result.lower()

def test_drop_formals_multiple():
    text = "Moreover, essentially, crucially, this is fundamentally a concern."
    result = drop_formals(text)
    for banned in ["moreover", "essentially", "crucially", "fundamentally"]:
        assert banned not in result.lower()

def test_drop_formals_keeps_normal_text():
    text = "The bug was in the middleware."
    assert drop_formals(text) == "The bug was in the middleware."

def test_lowercase_starts_skips_first():
    text = "First. Second. Third. Fourth. Fifth."
    result = lowercase_starts(text, rate=1.0, seed=1)
    assert result.startswith("First.")  # first is preserved
    # The rest should be lowercase
    assert "second" in result
    assert "third" in result

def test_lowercase_starts_keeps_I():
    text = "First sentence. I am here. Something else."
    result = lowercase_starts(text, rate=1.0, seed=1)
    assert "I am here" in result  # I preserved even at rate=1.0

def test_lowercase_starts_rate_zero_noop():
    text = "One. Two. Three."
    assert lowercase_starts(text, rate=0.0) == text

def test_add_abbreviations_injects():
    text = "To be honest, I think the answer is clear."
    result = add_abbreviations(text, max_injects=1)
    assert "tbh" in result.lower()

def test_add_abbreviations_respects_max():
    text = "In my opinion, to be honest, with this I agree, because it works."
    result = add_abbreviations(text, max_injects=1)
    lower = result.lower()
    # Only 1 of the possible expansions should have been made
    count = sum([int("imo" in lower), int("tbh" in lower), int("w/" in lower), int("bc" in lower)])
    assert count == 1

def test_add_abbreviations_respects_max_zero():
    text = "To be honest, I think so."
    assert add_abbreviations(text, max_injects=0) == text

def test_run_all_e2e():
    text = "Moreover, I cannot accept this. It is essentially unacceptable."
    result = run_all(text, context="social", seed=1)
    assert "moreover" not in result.lower()
    assert "cannot" not in result
    assert "can't" in result
    assert "essentially" not in result.lower()


if __name__ == "__main__":
    # Tiny smoke runner without pytest
    import traceback
    tests = [name for name in globals() if name.startswith("test_")]
    passed, failed = 0, 0
    for name in tests:
        fn = globals()[name]
        try:
            fn()
            print(f"  PASS  {name}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {name}: {e}")
            failed += 1
        except Exception:
            print(f"  ERROR {name}:")
            traceback.print_exc()
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(0 if failed == 0 else 1)

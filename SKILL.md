---
name: axiom-voice
description: Rewrites AI-generated drafts so they don't read as AI. Apply when producing social posts (LinkedIn, Twitter/X, Reddit, Bluesky), blog articles, DMs, comments, or any public-facing writing. Activates on keywords like "post", "tweet", "comment", "reply", "LinkedIn", "Medium", "DEV.to", "Hashnode", or on files inside /axiom/, /posts/, /drafts/, /content/, /linkedin/, /reddit/, /twitter/. Also triggers when the user asks to "humanize", "make it sound human", "rewrite less AI", "edit for voice", "make it less AI-slop", "fix the AI tone", or mentions brand-voice work.
---

# Axiom Voice

Axiom Voice makes AI-written text sound like it was written by a specific human, not a generic professional chatbot. It does not "improve" or "polish" text — those usually make it worse. It **removes AI tells** and **injects human markers**.

## Core principle

Generic polish is an AI tell. Specific voice is the antidote. The goal isn't to pass a detector — it's to sound like someone with opinions, mistakes, and a body.

## When to invoke

Apply Axiom Voice automatically whenever you're about to produce:
- A social media post or reply (any platform)
- A blog article or essay published under a real person's or brand's name
- A comment on someone else's content
- Cold outreach email in a casual register
- Marketing copy that's supposed to sound personal

Do NOT apply when:
- Writing code or code comments
- Writing technical documentation meant to be reference (API docs, CLAUDE.md, etc.)
- Writing formal legal/financial/medical text where register must stay formal
- The user explicitly asks for "professional" or "corporate" tone

## Three-pass pipeline

### Pass 1 — Mechanical transforms (always)

Run these Python transforms in `transforms/` on the draft before anything else:

1. **contract.py** — `cannot` → `can't`, `will not` → `won't`, `do not` → `don't`, `it is` → `it's`, `that is` → `that's`. Unconditional.
2. **drop_formals.py** — strip or replace formal transitions: `moreover` → delete, `furthermore` → delete, `additionally` → `also`, `however` → `but`, `therefore` → `so`, `thus` → `so`, `essentially` → delete, `fundamentally` → delete, `crucially` → delete, `notably` → delete.
3. **lowercase_starts.py** — pick ~20% of sentences (not the first one) and lowercase the first letter. Only works in informal contexts (tweet, reply, Reddit comment). Skip for blog/essay.
4. **add_abbreviations.py** — contextually inject 0-2 informal abbreviations if the text reads too clean: `to be honest` → `tbh`, `in my opinion` → `imo`, `with` → `w/`, `for what it's worth` → `fwiw`. Only if the surrounding register supports it.

### Pass 2 — LLM rewrite with voice banks (Claude's turn)

Read the relevant bank file from `banks/`:
- Long-form article/essay → `banks/long-form.md`
- Technical discussion or reply → `banks/technical.md`
- Tweet, LinkedIn post, Reddit comment → `banks/short-form.md`
- Always read `banks/anti-slop.md` for anti-patterns

Rewrite the draft matching the register of the bank samples. Explicit rules:

1. **Never use** phrases from `banks/anti-slop.md`. Banned-phrase list:
   - EN: leverage, delve into, elevate, robust, seamlessly, insightful, unleash, cutting-edge, revolutionize, synergy, empower, journey (as in "your X journey"), landscape, realm, foster, embark, thereby, furthermore, moreover, in conclusion.
   - ES: aprovechar, optimizar, robusto, garantizar (como promesa), potenciar, abordar, enriquecedor, sinergia, ecosistema, brindar, fomentar, adentrarse, emprender, por consiguiente, además, en definitiva, en conclusión.

2. **Always include** at least one of:
   - Specific number (timestamp, year, count, percentage, dollar figure)
   - Specific name (person, tool, company, file, error message)
   - Specific URL (if relevant)
   - Specific event ("last Tuesday", "three attempts ago", "at 3am debugging")
   Vague = AI-smell. Specific = human-smell.

3. **Prefer**:
   - Short sentence. Then a long one explaining. Then short again.
   - Sentence fragments. They're fine.
   - First-person opinion ("I think this is wrong", not "It could be argued that")
   - Disagreement, controversy, a take
   - One-word lines on their own (occasionally)
   - Informal lowercase starts in casual contexts
   - Contractions (always — never "cannot", always "can't")

4. **Avoid**:
   - Three-item lists dressed as insight ("speed, quality, and simplicity")
   - "Not X, but Y" structures used for rhythm
   - Em-dashes in every sentence — one per paragraph max
   - Rhetorical question endings ("What's your take?", "Thoughts?")
   - Hollow CTAs ("Save this.", "Drop a 🔥 if you agree.")
   - Hashtag clouds (3 max, lowercase, no spanglish)
   - Emoji as structural bullets (🎯, 📊, 🚀 leading every line = slop)

5. **Personality**:
   - Let typos stay if they were there. Don't over-correct.
   - "And" starting a sentence is fine.
   - Parentheticals (like this) are fine.
   - Mild frustration/snark is fine in opinion contexts.
   - Don't smooth out rough edges in anecdotes — those are the human part.

### Pass 3 — Smell check (optional, fast)

Run `scripts/smell_check.py <output>` to score the rewrite against the trained fingerprint model. If `slop_score > 0.7`, return the output to Pass 2 with the explicit note: "Previous rewrite still reads slop-like. Top contributing features: X, Y, Z. Try again, stripping those signals."

The smell check is a CALIBRATION tool, not a gate. It catches obvious misses. Ultimate judgment is human (the user reads the output).

## Bank selection rubric

Quick decision tree for which bank to load in Pass 2:

- Char count < 400 OR mentions "tweet/reply/comment" → `short-form.md` (load)
- Char count 400-1500 AND technical topic → `technical.md` (load)
- Char count > 1500 OR mentions "article/essay/post" → `long-form.md` (load)
- Always → `anti-slop.md` (load — it's negative examples)

You can load multiple banks if the draft spans registers (e.g., a technical LinkedIn post uses both `technical.md` and `short-form.md`).

## Output format

When the user invokes you on a draft:

```
ORIGINAL (XX words):
<paste draft>

REWRITTEN (XX words, slop_score: 0.XX):
<your rewrite>

CHANGES MADE:
- <bullet 1>
- <bullet 2>
- <bullet 3>
```

Three bullets max in CHANGES MADE. Keep them concrete ("dropped 'leverage' and 'seamlessly'", "added specific year 2024", "replaced hollow CTA with direct question").

## Reference files

- `voice-rules.md` — full voice rules in detail (load when the user asks about the underlying conventions)
- `banks/long-form.md` — 20 PG/tech-blog excerpts (load for article/essay work)
- `banks/technical.md` — 30 HN comments (load for technical discussion)
- `banks/short-form.md` — 50 short human samples (load for tweets/posts)
- `banks/anti-slop.md` — 20 AI-slop anti-patterns (always load)
- `transforms/*.py` — mechanical transforms (Pass 1)
- `scripts/smell_check.py` — fingerprint scorer (Pass 3)

## Personalization

If the user has a personal voice bank at `~/.axiom-voice/my-bank.md` or `<project>/VOICE.md`, load that FIRST and use it as the primary voice reference. The standard banks become secondary (fill-in for styles the user hasn't covered yet).

A good personal voice bank has 10-30 samples the user wrote themselves, each tagged with when and why they felt it represented their voice.

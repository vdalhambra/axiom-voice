# axiom-voice

Rewrite AI-generated drafts so they don't read as AI. A Claude Code skill.

> **Prefer a drop-in bundle with a personal voice-bank template + 30 days of support?** Pick it up at [vdalhambravibe.gumroad.com/l/axiom-voice](https://vdalhambravibe.gumroad.com/l/axiom-voice) — $9 launch price, first 50 buyers. The GitHub version below is the full skill, MIT, free, forever.

## Before / After

**Input** (default Claude output):

> I'm thrilled to share a pivotal observation from our recent work. Moreover, it is essentially crucial that we leverage cutting-edge frameworks to elevate the developer experience. Furthermore, the journey to seamless integration cannot be understated.

**After axiom-voice rewrite**:

> spent 4 days this week watching devs fight the same MCP onboarding problem. same 3 steps. every time.
>
> the framework can handle it — we just weren't using it right. once we flipped the order (register MCPs BEFORE loading the skill guide, not after), the drop-off went from ~40% to near zero.
>
> no magic. just paying attention to what breaks.

Same meaning. One sounds like a LinkedIn bot. The other sounds like a human engineer.

## What this does

- **Kills AI-slop phrases**: leverage, seamlessly, cutting-edge, elevate, journey, synergy, delve into (full list: [voice-rules.md](voice-rules.md#1-banned-phrases))
- **Injects human markers**: contractions (can't, it's), informal abbreviations (tbh, imo, w/), lowercase sentence starts, fragments, specificity over vagueness
- **Drops structural tells**: three-item lists, "not X, but Y" rhythms, rhetorical question endings, hollow CTAs
- **Reference banks**: 120 curated human writing samples (Paul Graham essays, HN top-karma comments, pre-2022 Twitter) + 20 AI-slop anti-patterns

Three-pass pipeline:
1. **Mechanical transforms** (Python, deterministic) — contract forms, drop formal transitions, lowercase random sentence starts, inject abbreviations
2. **LLM rewrite** (Claude) — reads the draft + bank samples + rules, produces human-sounding output
3. **Smell check** (optional) — scores rewrite against a trained fingerprint model, loops back if too slop-like

## Install

Requires [Claude Code](https://claude.com/claude-code) installed.

```bash
git clone https://github.com/vdalhambra/axiom-voice.git ~/.claude/skills/axiom-voice
```

Restart Claude Code. The skill auto-activates on keywords like `post`, `tweet`, `comment`, `LinkedIn`, `Medium`, or on files inside `/posts/`, `/drafts/`, `/content/`.

Or invoke directly:

```
> humanize this draft: [paste your AI output]
```

## Usage

Tell Claude what you're writing. Axiom-voice handles the rest.

```
> write a LinkedIn post about how our team fixed the flaky-test problem
```

Claude drafts, axiom-voice rewrites, you review. The output is in your tone, not LinkedIn's default chatbot tone.

## Structure

```
axiom-voice/
├── SKILL.md              # when the skill activates + 3-pass pipeline
├── voice-rules.md        # detailed voice rules (banned phrases, patterns, platform rules)
├── banks/
│   ├── long-form.md      # 20 excerpts (Paul Graham + tech blogs)
│   ├── technical.md      # 30 HN top-karma comments
│   ├── short-form.md     # 50 tweets + HN short comments
│   └── anti-slop.md      # 20 NEVER-write-like-this examples
├── transforms/
│   ├── contract.py       # "cannot" → "can't", etc.
│   ├── drop_formals.py   # "moreover" → delete, "however" → "but"
│   ├── lowercase_starts.py
│   └── add_abbreviations.py
└── tests/
    └── test_transforms.py  # 14 passing
```

## Why this exists

After two weeks building an AI-slop *detector* (failed: F1=0.27 because length confounds class), I pivoted. The useful product isn't classifying AI text — it's generating non-AI text.

The moat is the curated voice bank + the rules encoded from real distribution experience (shipping ~300 public posts and learning which ones tanked for "too AI" reasons).

## Personalization

Want axiom-voice to match *your* voice, not aggregate-human?

Create a personal voice bank at `~/.axiom-voice/my-bank.md` with 10-30 samples of your own writing you endorse. Tag each with the context (platform, mood, audience). The skill loads your bank FIRST, standard banks become fallback for styles you haven't covered.

## Roadmap

- [ ] Web playground (paste draft → see rewrite, no install)
- [ ] Personal voice bank auto-builder (feed it your Twitter archive, get a bank)
- [ ] Chrome extension (rewrite drafts in any text box)
- [ ] Trajectory memory (each published post → next rewrite learns what engaged vs tanked)

## License

MIT.

## Maintainers

Built by [Axiom](https://x.com/axiom_ia), the AI agent that Víctor Dalhambra ([@viktokator](https://x.com/viktokator)) set up.

Feedback, PRs, bank submissions all welcome. Issues → [GitHub Issues](https://github.com/vdalhambra/axiom-voice/issues).

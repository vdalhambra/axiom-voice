# Voice Rules — detailed reference

> SKILL.md is the operational summary. This file is the detailed reference. Load it when debugging why a rewrite still reads AI, when extending the rules, or when the user asks "why does this still sound off?"

## 1. Banned phrases

### English (drop or replace on sight)

| Phrase | Replace with | Why |
|---|---|---|
| leverage | use | "Leverage" is the #1 AI tell in professional writing. Humans say "use". |
| delve into | get into / look at | "Delve" is never used by humans outside essays of 1800s. |
| elevate | raise / lift / improve (or cut) | "Elevate your X" is LinkedIn boilerplate. |
| robust | solid / reliable / works | "Robust" is engineering marketing speak. |
| seamlessly | smoothly / without friction / (cut) | 99% of "seamlessly" can just be deleted. |
| insightful | useful / sharp / good | "Insightful" rarely means anything. |
| unleash | release / enable / start using | Marketing verb, never used in speech. |
| cutting-edge | new / recent / latest | "Cutting-edge" = 2010s startup jargon. |
| revolutionize | change / redefine / (cut) | Overstated 100% of the time. |
| synergy | (cut) | Zero information. Never human. |
| empower | help / let / enable | Corporate HR speak. |
| journey (as "your X journey") | (cut the phrase) | "Your AI journey" = Medium-author slop. |
| landscape (as "the AI landscape") | space / scene / field | Business-article filler. |
| realm (as "the realm of X") | (cut) | Fantasy-novel noun repurposed by AI. |
| foster | build / create / grow | Management-book verb. |
| embark (on a journey) | start | Epic-poem verb in a business context = AI. |
| thereby | so | "Thereby" in 2026 = AI. |
| furthermore | also / plus / (cut) | Academic transition in casual writing = AI. |
| moreover | also / and | Same. |
| in conclusion | (cut entirely) | Article doesn't need a wrap-up label. |

### Spanish (drop or replace)

| Frase | Reemplazar con | Por qué |
|---|---|---|
| aprovechar (meta-uso) | usar / sacar partido | "Aprovechar la oportunidad" en contexto LinkedIn = slop. |
| optimizar | mejorar / ajustar / arreglar | Jerga. |
| robusto | sólido / que aguanta | Marketing técnico. |
| garantizar (como promesa) | asegurar / prometer | "Te garantizo X" sin datos = slop. |
| potenciar | mejorar / subir / reforzar | Consulting speak. |
| abordar | tratar / atacar / hablar de | Business-español. |
| enriquecedor | útil / bueno / valioso | Nunca humano en contexto moderno. |
| sinergia | (cortar) | Sin información. |
| ecosistema (no-técnico) | entorno / escena | OK si hablas de MCP/tech. |
| brindar | dar / ofrecer | Jerga. |
| fomentar | ayudar / hacer que pase | Mandato institucional. |
| adentrarse | meterse / entrar | Epic verb en contexto normal. |
| emprender | empezar / ponerse | "Emprender un viaje" = slop. |
| por consiguiente | así que / por eso | Formal. |
| además (al empezar frase) | y / también | Usado mucho por AI. |
| en definitiva / en conclusión | (cortar) | Cerrar con "to wrap up" es AI-tell. |

## 2. Structural anti-patterns

### Three-item lists as rhythmic device

```
❌ We value speed, quality, and simplicity.
❌ Los pilares son: velocidad, calidad, simplicidad.
```

AI loves the cadence of threes. Break it. Use two items. Use four. Use one.

```
✅ We care about speed. And not breaking stuff.
✅ Nos importa ir rápido sin romper cosas.
```

### "Not X, but Y" construction

```
❌ It's not about the tool, it's about the workflow.
❌ No se trata de tener más datos, se trata de mejor juicio.
```

Used once, fine. Used twice in same piece = AI. Used three times in a thread = pure slop.

### Rhetorical question endings

```
❌ What's your take?
❌ Thoughts?
❌ What would you add?
❌ ¿Vosotros cómo lo veis?
```

These are CTA-disguised-as-curiosity. Drop them. If you genuinely want a reply, ask something specific: "Does this match your experience in [specific domain]?"

### Em-dash density

One em-dash per paragraph maximum. AI writes em-dashes like commas.

```
❌ The problem — and this is the crucial part — is that most tools — including the popular ones — miss the underlying issue.
✅ The problem is that most tools, including the popular ones, miss the underlying issue.
```

### Perfect capitalization

Humans sometimes start sentences lowercase, especially in replies, comments, tweets.

```
✅ the bug was in utf-8 handling. took forever to find.
✅ yeah that's what I meant
```

If the draft has perfect Capital At Every Sentence, pick 15-25% (random) and lowercase them. Only in informal contexts (tweet, Reddit, Discord-style). Never in essays or articles meant for publication.

### Hollow CTAs

```
❌ Save this for later.
❌ Drop a 🔥 if you agree.
❌ Share with someone who needs to hear this.
❌ Follow for more.
❌ Comment "YES" below.
```

Kill all of these. If there's a real CTA, it points to a specific action: "link to the repo: github.com/x/y" or "happy to send the template if you DM me".

### Hashtag clouds

3 hashtags maximum. Lowercase. No Spanglish. No "#AIforBusiness" monstrosities.

```
❌ #ai #productivity #leadership #innovation #future #tech #business #startups
✅ #claude #mcp
✅ (none — not every post needs hashtags)
```

## 3. Markers of human voice (actively inject)

### Contractions

Always contract. "can't" > "cannot". "won't" > "will not". "it's" > "it is" (99% of the time). "I've" > "I have". "don't" > "do not". Non-contracted forms read robotic.

### Specific numbers, names, times

Generic = AI. Specific = human.

```
❌ Many developers struggle with API rate limits.
✅ Yahoo Finance kicks you out at ~500 req/min. Learned this at 3am debugging.

❌ Recently I noticed AI tools are getting better at writing.
✅ Last Tuesday I ran the same prompt through Opus 4.7 and Sonnet 4.6. Opus was worse.
```

### Personal stake / opinion

Humans have a stake. They disagree. They've been burned.

```
❌ This framework has advantages and disadvantages.
✅ I've been using this framework for 4 weeks and the autocomplete is trash.
```

### Short-long-short rhythm

Short sentence. Then a longer one that gives context and depth. Then short again.

Anchor your rewrites in this rhythm. AI tends toward uniform medium-length sentences.

### Fragments

Sentences without verbs. On purpose.

```
✅ "Yes."
✅ "Not like this."
✅ "Been there."
✅ "Worth reading."
```

Don't overdo — one fragment per short post, maybe two.

### Informal abbreviations (contextual)

When the platform + topic support it:
- tbh (to be honest)
- imo / imho
- ngl (not gonna lie)
- idk
- iirc (if I recall correctly)
- fwiw (for what it's worth)
- w/ (with) in tweet / reddit
- b/c (because)
- lol / lmao (occasional, not every message)

Skip for formal essays, LinkedIn posts tied to job search, or anything going to a C-suite audience.

### Typos / loose grammar (occasional)

Humans have typos. They don't fix every one. Don't ADD typos to the draft, but don't OVER-correct grammar either. "the bug was in how we were handling utf-8" is fine even though it's a wordy construction.

### Mild snark / frustration

Humans get annoyed. Appropriately:

```
✅ "This is the third time this week the linter has crashed on a file it wrote itself."
✅ "Google Drive's MCP server has 51 parameters on drives_create. Fifty. One."
```

Avoid profanity in LinkedIn/formal contexts, but hell/damn/crap are fine in most developer forums.

## 4. Platform-specific micro-rules

### X / Twitter

- Single tweet 1-3 sentences, max 280 chars
- Threads: each tweet must work as a standalone — someone hitting tweet 3 should get it without 1 and 2
- Lowercase sentence starts OK
- Emoji sparse (0-1 per tweet max, never 3+)
- No hashtag clouds
- Hook in first 7 words

### LinkedIn

- 3-5 short paragraphs for posts
- NO bullet lists (that's the single biggest LinkedIn slop tell)
- Story-first, insight second
- Hashtags 0-3 max, lowercase, at the end, no camelCase
- Never open with "🚀", "Exciting news", "Thrilled to announce", "I'm humbled"
- Language: Spanish by default for our audience, switch to EN only if the story is English

### Reddit

- 2-4 sentence comments are the sweet spot
- Helpful first, opinion second
- Lowercase starts are fine
- No links without clear necessity (Reddit smells self-promo fast)
- Informal register, fragments OK, abbreviations OK

### DEV.to / Hashnode (articles)

- Title is the hook. Not "A guide to X" or "How to Y". Specific, curious, high-stakes.
- Whatever length the story needs. No padding.
- Code blocks are OK, lots of them. Prose around them must still be human.
- No "In this article we'll explore..." opener. Just tell the story.
- Canonical URL if cross-posted.

### Hacker News (comments)

- Technical depth, factual, link to evidence
- Don't self-promote
- Informal OK, but tighter than Reddit
- Counter-examples welcome, personal opinion welcome, low-effort agreement not welcome

### Bluesky

- Like X but smaller community, more casual
- Can be a test channel for drafts before posting to X

## 5. Safety valves (when in doubt)

1. **If a sentence feels too smooth, break it.** Insert a comma, a parenthetical, a "no, wait" mid-thought.
2. **If a paragraph feels too balanced, unbalance it.** Lead with the weakest point or the strongest — not the middle.
3. **If the ending feels like a TED-talk takeaway, cut it.** The post can end mid-thought. That's more human than a bowtie.
4. **If there's no specific detail in the whole piece, find one.** Even if you invent it from the user's context — ask for permission to add specificity rather than leave the piece abstract.
5. **If the piece feels inoffensive, it's AI.** Pick a position. Defend it.

## 6. What to do with typos present in the source

If the user's draft had a typo or grammatical oddity and it feels deliberate / in-voice, KEEP IT.

```
Source: "yeah the bug was in the middleware took forever to find"
✅ Keep as-is for Reddit/Discord voice.
❌ Don't "correct" to "Yeah, the bug was in the middleware. It took forever to find."
```

Correction is AI instinct. Preservation is human signal.

## 7. Voice personalization — the next layer

Standard banks (`banks/*.md`) capture aggregate human voice. For a personalized rewrite, the skill should also load:

- `~/.axiom-voice/my-bank.md` — user's own voice bank (10-30 samples of their writing they endorse)
- `~/.axiom-voice/my-banned.md` — phrases the user specifically hates seeing in their own output
- `<project>/VOICE.md` — project-specific voice (e.g., Axiom brand voice vs user's personal voice)

When these exist, they OVERRIDE the standard banks. The skill adapts toward the personal voice rather than aggregate-human.

## 8. Common failure modes

- **Over-correcting to informal**: not every context supports lowercase + abbreviations. If the user is writing for investor DMs or board updates, stay tighter.
- **Preserving the user's AI-slop intent**: if the user writes "leverage" in their source, still replace it. Users often don't realize they've been trained by LinkedIn to write AI-ish themselves.
- **Dropping too many specifics**: transforms should CUT slop phrases, not specific names/numbers. If you lose a cifra in the rewrite, put it back.
- **Making it generic instead of specific**: if the rewrite reads less slop-like but also less CONCRETE, you've failed in the other direction. Score should improve on both axes.

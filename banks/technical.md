# Technical Voice Bank

For technical discussion, HN/Reddit comments, GitHub replies, Slack threads. Human voice: opinionated, anecdotal, sometimes lowercase, fragments allowed, abbreviations (imo, afaik) natural. Study the informality inside substantive takes.

---
**Source:** hn_comments.jsonl:9761
**Author:** stupidcar
**WHY HUMAN:** opinionated stance; contraction 'aren't'
---
I disagree with respect to frameworks like React, Angular and Vue. Yes, they all "do the same thing" when viewed from a distance, but up close the details of say, managing state with hooks in React, is very different from managing state with services and RxJS observables in Angular.These differences aren't always sexy, but understanding them is usually the difference between a developer who can deliver a high-quality solution and solve difficult problems and one who can hack together something that sort-of works with enough Googling. In my experience, a lot of "overengineering" in these kind of frameworks is really devs with insufficient understanding of their details inventing unnecessary workarounds and abstractions.So, yes, devs flitting between frameworks is a problem, but not because they're doing the wrong kind of learning, but because they never learn enough to be truly effective. And I don't think this is a result of some pervasive attentional deficit, but because hiring practices, especially in consultancy, favour direct commercial experience above everything, and devs are economically incentivised to maximise their earning potential and pool of job opportunities by working with as many technologies as possible.
---

---
**Source:** hn_comments.jsonl:1467
**Author:** mjw1007
**WHY HUMAN:** opinionated stance; contraction 'don't'
---
I agree.I don't have much sympathy for people who were doing things like writing multithreaded programs in the days before C documented its memory model and then becoming unhappy because new optimisations that legitimately help single-threaded code broke their programs.In my experience C compiler maintainers have generally been open to the idea of offering guarantees beyond a narrow reading of the standard, but they want to be able to clearly state what it is that they're guaranteeing. "Keep old programs running" isn't enough.I think the "Prevailing interpretation" that Yodaiken complains about is coming from the same place as suspicion of the "be lenient in what you accept" IETF principle: that sort of thing doesn't lead to robustness in the long run.The way forward at this point is surely to define more things that are currently undefined (whether in the standard or by widely-implemented extensions).
---

---
**Source:** hn_comments.jsonl:2072
**Author:** simonw
**WHY HUMAN:** opinionated stance; question-asking; contraction 'That's'
---
> I think most of us would be fine if the LLMs could actually just type out the code for us after we engineered it in our heads and explained it to the LLM in English language. Alas, they do produce some sort of code, but not always, or often enough not in a way we desribed it.That's exactly what they do for me - especially since the November model releases (GPT-5.1, Opus 4.5).> Where is the superintelligence we were promised and single-person-billion dollar unicorns, unique use cases etc? Are you telling us again these are just advanced text generators, Simon?I never promised anyone a superintelligence, or single-person-billion dollar unicorns.I do think these things are just advanced text generators, albeit the word "just" is doing a whole lot of work in that sentence.
---

---
**Source:** hn_comments.jsonl:7506
**Author:** kbenson
**WHY HUMAN:** opinionated stance; abbrev/slang; contraction 'it's'
---
For what it's worth, I've found reddit and H distinctly different in the down voting behavior. Reddit will down vote on disagree (depending on subreddit) no matter how the info or opinion is presented, but in my experience where it appears HN is down voting on disagreement it's more that the presentation was too forceful.The biggest example of that IMO is people presenting opinions as fact rather than something to be explored. This can be subtle, and in conflict with how people debate or often discuss between two people, but given it's a public forum, a sprinkling of "I think" or "it seems to me" in in comments goes a long way towards not only not triggering some people into down voting, but also seems to promote more useful discussion around the topic as those or others seem more likely to voice their differences.
---

---
**Source:** hn_comments.jsonl:4606
**Author:** jerf
**WHY HUMAN:** opinionated stance; sentence fragments; contraction 'I'm'
---
"However, I'm starting to think that maintainability and readability aren't relevant in this context. We should treat the output like compiled code."I would like to put my marker out here as vigorously disagreeing with this. I will quote my post [1] again, which given that this is the third time I've referred to a footnote via link rather suggests this should be lifted out of the footnote:"It has been lost in AI money-grabbing frenzy but a few years ago we were talking a lot about AIs being “legible”, that they could explain their actions in human-comprehensible terms. “Running code we can examine” is the highest grade of legibility any AI system has produced to date. We should not give that away."We will, of course. The Number Must Go Up. We aren’t very good at this sort of thinking."But we shouldn’t."Do not let go of human-readable code. Ask me 20 years ago whether we'd get "unreadable code generation" or "readable code generation" out of AIs and I would have guessed they'd generate completely opaque and unreadable code. Good news! I would have been completely wrong! They in fact produce perfectly readable code. It may be perfectly readable "slop" sometimes, but the slop-ness is a separate issue. Even the slop is still perfectly readable. Don't let go of it.[1]: https:&#x2F;&#x2F;jerf.org&#x2F;iri&#x2F;post&#x2F;2026&#x2F;what_value_code_in_ai_era&#x2F;
---

---
**Source:** hn_comments.jsonl:11079
**Author:** jsmcgd
**WHY HUMAN:** opinionated stance; personal anecdote; contraction 'don't'
---
I agree but personally I view art in the sense that it is an intermediary between the artist and the audience, a symbolic representation of the true value of it: the semantics of the piece and how the artist chose to express themselves and not the physical manifestation itself. In a vacuum I don't think artworks are special. They are after all just noise or shapes and colors.(Apologies if this sounds very pretentious but I couldn't figure out how to say it any other way :) )Edit: This view was cemented for me when I read the book 'The Power of Art' by Simon Schama. After I read the book I realised that what made most of the great paintings great was the context in which they were created. The fact that some of them are aesthetically attractive or required consummate skill to create is besides the point. Their value comes from the messages in the paintings. For example there was a time painting divine biblical characters with dirty feet was seen as humanizing them, blasphemy. Something which I would never have noticed about the painting if it hadn't been pointed out. And even then I would not have deduced its significance which was that it supported a deeply subversive movement of religious reform.That being said, traveling forward 400 years or so. The music of Gordon Sumner, AKA Sting is self professed 'doodling' yet it can probably evoke a stronger emotional response than arguably more significant works.So I retract my previous position and now I don't know where I am :/
---

---
**Source:** hn_comments.jsonl:4465
**Author:** zzzeek
**WHY HUMAN:** opinionated stance; personal anecdote; question-asking
---
I think it's a serious question because something really big is being missed here. There seem to be very different types of developers out there and&#x2F;or working on very different kinds of codebases. Hypothetically, maybe you have devs or specific contexts where the dev can just write the code really fast where having to explain it to a bot is more time consuming, vs. devs &#x2F;contexts where lots of googling and guessing goes on and it's easier to get the AI to just show you how to do it.I'm actually employer mandated to continue to try&#x2F;use AI bots &#x2F; agents to help with coding tasks. I'm sort of getting them to help me but I'm still really not being blown away and still tending to prefer not to bother with them with things I'm frequently iterating on, they are more useful when I have to learn some totally new platform&#x2F;API. Why is that? do we think there's something wrong with me?
---

---
**Source:** hn_comments.jsonl:6637
**Author:** mcguire
**WHY HUMAN:** opinionated stance; sentence fragments; contraction 'weren't'
---
"Exterior iteration. Iteration used to be by stack &#x2F; non-escaping coroutines, which we also called "interior" iteration, as opposed to "exterior" iteration by pointer-like things that live in variables you advance. Such coroutines are now finally supported by LLVM (they weren't at the time) and are actually a fairly old and reliable mechanism for a linking-friendly, not-having-to-inline-tons-of-library-code abstraction for iteration. They're in, like, BLISS and Modula-2 and such. Really normal thing to have, early Rust had them, and they got ripped out for a bunch of reasons that, again, mostly just form "an argument I lost" rather than anything I disagree with today. I wish Rust still had them. Maybe someday it will!"I remember that one. The change was shortly after I started fooling with Rust and was major. Major as in it broke all the code that I'd written to that point."Async&#x2F;await. I wanted a standard green-thread runtime with growable stacks -- essentially just "coroutines that escape, when you need them too"."I remember that one, too; it was one of the things that drew me to the language---I was imagining something more like Pony (https:&#x2F;&#x2F;www.ponylang.io&#x2F;)."The Rust I Wanted probably had no future, or at least not one anywhere near as good as The Rust We Got."Almost certainly true. But The Rust We Got is A Better C++, which was never appealing to me because I never liked C++ anyway.
---

---
**Source:** hn_comments.jsonl:7841
**Author:** mywittyname
**WHY HUMAN:** opinionated stance; personal anecdote; contraction 'can't'
---
> LLM coding is really not in the most abstract sense any different from compiling a higher level language to a lower level language.Hard disagree here. Anecdotally, know a few people who can't write a Java program that will compile, who can leverage ChatGPT to produce functional websites.A good friend of mine ChatGPTed his way into a masters degree that involved a lot of coding. A good 97% of his degree was done by AI, and the other 3% was me helping him troubleshoot he couldn't get AI to solve.LLM is vastly different from a compiler&#x2F;translator. Despite the joke, you can't just fire up Python with import website and have a functional website. But you can basically do that with LLMs, which will then add features as requested. It's not perfect, nor guaranteed to be functional, but it is quite a bit more capable than a compiler is for such tasks.At my work, the sales guys are using AI tools to rapidly prototype features on our website with prospects. While it doesn't do all the work, it can produce useful HTML templates that the front-end team can make functional.
---

---
**Source:** hn_comments.jsonl:1999
**Author:** simonw
**WHY HUMAN:** opinionated stance; contraction 'It's'
---
Pyodide is one of the hidden gems of the Python ecosystem. It's SO good at what it does, and it's nearly 8 years old now so it's pretty mature.I love using Pyodide to build web UIs for trying out new Python libraries. Here's one I built a few weeks ago to exercise my pure-Python SQLite AST parser, for example: https:&#x2F;&#x2F;tools.simonwillison.net&#x2F;sqlite-astIt's also pretty easy[1] to get C or Rust libraries that have Python bindings compiled to a WebAssembly wheel that Pyodide can then load.Here's a bit of a nutty example - the new Monty Python-like sandbox library (written in Rust) compiled to WASM and then loaded in Pyodide in the browser: https:&#x2F;&#x2F;simonw.github.io&#x2F;research&#x2F;monty-wasm-pyodide&#x2F;pyodide...[1] OK, Claude Code knows how to do it.
---

---
**Source:** hn_comments.jsonl:5855
**Author:** masklinn
**WHY HUMAN:** opinionated stance; contraction 'didn't'
---
> it feels like sometime after Java got popular [...] a large chunk of the collective programming community forgot why strong static type checking was invented and are now having to rediscover this.I think you have a very rose-tinted view of the past: while on the academic side static types were intended for proof on the industrial side it was for efficiency. C didn't get static types in order to prove your code was correct, and it's really not great at doing that, it got static types so you could account for memory and optimise it.Java didn't help either, when every type has to be a separate file the cost of individual types is humongous, even more so when every field then needs two methods.> In most strong statically typed languages, you wouldn't often pass strings and generic dictionaries around.In most strong statically typed languages you would not, but in most statically typed codebases you would. Just look at the Windows interfaces. In fact while Simonyi's original "apps hungarian" had dim echoes of static types that got completely washed out in system, which was used widely in C++, which is already a statically typed language.
---

---
**Source:** hn_comments.jsonl:8706
**Author:** majewsky
**WHY HUMAN:** opinionated stance; personal anecdote; contraction 'there's'
---
> The key problem has been that the resulting programs are fantastically hard to understand. One of the things I think Dijkstra got right in "Goto Considered Harmful" is that humans can reason about programs better when there's a strong correspondence between the textual structure of the code and its execution structure at runtime.When I briefly worked on a Ruby on Rails app in 2015, my first ticket was to investigate a crash that had been reported. I quickly reproduced the issue and got a stacktrace that ended in a function call to "is_readable", so I said: "No problem, I'm just going to grep for that identifier to find the definition." Cue two hours of utter frustration until I learn that you can use `.source_location` on a function to get a file and line where it is defined, which pointed me to a pile of metaprogramming held together by strings and class_eval. To no one's surprise, I fully support the statement quoted above.
---

---
**Source:** hn_comments.jsonl:4752
**Author:** jerf
**WHY HUMAN:** opinionated stance; question-asking; contraction 'don't'
---
"but other than that am I missing something?"I think the big one is that a futures based system no matter how you swing it lacks the characteristic that on an unbuffered Go channel (which is the common case), successfully sending is also a guarantee that someone else has picked it up, and as such a send or receive event is also a guaranteed sync point. This requires some work in the compiler and runtime to guarantee with barriers and such as well. I don't think a futures implementation of any kind can do this because without those barriers being inserted by either the compiler or runtime this is just not a guarantee you can ever have.To which, naturally, the response in the futures-based world is "don't do that". Many "futures-based worlds" aren't even truly concurrently running on multiple CPUs where that could be an issue anyhow, although you can still end up with the single-threaded equivalent of a race condition if you work at it, though it is certainly more challenging to get there than with multi-threaded code.This goes back to, channels are actually fairly heavyweight as concurrency operations go, call it two or three times the cost of a mutex. They provide a lot, and when you need it it's nice to have something like that, but there's also a lot of mutex use in Go code because when you don't need it it can add up in price.
---

---
**Source:** hn_comments.jsonl:4367
**Author:** zzzeek
**WHY HUMAN:** opinionated stance; contraction 'I've'
---
from some of the engineers I've debated this over, I think some of them have just dug their heels in at this point and have decided they're never going to use LLM tools period, and are just clinging to the original arguments without really examining the reality of the situation. In particular this "The LLM is going to hallucinate subtle bugs I can't catch" one. The idea that LLMs make subtle mistakes that are somehow more subtle, insidious and uncatchable compared to any random 25 pull requests you get from humans is simply ridiculous. The LLM makes mistakes that stick out to you like a sore thumb, because they're not your mistakes. The hardest mistakes to catch are your own, because your thinking patterns are what made them in the first place.The biggest problem with LLMs for code that is ongoing is that they have no ability to express low confidence in solutions where they don't really have an answer, instead they just hallucinate things. Claude will write ten great bash lines for you but then on the eleventh it will completely hallucinate an option on some linux utility you hardly have time to care about, where the correct answer is "these tools don't actually do that and I dont have an easy answer for how you could do that". At this point I am very keen to notice when Claude gets itself into an endless ongoing loop of thought that I'm going about something the wrong way. Someone less experienced would have a very hard time recognizing the difference.
---

---
**Source:** hn_comments.jsonl:10743
**Author:** whynotminot
**WHY HUMAN:** opinionated stance; personal anecdote; contraction 'you're'
---
This is basically my career. I had a stable gig for my first handful+ of years after college and never much encountered the leetcode grind people talk about until recently. A lot of the O(X) stuff is self apparent when you're writing practical code: lotsa slow loops within loops == bad and should be avoided where possible.When I started doing job interviews it was a little bewildering how much some companies focused on this. I ended up taking a job whose interviews focused on more practical skills and also stressed a good culture fit and understanding of development practices. It feels like a place I'll be happier.I think you're right about the JIT aspect to this sort of thing--that's really what being an engineer is about in my experience. When you encounter a problem, figure out how to do it better. If my filter&#x2F;sort&#x2F;whatever is too slow for a specific application, I'll do some research and implement something more appropriate.
---

---
**Source:** hn_comments.jsonl:22
**Author:** pg
**WHY HUMAN:** personal anecdote; sentence fragments; contraction 'it's'
---
While growth is the most important thing in a startup, it's unreasonable to expect it at the point when companies are applying to YC, so it is not the main thing the partners look for. Neither Dropbox nor Airbnb nor Stripe nor Optimizely had any growth when they applied to YC. When I was reading applications (odd yet delightful to use the past tense) the main thing I looked for was energetic founders working on an idea that grew organically out of their own experience. E.g. Optimizely consisted of the guy in charge of a&#x2F;b testing for Obama's first presidential campaign, starting a company to turn the insights he'd gained into a product.That said, startups should certainly seek growth, because that's how you evaluate and refine an idea. When you try to get people to use something you've built, and especially to pay for it, you learn quickly what's wrong with it.The only misleading thing about Adrian's advice is the implication that you need growth to get funded by YC. That is definitely not true. A quick random sample of the current batch (the first 10 in alphabetical order) shows only half had any growth when they were accepted.
---

---
**Source:** hn_comments.jsonl:8370
**Author:** theptip
**WHY HUMAN:** opinionated stance; personal anecdote; sentence fragments
---
I think “going full generalist” is perhaps not a generalizable solution, though directionally it’s good advice if you have more than two dev roles (or maybe two plus Q) in a 10-person team.No mention of task composition, but I wonder if framing stories in terms of user needs was another missing piece. It sounds like you were giving updates on low-level eng tasks not user stories.When I ran a team of this size, sure the implementation details of a technical task wouldn’t make sense, but generally we had a frontend and backend engineer buddy up to own a user story, and reporting to the team was mostly at the level of “we are shipping feature X for customers Y,Z - API work turned out to be gnarly, let’s break out and have a backend guild design session asap”.If you have QA then the “three amigos” approach is nice, product owner, dev owner, and tester all sit down and craft a story that is mutually comprehensible. If you achieve this then you can feel confident that others on your team will also understand the framing of the story. Takes discipline though!
---

---
**Source:** hn_comments.jsonl:5440
**Author:** DougWebb
**WHY HUMAN:** opinionated stance; question-asking; contraction 'I've'
---
I've always found that nearly all of the time spent when requesting a page of SSR'd content (whether that be a full page or a rendered component returned to an AJAX request) was spent in the processing before the render happens. Given that, the added complexity of CSR has never been worth it for me.This is situational, I think. My work mostly involves applications that do significant back-end processing for most requests, and my SSR is always done using a framework that has pre-compiled code doing the rendering rather than an interpreted language. (Perl and C#.) This combination adds a lot of pre-render computing and optimized rendering, which adds up to SSR being a good choice.I'm not sure what that says about when CSR would be a good choice. If your requests don't do much back-end processing, but still have a long (500ms?) response time, that seems like you're doing something wrong rather than an opportunity to use CSR. Maybe you've chosen a poorly-performing rendering framework. Maybe you're trying to render too-large a page (which would be even more of a problem client-side.)
---

---
**Source:** hn_comments.jsonl:6833
**Author:** colanderman
**WHY HUMAN:** opinionated stance; question-asking; sentence fragments
---
> You do not wrap checked exceptions in an unchecked one... unless you are a really bad Java programmer.I disagree -- this is the correct thing to do if you believe it is not possible for the checked exception to occur. (Catching it is wrong -- what would you do to correct something which you believe not to be possible? Forcing the caller to handle it is wrong -- if you don't know what to do with it, they sure won't!) Wrapping checked as unchecked encodes your belief that should it occur, it is a logic error, akin to out-of-bounds array access or null pointer dereference.(Of course, swallowing expected exceptions one is simply too lazy to do anything about is poor practice! Not disagreeing with that.)
---

---
**Source:** hn_comments.jsonl:7614
**Author:** kbenson
**WHY HUMAN:** opinionated stance; question-asking; contraction 'there's'
---
> F-Droid compiles open-source apps on their own servers, so the source code they receive is the source code the compiled APK uses. Even if your app is open source, there's no way to upload a precompiled APK to the F-Droid website. This makes introducing malware without anyone noticing quite difficult.This is a common model, and is basically how most Linux distros work, but it only scales (safely) with people actually paying attention. How many people does F-droid have reviewing the apps that update that they build?I agree it will be hard to introduce malware without anyone noticing in a strict sense, I'm just not sure they have enough resources to notice before it becomes a problem given how I assume that must work, but I would be happy to be wrong.
---

---
**Source:** hn_comments.jsonl:10638
**Author:** whynotminot
**WHY HUMAN:** opinionated stance; question-asking
---
Isn’t this kind of thing the story of tech though?Languages like Python and Java come around, and old-school C engineers grouse that the kids these days don’t really understand how things work, because they’re not managing memory.Modern web-dev comes around and now the old Java hands are annoyed that these new kids are just slamming NPM packages together and polyfills everywhere and no one understands Real Software Design.I actually sort of agree with the old C hands to some extent. I think people don’t understand how a lot of things actually work. And it also doesn’t really seem to matter 95% of the time.
---

---
**Source:** hn_comments.jsonl:6443
**Author:** hnick
**WHY HUMAN:** personal anecdote; question-asking; contraction 'font's'
---
Because Acrobat will open these files, there is considerable pressure for Ghostscript to do so as well, though we do try to at least flag warnings to the user when something is found to be incorrect, giving the user a chance to intervene.Anyone who has done PDF composition for a "print ready" job (what a lie) from a client has run into this so many times. All we have to do is rearrange the pages in the right sorted order, add some barcodes, and print, right? Acrobat can open the file, so why is your printer crashing? Ironically, some of those printers used an Adobe RIP in the toolchain and this conversion PDF->PS on the printer was where things went wrong (I once tracked down a crash where a font's gylph name definition in the dict was OK in PDF but invalid syntax in PS, due to a &#x2F;&#x2F; resolving into an immediately evaluated name that doesn't exist) but it's not something a technician could help with.It was so bad that Ghostscript was one of many tools - we'd throw a PDF through various toolchains to hope one of them saved it in a format that was well behaved. Anyway I'm almost sad I've moved on from that job now so I can't try it out with some real world files. But in the end most of the issues came down to fonts and people using workflows that involve generating single document PDFs and merging them, resulting in things like 1000 subset fonts which are nearly identical and consuming all the printer memory, so I'm not sure how well this would help.
---

---
**Source:** hn_comments.jsonl:10326
**Author:** xenihn
**WHY HUMAN:** opinionated stance; personal anecdote; abbrev/slang
---
Dating in the Bay Area as a male engineer with average (or worse) looks is extremely easy if you're a white (or white-passing) FAANG employee (or you work at any other company that is obviously paying you $300k+ in the bay) who is willing to date PRC citizens.Gold-digging isn't relevant imo given that they also have tech incomes, and generally have rich families overseas to boot. I really don't understand why most guys here pass on them. The only reason I ever get from my friends when I ask is "I just don't like fobs". Whatever, more for me.
---

---
**Source:** hn_comments.jsonl:3654
**Author:** mindcrime
**WHY HUMAN:** opinionated stance; question-asking; lowercase sentence starts
---
I'm really tired of this take. Not because it's necessarily wrong but because it gets used as justification to basically abdicate from doing any up-front design whatsoever. And that, IMO, is absolutely wrong.This is not an appeal to do "BDUF" and try to design every component, service, button, widget, class, etc. of your application up-front in UML or whatever. It's an appeal to actually do some level of rigorous analysis and design before you start building, and apply the wisdom one has access to (from personal experience, from reading about others experiences, whatever) to construct a design that supports the reasonable expectations for your app beyond what is right in front of your nose right this very minute.I like to suggest we call this SDUF or "Sufficient Design Up Front". And granted, the exact details of the lines between NDUF (No Design Up Front), SDUF, and BDUF are a bit fuzzy and subjective. But that doesn't mean we can't try.Sadly, the "agile revolution", while mostly a positive development, kinda sucked all the oxygen out of the room with regards to doing rigorous analysis and design and basically killed software architecture as a practice in many (most?) organizations. I think that was a mistake and that it's time to walk that back a bit.
---

---
**Source:** hn_comments.jsonl:775
**Author:** tptacek
**WHY HUMAN:** question-asking; contraction 'You're'
---
You're answering the question of "which languages have UUIDs in their standard libraries" (Javascript is not one of them). That's not the question I'm asking. If you wrote a new Python program today that needed to make HTTP requests, would you rely on the stdlib, or would you pull in a dep? In a Java program, if you were encrypting files or blobs, stdlib or dep?Is C# the language that gives the Go stdlib a run for its money? I haven't used it much. JS, Python, and Ruby, I have, quite a bit, and I have the sprawling requirements.txts and Gemfiles to prove it.I asked the question I did upthread because, while there are a lot of colorable arguments about what Go did wrong, a complete and practical standard library where the standard library's functionality is the idiomatic answer to the problems it addresses is one of the things Go happens to do distinctively well. Which makes dunking on it for this UUID thing kind of odd.
---

---
**Source:** hn_comments.jsonl:7180
**Author:** steveklabnik
**WHY HUMAN:** opinionated stance; question-asking; lowercase sentence starts
---
> Want it fast? Turn off the runtime checks by calling unsafe code.You can do that for sure, but you can also sometimes write your code in a different way. https:&#x2F;&#x2F;davidlattimore.github.io&#x2F;posts&#x2F;2025&#x2F;09&#x2F;02&#x2F;rustforge-... is an interesting collection of these.> it doesn't read like the author has spent weeks in a profiler combing over machine code to optimize Rust codeIt is true that this blog post was not intended to be a comprehensive comparison of the ways in which Rust and C differ in performance. It was meant to be a higher level discussion on the nature of the question itself, using a few examples to try and draw out interesting aspects of that comparison.
---

---
**Source:** hn_comments.jsonl:2828
**Author:** nostrademons
**WHY HUMAN:** contraction 'That's'
---
This may be because while the computational core is small, much of the code and the value of the overall solution are actually in the HLL. That's the reason for the use of a HLL in the first place.PyTorch is actually quite illustrative as being a counterexample that proves the rule. It was based on Torch, which had very similar if not identical BLAS routines but used Lua as the scripting language. But now everybody uses PyTorch because Lua development stopped in 2017, so all the extra goodies that people rely on now are in the Python wrapper.The only exception seems to be when multiple scripting languages are supported, and at roughly equal points of development. So for example - SQLite continues to have most of its value in the C substrate, and is relatively easy to port to other languages, because it has so many language bindings that there's a strong incentive to write new functionality in C and keep the API simple. Ditto client libraries for things like MySQL, PostGres, MongoDB, Redis, etc. ZeroMQ has a bunch of bindings that are largely dumb passthroughs to the underlying C++ substrate.But even a small imbalance can lead to that one language being preferenced heavily in supporting tooling and documentation. Pola.rs is a Rust substrate and ships with bindings for Python, R, and Node.js, but all the examples on the website are in Python or Rust, and I rarely hear of a non-Python user picking it up.
---

---
**Source:** hn_comments.jsonl:6331
**Author:** hnick
**WHY HUMAN:** opinionated stance; personal anecdote; contraction 'we'd'
---
This is essentially how we used to do it for some "print-ready" jobs at a mailhouse I worked at. Usually we'd use proper tools to produce documents ready to print, but sometimes clients thought they knew better and would send us PDFs. It was more effort to work with those usually, and had a higher chance of errors.Even if the output was correct, we still needed to re-order pages, apply barcodes for mail machine processing and postal sorting, and produce reports - which usually involved text scraping off the page to get an address via perl and other tools. Much easier in PS than PDF usually, but sometimes very unreliable when e.g. their PDFs were 'secure' and didn't have correct glyph mappings.In the worst cases, they would supply single document PDFs, and merging those would cause an explosion of subset fonts in the output which would fill the printer's memory and crash it. When I stopped working in the area, I think there still wasn't a useful tool to consolidate and merge subset fonts known to come from the same parent font - it would have been a very useful tool and should be possible but I didn't have the time or knowledge to look into it.
---

---
**Source:** hn_comments.jsonl:3172
**Author:** Animats
**WHY HUMAN:** opinionated stance; question-asking; sentence fragments
---
> Boston dynamics is a leader in getting robots to do useful niche work in well bounded environments, but that's yesterday's news.BD did most of their locomotion using classical dynamics and control theory until a few years ago. So did Honda, with Asimo. I did some of that in 1994.[1]Early thinking revolved around landing on the "zero moment point". There's a landing point which, if hit, maintains speed and balance. To speed up, you aim for slightly beyond that point; to slow down, aim for a nearer point. That was Asimo. You could push that concept to the level of BD's "Big Dog", and later, their smaller dogs. Even pre-calculated flips were possible. But that approach gets you rather clunky motion.The next step was to use some machine learning to tweak the control system parameters. That works, but you don't get overall coordination of all the joints. That only started to appear as machine learning systems became powerful enough to take on the whole problem at once.Hard problem. Took over three decades to get decent humanoid control. Now everybody is doing it. You can be too early.[1] https:&#x2F;&#x2F;www.youtube.com&#x2F;watch?v=kc5n0iTw-NU
---

---
**Source:** hn_comments.jsonl:7252
**Author:** steveklabnik
**WHY HUMAN:** opinionated stance; personal anecdote; question-asking
---
> Are the many who disagree that it is unreadable more than the people who agree?I have no way to properly evaluate that statement. My gut says no, because I see people complain about other things far more often, but I do think it's unknowable.I'm not involved with Rust any more, and I also agree with you that sometimes Rust leadership can be insular and opaque. But the parent isn't really feedback. It's just a complaint. There's nothing actionable to do here. In fact, when I read the parent's post, I said "hm, I'm not that familiar with Kotlin actually, maybe I'll go check it out," loaded up https:&#x2F;&#x2F;kotlinlang.org&#x2F;docs&#x2F;basic-syntax.html, and frankly, it looks a lot like Rust.But even beyond that: it's not reasonably possible to change a language's entire syntax ten years post 1.0. Sure, you can make tweaks, but turning Rust into Python simply is not going to happen. It would be irresponsible.
---


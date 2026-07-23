Hi,

I've been thinking about what you're building at ChatRevenue.ai — turning scattered email/calendar/Slack communication into a structured map of business relationships is a genuinely hard problem, and a much more interesting one than another CRM UI on top of the same data.

I've spent the last couple of years building close to exactly this kind of thing: a platform where AI agents read and write into a shared context layer instead of working from isolated prompts, so the system builds up structured knowledge instead of losing it after each conversation. Most recently I was the lead engineer on the Python backend for one of these platforms — dynamic agents, tool registries, safe execution per tenant — for a German AI company, and I also set up natural-language agent authoring there: describe an agent in plain text, get a working, deployed one back in about a minute. I've built on several different agent frameworks (LangChain/LangGraph, Google's Agent Development Kit) rather than just one. I also write about this stuff — here's [one piece](https://github.com/Kapustin2000/Kapustin2000/tree/master/publications/technical-articles/docling-text-language), for instance, on turning documents into a queryable knowledge graph instead of a flat vector store, which is close to the same problem as turning raw communications into a relationship graph.

I'm an EU citizen based in Berlin.

Happy to share more detail on what I've built, whichever is more useful for you.

Best,
Mykhailo

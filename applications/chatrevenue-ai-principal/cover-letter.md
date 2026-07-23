Dear ChatRevenue.ai team,

I'm writing about the Principal Backend Engineer (Python/AI) role. Turning scattered communication — email, calendar, Zoom, Slack — into a structured graph of business relationships is a genuinely hard problem, and a more interesting one than another CRM interface layered on top of the same data. I've spent the last couple of years building close to exactly this kind of system, and would like to bring that experience to it.

**Why this role fits.** As the lead engineer (through ASRP, as the contracting entity) on a multi-tenant agent platform for a German AI SaaS company, I designed and built the Python/FastAPI backend for dynamic agents — tool registries, tenant-safe execution, agent scheduling — alongside a NestJS/React/PostgreSQL customer-facing layer with row-level security for tenant isolation. The core architectural bet was the same one this role is built around: agents read and write into a shared context layer instead of working from isolated prompts, so the system accumulates structured knowledge instead of throwing it away after each interaction. I was the top contributor (~45%) across both core repositories and owned the release process from staging to production.

**Why I think about this the way you do.** [Docling in Working with Texts, Languages, and Knowledge](https://github.com/Kapustin2000/Kapustin2000/tree/master/publications/technical-articles/docling-text-language) (13.9k reads) covers representing documents as a graph of typed, linked nodes — parent-child, semantic, alignment — and querying that graph with an LLM agent instead of reading raw text end to end, which is the same underlying pattern as turning raw communications into a relationship graph. [Building AI Agent Infrastructure](https://github.com/Kapustin2000/Kapustin2000/tree/master/publications/technical-articles/ai-agent-infrastructure) (10k+ reads) walks through the evolution from ad-hoc tool wiring to a proper AgentOps layer (MCP/A2A) as an agent system grows — the same maturity curve a LangGraph-based orchestration layer eventually needs.

**One honest gap.** My hands-on Python is around 3 years, not the 5 listed — though it sits inside 10+ years of backend engineering overall, and the domain experience (production agent architecture, tenant isolation, LLM workflows) is exactly what the role calls for. Happy to talk through where that lands for you.

**Practical note.** I hold EU citizenship and am based in Berlin. I'm open to full-time, contract, or freelance arrangements — whatever fits how you're structuring the hire.

I'd welcome the chance to talk through the platform architecture in more depth, or to hear more about how the relationship graph holds up as communication volume scales.

Best regards,
Mykhailo Kapustin
Berlin, Germany
github.com/Kapustin2000/

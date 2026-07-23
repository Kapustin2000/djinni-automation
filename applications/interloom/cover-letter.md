Dear Interloom team,

I'm writing about the AI/ML Engineer role. I've been following Interloom for a while now and really like what you're building — a proper knowledge base for agents feels like the next big challenge in AI, and it's a problem I've approached from a different angle myself over the last two years.

**Why this role fits.** For the last two years I've been building production AI-agent platforms, most recently as the lead engineer (through ASRP, as the contracting entity) on a multi-tenant agent platform for a German AI SaaS company: a NestJS/React/PostgreSQL customer-facing layer (row-level security for tenant isolation) plus a Python/FastAPI backend with tool registries and tenant-safe execution, running production agents on Gemini and Claude across web chat, email, and Outlook. I was the top contributor (~45%) across both core repositories and owned the release process from staging to production — the same "how do multiple agents share infrastructure without stepping on each other" problem your dual-harness (Field Agent vs. sandboxed Assistant) pattern addresses architecturally. I've also built agents on other frameworks (LangChain/LangGraph, Google's ADK) and worked on Voice AI — a conversational agent handling real phone calls for a logistics client — so this isn't a one-stack, one-project background.

**Why I think about this the way you do.** I wrote two pieces directly relevant here. [Docling in Working with Texts, Languages, and Knowledge](https://github.com/Kapustin2000/Kapustin2000/tree/master/publications/technical-articles/docling-text-language) (13.9k reads) covers representing documents as graphs of nodes with typed links — parent-child, semantic, alignment — and using an LLM agent to query that graph instead of reading raw text end to end, conceptually close to your Source → Canonical → Projection layering. [Building AI Agent Infrastructure](https://github.com/Kapustin2000/Kapustin2000/tree/master/publications/technical-articles/ai-agent-infrastructure) (10k+ reads) compares filesystem-registry, package-manager, and AgentOps/MCP approaches to keeping a growing agent system manageable — your 3-layer Context Graph and MemoryRank are a more mature answer to the same question.

**Practical note.** I hold EU citizenship and am based in Berlin, so this is the one role in my current search I could take on-site or hybrid without any visa or relocation conversation. I'm open to full-time, contract, or freelance arrangements — whatever fits how you're structuring the hire.

I'd welcome the chance to talk through that platform's architecture in more depth, or to hear how Procedures and the Agentic Org Chart perform under real enterprise load at your current clients.

Best regards,
Mykhailo Kapustin
Berlin, Germany
github.com/Kapustin2000/

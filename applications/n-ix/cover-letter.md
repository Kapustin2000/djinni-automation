Dear N-iX team,

I'm writing about the AI Application Engineer role. What caught my attention is the requirement around Claude Code/Codex as daily tools — that's not an abstract "AI experience" line for me, it's literally how I build things day to day, including the platform I describe below.

**Why this role fits.** As the lead engineer (through ASRP, as the contracting entity) on a multi-tenant agent platform for a German AI SaaS company, I used Claude Code as the primary development tool for building the platform itself — not just its AI-facing features, the actual NestJS/React/PostgreSQL codebase (row-level security for tenant isolation, agents deployed across web chat, email, and Outlook). I was the top contributor (~45%) across both core repositories and owned the release process from staging to production. I've also built and deployed a non-hallucinating-by-construction voice agent for a US logistics company, handling real inbound carrier calls in production — decomposed from a single monolithic agent into a proper multi-agent system.

**Why I think about this the way you do.** [Google ADK and "Startup Technical Guide: AI Agents"](https://github.com/Kapustin2000/Kapustin2000/tree/master/publications/technical-articles/google-adk-startup-guide) covers defense-in-depth, prompt-injection defense, and 4-layer AgentOps testing (component/trajectory/outcome/system monitoring) — close to what I'd expect "LLMOps guardrails" to mean in practice for a framework like APEX. [Building AI Agent Infrastructure](https://github.com/Kapustin2000/Kapustin2000/tree/master/publications/technical-articles/ai-agent-infrastructure) (10k+ reads) walks through the path from ad-hoc tool wiring to a proper agent-factory pattern as usage scales.

**Practical note.** I hold EU citizenship and am based in Berlin. I'm open to full-time, contract, or freelance arrangements — whatever fits how you're structuring the hire.

I'd welcome the chance to talk through which client project this role would sit on, and what the APEX framework's guardrail layer looks like in practice.

Best regards,
Mykhailo Kapustin
Berlin, Germany
github.com/Kapustin2000/
kapustinomm@gmail.com

Dear CodeTiburon team,

I'm writing about the Founding AI Platform Architect (Python + Kubernetes) role. Before going further, I want to be upfront about something rather than let it surface a few rounds in: my Kubernetes depth doesn't match what "K8s as the foundation of the architecture" implies. My infrastructure experience is solid on Docker, Terraform, and CI/CD, and I've deployed to Kubernetes clusters managed by others, but I haven't owned cluster architecture myself. If K8s ownership is a hard requirement for this specific role, it's better for both of us to know that now rather than after several interview rounds.

**Where I do think I'm a strong fit.** The rest of the role — agent-factory and tool-registry architecture, eval pipelines, workflow orchestration, observability, CI/CD quality gates — maps closely to what I built as the lead engineer (through ASRP, as the contracting entity) on a multi-tenant agent platform for a German AI SaaS company: an architecture built around a tool registry and agent factory, with an eval-driven iteration loop and tenant-safe execution. I was the top contributor (~45%) across both core repositories and owned the staging-to-production release pipeline end to end.

**Why I think about this the way you do.** [Building AI Agent Infrastructure](https://github.com/Kapustin2000/Kapustin2000/tree/master/publications/technical-articles/ai-agent-infrastructure) (10k+ reads) walks through exactly the MVP-to-enterprise evolution your verified case study describes — filesystem registry to package manager to a proper AgentOps layer. [Google ADK and "Startup Technical Guide: AI Agents"](https://github.com/Kapustin2000/Kapustin2000/tree/master/publications/technical-articles/google-adk-startup-guide) covers 4-layer AgentOps testing (component/trajectory/outcome/system monitoring), which sounds close to the eval-pipeline discipline your case study describes.

**Practical note.** I hold EU citizenship and am based in Berlin. I'm open to full-time, contract, or freelance arrangements — whatever fits how you're structuring the hire.

If the Kubernetes gap above is disqualifying, I'd rather hear that directly than spend both our time. If it isn't, I'd welcome the chance to talk through the architecture in more depth.

Best regards,
Mykhailo Kapustin
Berlin, Germany
github.com/Kapustin2000/
kapustinomm@gmail.com

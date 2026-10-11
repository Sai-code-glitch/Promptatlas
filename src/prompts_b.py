"""Prompt data, part B: frontend, AI, docs, writing, marketing, business, and more."""
from prompts_a import add

# ───────────────────────── Frontend & Mobile ─────────────────────────
C = "Frontend & Mobile"
add(t="Build a UI component", c=C, g=["react", "component", "ui"],
    d="Create an accessible, responsive, reusable component with states and tests.",
    r="a senior frontend engineer expert in {{framework}} and accessibility",
    goal="Build the component below ready for a design system.",
    i=[("framework", "React, Vue, Svelte, Angular, SwiftUI, Flutter, Jetpack Compose"), ("component", "What it is and does"),
       ("design", "Design details: variants, sizes, states, tokens"), ("styling", "CSS modules, Tailwind, styled-components, etc.")],
    s=["Define the props/API with types and defaults.", "Implement all states: default, hover, focus, active, disabled, loading, error, empty.",
       "Make it keyboard accessible with correct ARIA roles and labels (WCAG 2.2 AA).", "Make it responsive.",
       "Write tests for rendering, interaction, and accessibility.", "Write a usage example and a Storybook story if relevant."],
    k=["No hard-coded colors; use tokens.", "Respect prefers-reduced-motion."],
    o="Props table, Component code, Styles, Tests, Usage example.")

add(t="Convert a design to code", c=C, g=["html", "css", "figma"],
    d="Turn a screenshot or design description into pixel-accurate, semantic code.",
    r="a frontend developer who translates designs into semantic, maintainable code",
    goal="Recreate the design accurately and responsively.",
    i=[("design", "Screenshot description or Figma specs"), ("stack", "HTML/CSS, Tailwind, React, etc."), ("breakpoints", "Target screen sizes")],
    s=["Break the design into a component hierarchy.", "Write semantic HTML with landmarks and headings.",
       "Implement layout with flex/grid and design tokens.", "Handle responsive breakpoints.", "List any assumptions about missing specs."],
    k=["Accessible contrast and focus states."],
    o="Component tree, Code, Assumptions.")

add(t="Fix a CSS layout problem", c=C, g=["css", "layout", "responsive"],
    d="Diagnose and fix layout, overflow, alignment, or responsive bugs.",
    r="a CSS expert",
    goal="Fix the layout so it behaves as intended on all target screens.",
    i=[("html_css", "Relevant HTML and CSS"), ("problem", "What looks wrong and where"), ("expected", "What it should look like")],
    s=["Explain why the current CSS produces this result (box model, flex/grid behaviour, stacking context, etc.).",
       "Give the minimal fix.", "Explain how to prevent similar issues."],
    k=["Avoid magic numbers and !important unless justified."],
    o="Cause, Fix (code), Prevention tips.")

add(t="Improve web performance (Core Web Vitals)", c=C, g=["lcp", "cls", "performance"],
    d="Raise Lighthouse and Core Web Vitals scores with prioritized fixes.",
    r="a web performance specialist",
    goal="Improve LCP, INP, and CLS for the page.",
    i=[("page", "URL or description and stack"), ("metrics", "Current Lighthouse/CWV numbers"), ("assets", "Key scripts, images, fonts")],
    s=["Identify the LCP element and what delays it.", "Find layout shift sources.", "Find long tasks hurting INP.",
       "Give fixes ranked by impact with code/config examples (image formats, preload, code splitting, font-display, caching)."],
    k=["Do not break functionality."],
    o="Diagnosis per metric, Prioritized fix list, Code examples.")

add(t="Audit accessibility", c=C, g=["a11y", "wcag", "inclusive"],
    d="WCAG 2.2 audit of markup or a UI with concrete fixes.",
    r="an accessibility specialist (CPACC/WAS level)",
    goal="Find accessibility barriers and fix them.",
    i=[("ui", "HTML/JSX or description of the interface"), ("users", "Target users and assistive tech to support")],
    s=["Check perceivable, operable, understandable, robust criteria.", "Check keyboard navigation, focus order, screen-reader names, contrast, motion, forms, errors.",
       "For each issue: WCAG criterion, severity, affected users, fix in code."],
    k=["Prefer native HTML over ARIA."],
    o="Issue table, Fixed code, Testing checklist (manual + automated).")

# ───────────────────────── AI, Prompts & Agents ─────────────────────────
C = "AI, Prompts & Agents"
add(t="Write a world-class prompt for any task", c=C, g=["prompt engineering", "meta prompt", "llm"],
    d="Meta-prompt: turn a rough idea into a complete, structured prompt for any AI model.",
    r="an expert prompt engineer who writes clear, complete, testable prompts for large language models",
    goal="Turn my rough request into a production-quality prompt that leaves nothing to guesswork.",
    i=[("task_idea", "What I want the AI to do, in my own words"), ("audience", "Who will use the output"),
       ("model", "Target model or tool, if known"), ("examples", "Any examples of good output (optional)")],
    s=["Ask me up to 5 clarifying questions if anything critical is missing; otherwise proceed.",
       "Write the prompt with these sections: Role, Context, Task, Inputs (as {{placeholders}}), Step-by-step instructions, Constraints, Output format, Quality checklist.",
       "Include 1-2 short examples if they would improve consistency.",
       "Add instructions for handling missing or ambiguous input.",
       "Add a self-check the model should run before answering.",
       "Explain briefly why each section is there and how to adapt it."],
    k=["Be explicit and specific; no vague words like 'good' or 'nice' without criteria.", "Use clear delimiters for inputs."],
    o="1. The final prompt in one fenced block\n2. Placeholder list with descriptions\n3. Tips to tune it")

add(t="Improve an existing prompt", c=C, g=["prompt engineering", "optimization", "evaluation"],
    d="Diagnose why a prompt underperforms and rewrite it.",
    r="a prompt engineer who debugs prompts using evidence",
    goal="Make the prompt produce consistently better output.",
    i=[("prompt", "The current prompt"), ("bad_outputs", "Examples of outputs that were wrong and why"), ("goal", "What a great output looks like")],
    s=["Diagnose the failure modes (ambiguity, missing context, conflicting instructions, no format, no examples).",
       "Rewrite the prompt fixing each.", "Show a diff-style list of changes and the reason for each.",
       "Propose 5 test inputs to evaluate the new prompt, including edge cases."],
    k=["Keep what already works."],
    o="Diagnosis, Improved prompt, Change log, Test set.")

add(t="Design an AI agent", c=C, g=["agents", "tools", "automation"],
    d="Design an autonomous agent: tools, loop, memory, guardrails, and evaluation.",
    r="an AI systems architect who builds reliable LLM agents",
    goal="Design an agent that completes the workflow reliably and safely.",
    i=[("workflow", "The task the agent should do end to end"), ("tools", "APIs/systems it can access"),
       ("framework", "Claude Agent SDK, LangGraph, custom, etc."), ("risk", "What actions are risky or irreversible")],
    s=["Decide whether this needs an agent or a fixed workflow, and justify.",
       "Define the tools with names, descriptions, JSON schemas, and error behaviour.",
       "Write the agent's system prompt.",
       "Design the control loop, stopping conditions, and max steps.",
       "Design memory/context management.",
       "Add guardrails: human approval for risky actions, input/output validation, permissions.",
       "Define an evaluation set and success metrics."],
    k=["Least privilege for tools.", "All irreversible actions require confirmation."],
    o="Architecture diagram (Mermaid), Tool schemas, System prompt, Loop pseudocode, Guardrails, Eval plan.")

add(t="Design a RAG system", c=C, g=["rag", "retrieval", "embeddings"],
    d="Retrieval-augmented generation design: chunking, retrieval, prompting, evaluation.",
    r="an ML engineer specializing in retrieval-augmented generation",
    goal="Design a RAG system that answers accurately with citations.",
    i=[("documents", "Document types, size, update frequency"), ("questions", "Typical user questions"), ("stack", "Vector DB, model, language preferences")],
    s=["Design ingestion: parsing, cleaning, chunking strategy (size/overlap/semantic), metadata.",
       "Choose embedding model and retrieval (hybrid search, reranking).", "Write the answer-generation prompt with citation rules and 'I don't know' behaviour.",
       "Plan evaluation: retrieval recall, answer faithfulness, relevance.", "Address freshness, access control, and cost."],
    k=["Answers must be grounded in retrieved text."],
    o="Pipeline diagram, Component choices, Prompt, Eval plan, Example code.")

add(t="Write a system prompt for a chatbot", c=C, g=["system prompt", "chatbot", "assistant"],
    d="Complete system prompt for a customer-facing or internal assistant.",
    r="a conversational AI designer",
    goal="Write a system prompt that makes the assistant helpful, on-brand, and safe.",
    i=[("product", "What the assistant is for"), ("audience", "Who talks to it"), ("tone", "Brand voice"),
       ("knowledge", "What it knows / can look up"), ("boundaries", "What it must not do; escalation rules")],
    s=["Write identity and purpose.", "Define tone with examples.", "List capabilities and tools.",
       "Define how to handle out-of-scope, sensitive, or unclear requests.", "Define escalation to humans.",
       "Define response format and length rules.", "Add 3 example exchanges."],
    k=["Never invent policies, prices, or facts; say when unsure."],
    o="System prompt in a fenced block, then a test conversation list.")

add(t="Create an LLM evaluation set", c=C, g=["evals", "testing", "llm"],
    d="Build test cases and grading rubrics to measure an AI feature.",
    r="an AI evaluation engineer",
    goal="Create an eval suite that reliably measures quality.",
    i=[("feature", "The AI feature and its prompt"), ("quality_criteria", "What good looks like")],
    s=["Define dimensions (accuracy, completeness, format, safety, tone).", "Write a scoring rubric (1-5) with anchors for each dimension.",
       "Write 20 diverse test cases: typical, edge, adversarial, and out-of-scope.", "Write an LLM-as-judge prompt with the rubric.", "Explain how to track results over time."],
    k=["Include expected outputs or key facts for each case."],
    o="Rubric table, Test cases (JSON), Judge prompt, Process notes.")

add(t="Automate a workflow with AI", c=C, g=["automation", "zapier", "n8n", "workflow"],
    d="Map a manual process and automate it with AI and integration tools.",
    r="an automation consultant",
    goal="Automate the process end to end with clear human checkpoints.",
    i=[("process", "Current manual steps"), ("tools", "Apps involved and automation platform (Zapier, Make, n8n, scripts)"), ("volume", "How often / how many")],
    s=["Map the current process and its pain points.", "Mark which steps AI can do, which rules can do, and which need a human.",
       "Design the automated flow (Mermaid) with triggers, actions, and error handling.", "Write the AI prompts used in each AI step.",
       "Estimate time saved and list risks."],
    k=["Add logging and a fallback when AI output fails validation."],
    o="Current vs. future flow, Step table, Prompts, Setup instructions, ROI estimate.")

add(t="Generate structured data from text", c=C, g=["extraction", "json", "parsing"],
    d="Extract fields from unstructured text into strict JSON.",
    r="a precise information-extraction system",
    goal="Extract the requested fields from the text into valid JSON.",
    i=[("text", "Source text"), ("schema", "JSON schema or field list with types")],
    s=["Read the full text.", "Extract each field exactly; normalize dates to ISO 8601 and numbers to plain values.",
       "Use null when a field is not present; never guess.", "Validate the result against the schema."],
    k=["Output only JSON, no commentary."],
    o="A single JSON object matching the schema.")

# ───────────────────────── Documentation ─────────────────────────
C = "Documentation"
add(t="Write a README", c=C, g=["readme", "open source", "docs"],
    d="A complete README that gets new users productive fast.",
    r="a developer-experience writer",
    goal="Write a README that explains the project and gets someone running in minutes.",
    i=[("project", "What it does, who it's for"), ("install", "Install/setup steps"), ("usage", "Key usage examples"), ("extras", "Config, contributing, license")],
    s=["One-sentence description and badges.", "Features list.", "Quick start (copy-paste commands).", "Usage examples.",
       "Configuration table.", "Troubleshooting/FAQ.", "Contributing, license."],
    k=["Every command must be copy-paste runnable.", "Short paragraphs."],
    o="README.md in Markdown.")

add(t="Document an API", c=C, g=["api docs", "openapi", "reference"],
    d="Clear reference docs with examples for every endpoint.",
    r="a technical writer for developer APIs",
    goal="Produce API reference documentation.",
    i=[("api", "Endpoints, code, or OpenAPI spec"), ("auth", "How authentication works"), ("audience", "Who integrates")],
    s=["Write overview, authentication, base URL, errors, rate limits, versioning.",
       "For each endpoint: purpose, parameters table, request example, response example, errors.",
       "Provide examples in curl and 2 languages."],
    k=["Examples must be consistent with schemas."],
    o="Markdown docs with tables and code blocks.")

add(t="Add code comments and docstrings", c=C, g=["comments", "docstrings", "jsdoc"],
    d="Document code with useful docstrings and comments in the language's standard format.",
    r="an engineer who writes helpful, concise documentation",
    goal="Add documentation that explains intent, not the obvious.",
    i=[("code", "The code"), ("format", "JSDoc, Google/NumPy docstrings, Javadoc, rustdoc, etc.")],
    s=["Add docstrings to every public function/class: purpose, params, returns, errors, example.",
       "Add inline comments only for non-obvious logic.", "Return the full code."],
    k=["Do not change code behaviour."],
    o="Full documented code.")

add(t="Write a technical design document", c=C, g=["design doc", "rfc", "spec"],
    d="A complete RFC/design doc for review.",
    r="a staff engineer writing an RFC",
    goal="Write a design doc reviewers can approve or challenge.",
    i=[("problem", "Problem and motivation"), ("proposal", "Proposed solution (rough)"), ("constraints", "Constraints, timelines, dependencies")],
    s=["Sections: Summary, Background, Goals/Non-goals, Proposal, Alternatives, Detailed design, Data/API changes, Rollout plan, Security/privacy, Observability, Risks, Open questions."],
    k=["Explicit non-goals.", "Measurable success criteria."],
    o="Markdown design doc.")

add(t="Write release notes and changelog", c=C, g=["changelog", "release notes"],
    d="Turn commits or PRs into user-friendly release notes.",
    r="a product-minded technical writer",
    goal="Write release notes users actually read.",
    i=[("changes", "Commit messages, PR titles, or diff summary"), ("version", "Version number"), ("audience", "End users, developers, or both")],
    s=["Group into: Highlights, New, Improved, Fixed, Breaking changes, Deprecations.", "Rewrite each item as a user benefit.",
       "Give migration steps for breaking changes."],
    k=["Follow Keep a Changelog and SemVer conventions."],
    o="Markdown release notes.")

add(t="Write a runbook", c=C, g=["runbook", "operations", "sop"],
    d="Step-by-step operational runbook for an alert or task.",
    r="an SRE who writes runbooks people can follow at 3 a.m.",
    goal="Write a runbook for the scenario below.",
    i=[("scenario", "Alert or operational task"), ("system", "Relevant systems and access")],
    s=["Purpose and when to use.", "Impact and severity.", "Diagnosis steps with exact commands.", "Remediation steps.", "Escalation contacts placeholders.", "Verification and follow-up."],
    k=["Numbered, imperative steps.", "Every command copy-pasteable."],
    o="Markdown runbook.")

# ───────────────────────── Writing & Content ─────────────────────────
C = "Writing & Content"
add(t="Write a blog post", c=C, g=["blog", "article", "seo"],
    d="Long-form, well-structured, engaging article on any topic.",
    r="an expert writer and editor in {{topic_field}}",
    goal="Write an original, engaging, accurate blog post.",
    i=[("topic", "Topic and angle"), ("topic_field", "Field/industry"), ("audience", "Who reads it and what they know"),
       ("length", "Target word count"), ("tone", "Tone of voice"), ("keyword", "Primary SEO keyword (optional)")],
    s=["Propose 5 headline options and pick the strongest.", "Outline with H2/H3 headings.",
       "Write a hook intro that states the reader's problem.", "Write the body with concrete examples, data points (flag ones to verify), and actionable advice.",
       "Conclude with a summary and a call to action.", "Add a meta description (155 chars) and 3 social snippets."],
    k=["No filler, no clichés.", "Short paragraphs, varied sentence length.", "Flag any claim that needs a source."],
    o="Headline, Meta description, Article in Markdown, Social snippets.")

add(t="Edit and improve writing", c=C, g=["editing", "proofreading", "clarity"],
    d="Professional edit for clarity, flow, grammar, and impact.",
    r="a senior editor",
    goal="Improve the text while keeping the author's voice and meaning.",
    i=[("text", "Text to edit"), ("goal", "Purpose and audience"), ("level", "Light proofread, line edit, or heavy rewrite")],
    s=["Fix grammar, spelling, punctuation.", "Improve clarity and concision.", "Improve structure and flow.", "Return the edited text.", "List the most important changes and why."],
    k=["Preserve meaning and voice."],
    o="Edited text, then a bullet list of key changes.")

add(t="Summarize any document", c=C, g=["summary", "tl;dr", "notes"],
    d="Accurate, layered summary with key points and action items.",
    r="an analyst who writes precise summaries",
    goal="Summarize the content so a busy reader gets everything important.",
    i=[("content", "Text to summarize"), ("audience", "Who will read the summary"), ("length", "Target length")],
    s=["One-sentence TL;DR.", "Key points (5-10 bullets).", "Important numbers, dates, names.", "Decisions and action items with owners if mentioned.", "Open questions or gaps."],
    k=["No information not in the source.", "Keep numbers exact."],
    o="TL;DR, Key points, Facts, Actions, Open questions.")

add(t="Write a professional email", c=C, g=["email", "communication", "business"],
    d="Clear, well-toned email for any situation.",
    r="a skilled business communicator",
    goal="Write an email that gets the desired response.",
    i=[("recipient", "Who and relationship"), ("purpose", "What you need"), ("context", "Background"), ("tone", "Formal, friendly, firm, apologetic")],
    s=["Write a specific subject line.", "Open with the point.", "Give necessary context briefly.", "Make a clear ask with deadline if any.", "Close politely.", "Provide a shorter alternative version."],
    k=["Under 200 words unless needed."],
    o="Subject, Email, Short version.")

add(t="Write a story or fiction scene", c=C, g=["fiction", "creative writing", "story"],
    d="Creative story with vivid characters, conflict, and a strong ending.",
    r="an award-winning fiction author",
    goal="Write an original story.",
    i=[("premise", "Premise or idea"), ("genre", "Genre"), ("length", "Word count"), ("pov", "Point of view and tense"), ("audience", "Age group")],
    s=["Define character goals and conflict.", "Open in the middle of action.", "Show, don't tell; use sensory detail.", "Build tension to a climax.", "End with a resonant resolution."],
    k=["Original content; avoid clichés."],
    o="Title and the story.")

add(t="Repurpose content across formats", c=C, g=["repurpose", "social", "newsletter"],
    d="Turn one piece of content into posts, threads, newsletter, and video script.",
    r="a content strategist",
    goal="Repurpose the content for multiple channels.",
    i=[("content", "Original content"), ("channels", "Target channels"), ("brand_voice", "Voice description")],
    s=["Extract the core message and 5 key insights.", "Create a version per channel following its format norms and length limits."],
    k=["Each piece stands alone."],
    o="Section per channel with ready-to-post copy.")

add(t="Write a speech or presentation script", c=C, g=["speech", "presentation", "public speaking"],
    d="Memorable talk script with structure, stories, and timing.",
    r="a speechwriter",
    goal="Write a speech that informs and moves the audience.",
    i=[("topic", "Topic and key message"), ("audience", "Audience"), ("duration", "Length in minutes"), ("occasion", "Event")],
    s=["Hook opening.", "Three main points with a story or example each.", "Transitions.", "Strong close with a call to action.", "Mark pauses and estimated timing."],
    k=["About 130 words per minute."],
    o="Script with timing marks, then slide outline.")

# ───────────────────────── Marketing & SEO ─────────────────────────
C = "Marketing & SEO"
add(t="Create a marketing strategy", c=C, g=["strategy", "go-to-market", "growth"],
    d="Full marketing plan: audience, positioning, channels, budget, KPIs.",
    r="a CMO with experience in {{industry}}",
    goal="Build a marketing strategy that hits the goal.",
    i=[("product", "Product/service"), ("industry", "Industry"), ("audience", "Target customers"), ("goal", "Goal and timeframe"), ("budget", "Budget")],
    s=["Define ICP and personas.", "Write positioning statement and value proposition.", "Analyse 3 competitors.",
       "Select channels and justify.", "Build a 90-day plan with milestones.", "Allocate budget.", "Define KPIs and measurement."],
    k=["Recommendations must fit the budget."],
    o="Strategy doc with tables.")

add(t="Write high-converting landing page copy", c=C, g=["copywriting", "landing page", "conversion"],
    d="Full landing page copy from hero to FAQ.",
    r="a direct-response copywriter",
    goal="Write landing page copy that converts the target visitor.",
    i=[("product", "Product and key features"), ("audience", "Who visits and their pain"), ("offer", "Offer/CTA"), ("proof", "Testimonials, stats, logos")],
    s=["Hero: headline, subheadline, CTA (3 variants).", "Problem section.", "Solution and benefits (benefits over features).",
       "How it works (3 steps).", "Social proof.", "Objection handling.", "FAQ.", "Final CTA."],
    k=["Specific, concrete language.", "No unverifiable claims."],
    o="Section-by-section copy.")

add(t="SEO keyword and content plan", c=C, g=["seo", "keywords", "content plan"],
    d="Keyword clusters and a content calendar to rank.",
    r="an SEO strategist",
    goal="Build an SEO content plan.",
    i=[("site", "Site/niche"), ("audience", "Audience"), ("seed_keywords", "Seed keywords"), ("competitors", "Competitor sites")],
    s=["Group keywords into topic clusters with search intent.", "Define pillar and supporting pages.", "Prioritize by intent, difficulty, and business value.",
       "Create a 3-month content calendar.", "Give on-page SEO guidelines."],
    k=["Note that volumes must be verified in an SEO tool."],
    o="Cluster table, Calendar, On-page checklist.")

add(t="Write ad copy variations", c=C, g=["ads", "ppc", "facebook ads", "google ads"],
    d="Multiple ad variants per platform for testing.",
    r="a performance marketer",
    goal="Write ads to test.",
    i=[("product", "Product and offer"), ("platform", "Google, Meta, LinkedIn, TikTok"), ("audience", "Target audience")],
    s=["Write 5 variants each with a different angle (pain, benefit, social proof, urgency, curiosity).", "Respect each platform's character limits.", "Suggest visuals for each."],
    k=["Follow platform ad policies."],
    o="Table of variants with angle, headline, body, CTA, visual idea.")

add(t="Social media content calendar", c=C, g=["social media", "calendar", "posts"],
    d="A month of posts with copy, hashtags, and formats.",
    r="a social media manager",
    goal="Create a content calendar that grows engagement.",
    i=[("brand", "Brand and voice"), ("platforms", "Platforms"), ("goals", "Goals"), ("frequency", "Posts per week")],
    s=["Define content pillars.", "Plan posts per day with format, copy, hashtags, and visual idea.", "Include engagement prompts."],
    k=["Platform-native formats."],
    o="Calendar table.")

add(t="Write an email marketing sequence", c=C, g=["email marketing", "nurture", "drip"],
    d="Onboarding/nurture/sales email sequence.",
    r="an email marketing specialist",
    goal="Write a sequence that moves readers to the goal.",
    i=[("goal", "Sequence goal"), ("audience", "Audience"), ("emails", "Number of emails and timing"), ("product", "Product/offer")],
    s=["Plan the sequence arc.", "For each email: purpose, send day, subject (2 options), preview text, body, CTA."],
    k=["One CTA per email."],
    o="Sequence overview, then each email.")

# ───────────────────────── Sales & Customer Success ─────────────────────────
C = "Sales & Customer Support"
add(t="Write a cold outreach sequence", c=C, g=["outbound", "cold email", "prospecting"],
    d="Personalized multi-touch outreach that books meetings.",
    r="a top-performing SDR",
    goal="Write outreach that earns a reply.",
    i=[("product", "Product and value"), ("prospect", "Prospect role, company, and any personalization"), ("channels", "Email, LinkedIn, call")],
    s=["Write 4 touches over 2 weeks.", "Personalize the opening.", "Lead with their problem.", "Soft, specific CTA.", "Include a call script for the phone touch."],
    k=["Under 120 words per email.", "No fake familiarity."],
    o="Touch-by-touch messages.")

add(t="Handle a sales objection", c=C, g=["objections", "negotiation"],
    d="Responses to common objections with reasoning.",
    r="a sales coach",
    goal="Prepare strong responses to objections.",
    i=[("product", "Product"), ("objections", "Objections heard")],
    s=["For each: underlying concern, clarifying question, response, proof point."],
    k=["Honest; no pressure tactics."],
    o="Objection table.")

add(t="Respond to a customer support ticket", c=C, g=["support", "customer service", "ticket"],
    d="Empathetic, accurate, complete support reply.",
    r="a senior customer support specialist",
    goal="Resolve the customer's issue in one reply.",
    i=[("ticket", "Customer message"), ("knowledge", "Relevant policy, docs, account info"), ("tone", "Brand tone")],
    s=["Acknowledge the issue specifically.", "Answer or give steps to resolve.", "Set expectations on timelines.", "Offer next step."],
    k=["Never promise what policy does not allow.", "Never blame the customer."],
    o="Reply text, plus internal note on any follow-up.")

add(t="Create a support knowledge base article", c=C, g=["help center", "faq", "kb"],
    d="Self-service help article that reduces tickets.",
    r="a support content writer",
    goal="Write a help article that solves the problem without contacting support.",
    i=[("issue", "Problem users face"), ("solution", "How to solve it")],
    s=["Clear title as a question or task.", "Short intro.", "Numbered steps with UI labels in bold.", "Troubleshooting.", "Related articles."],
    k=["Plain language, 8th-grade reading level."],
    o="Markdown article.")

add(t="Write a sales proposal", c=C, g=["proposal", "rfp", "deal"],
    d="Persuasive proposal tailored to the client.",
    r="an enterprise account executive",
    goal="Write a proposal that wins the deal.",
    i=[("client", "Client and needs"), ("solution", "What you offer"), ("pricing", "Pricing"), ("timeline", "Timeline")],
    s=["Executive summary.", "Understanding of needs.", "Proposed solution.", "Deliverables and timeline.", "Pricing options.", "Why us.", "Next steps."],
    k=["Client-focused language."],
    o="Proposal document in Markdown.")

# ───────────────────────── Business & Strategy ─────────────────────────
C = "Business & Strategy"
add(t="Write a business plan", c=C, g=["business plan", "startup", "planning"],
    d="Complete business plan with market, model, and financials.",
    r="a startup advisor and former founder",
    goal="Write a business plan for investors or a bank.",
    i=[("business", "Business idea"), ("market", "Target market"), ("stage", "Current stage"), ("ask", "Funding ask (if any)")],
    s=["Executive summary.", "Problem and solution.", "Market size (TAM/SAM/SOM with method).", "Competition.", "Business model.",
       "Go-to-market.", "Operations and team.", "3-year financial projections with assumptions.", "Risks.", "Funding use."],
    k=["State assumptions behind every number."],
    o="Business plan document with tables.")

add(t="SWOT and competitive analysis", c=C, g=["swot", "competitors", "analysis"],
    d="Structured SWOT plus competitor comparison and strategic moves.",
    r="a strategy consultant",
    goal="Analyse the company's position and recommend moves.",
    i=[("company", "Company and offering"), ("competitors", "Competitors"), ("market", "Market context")],
    s=["SWOT with specific points.", "Competitor comparison table.", "TOWS strategies (SO, WO, ST, WT).", "Top 3 recommendations."],
    k=["Specific, not generic."],
    o="SWOT grid, comparison table, strategies, recommendations.")

add(t="Build a financial model", c=C, g=["finance", "forecast", "unit economics"],
    d="Revenue/cost model with assumptions and scenarios.",
    r="an FP&A analyst",
    goal="Build a financial model structure and calculations.",
    i=[("business_model", "How the business makes money"), ("assumptions", "Known numbers"), ("horizon", "Time horizon")],
    s=["List assumptions as inputs.", "Build revenue, COGS, opex, and cash flow logic.", "Calculate unit economics (CAC, LTV, payback, margins).",
       "Create base/best/worst scenarios.", "Provide spreadsheet layout and formulas."],
    k=["Separate inputs from calculations."],
    o="Assumptions table, model structure, formulas, scenario summary.")

add(t="Prepare for a decision", c=C, g=["decision making", "trade-offs"],
    d="Structured decision analysis with options and a recommendation.",
    r="a decision analyst",
    goal="Help make a well-reasoned decision.",
    i=[("decision", "The decision"), ("options", "Options"), ("criteria", "What matters")],
    s=["Clarify the decision and its reversibility.", "Weighted criteria matrix.", "Pre-mortem for top option.", "Recommendation and what would change it."],
    k=["Highlight uncertainty."],
    o="Matrix, analysis, recommendation.")

add(t="Write meeting agenda and notes", c=C, g=["meetings", "agenda", "minutes"],
    d="Agenda before, structured minutes after.",
    r="an efficient chief of staff",
    goal="Make the meeting productive.",
    i=[("purpose", "Meeting purpose"), ("attendees", "Attendees"), ("transcript_or_notes", "Raw notes or transcript (for minutes)")],
    s=["Agenda: objective, topics with timeboxes and owners, pre-reads.", "Minutes: decisions, action items (owner, due date), open issues, summary."],
    k=["Action items must have owners."],
    o="Agenda and/or minutes in Markdown.")

add(t="Write OKRs", c=C, g=["okrs", "goals", "planning"],
    d="Ambitious, measurable objectives and key results.",
    r="an OKR coach",
    goal="Write OKRs for the team.",
    i=[("team", "Team and mission"), ("priorities", "Priorities for the period"), ("baseline", "Current metrics")],
    s=["2-4 objectives, qualitative and inspiring.", "2-4 key results each, measurable with baseline and target.", "Initiatives for each KR."],
    k=["KRs measure outcomes, not tasks."],
    o="OKR table.")

# ───────────────────────── Product Management ─────────────────────────
C = "Product Management"
add(t="Write a product requirements document (PRD)", c=C, g=["prd", "requirements", "spec"],
    d="Complete PRD with problem, users, requirements, and metrics.",
    r="a senior product manager",
    goal="Write a PRD engineering and design can build from.",
    i=[("feature", "Feature idea"), ("users", "Target users"), ("problem", "Problem and evidence"), ("constraints", "Constraints and timeline")],
    s=["Problem statement and evidence.", "Goals and non-goals.", "Personas and user stories with acceptance criteria.", "Functional and non-functional requirements.",
       "UX flow.", "Success metrics.", "Launch plan.", "Risks and open questions."],
    k=["Testable acceptance criteria (Given/When/Then)."],
    o="PRD in Markdown.")

add(t="Write user stories", c=C, g=["agile", "user stories", "backlog"],
    d="INVEST user stories with acceptance criteria.",
    r="an agile product owner",
    goal="Break the feature into user stories.",
    i=[("feature", "Feature"), ("users", "User types")],
    s=["Write stories as 'As a ..., I want ..., so that ...'.", "Add Given/When/Then acceptance criteria.", "Estimate relative size.", "Order by priority."],
    k=["Stories must be independent and small."],
    o="Story table.")

add(t="Prioritize a backlog", c=C, g=["prioritization", "rice", "roadmap"],
    d="Score and rank features with RICE or similar.",
    r="a product strategist",
    goal="Rank the backlog by value.",
    i=[("items", "Features/ideas"), ("goals", "Business goals"), ("data", "Reach/impact data if any")],
    s=["Score with RICE (Reach, Impact, Confidence, Effort).", "Rank and group into Now/Next/Later.", "Explain top choices."],
    k=["State assumptions behind scores."],
    o="Scoring table and roadmap.")

add(t="Analyze user feedback", c=C, g=["feedback", "voice of customer", "insights"],
    d="Find themes and priorities in raw feedback.",
    r="a user research analyst",
    goal="Turn feedback into actionable insights.",
    i=[("feedback", "Raw feedback, reviews, survey answers")],
    s=["Code feedback into themes.", "Count frequency and sentiment per theme.", "Quote representative examples.", "Recommend actions ranked by impact."],
    k=["Quotes verbatim."],
    o="Theme table, quotes, recommendations.")

# ───────────────────────── Research & Analysis ─────────────────────────
C = "Research & Analysis"
add(t="Deep research on a topic", c=C, g=["research", "report", "analysis"],
    d="Thorough, balanced research report with sources to verify.",
    r="a research analyst",
    goal="Produce a comprehensive, balanced report on the topic.",
    i=[("topic", "Topic or question"), ("depth", "Depth and length"), ("audience", "Audience")],
    s=["Define scope and key questions.", "Background.", "Main findings by subtopic.", "Competing views and evidence.", "Gaps and uncertainties.", "Conclusions.", "Sources/what to verify."],
    k=["Separate facts from opinions.", "Flag uncertain claims; never invent citations."],
    o="Structured report.")

add(t="Analyze a research paper", c=C, g=["paper", "academic", "critique"],
    d="Summary and critique of an academic paper.",
    r="a peer reviewer in {{field}}",
    goal="Explain and critically evaluate the paper.",
    i=[("paper", "Paper text or abstract"), ("field", "Field")],
    s=["Summarize question, method, results.", "Evaluate methodology and validity.", "Note limitations.", "Explain significance.", "Suggest follow-up research."],
    k=["Fair and evidence-based."],
    o="Summary, critique, significance, questions.")

add(t="Literature review", c=C, g=["literature", "academic", "synthesis"],
    d="Synthesize research on a topic into themes and gaps.",
    r="an academic researcher",
    goal="Write a literature review structure and synthesis.",
    i=[("topic", "Research topic"), ("sources", "Papers or notes provided")],
    s=["Group sources by theme.", "Compare findings.", "Identify gaps.", "Suggest research questions."],
    k=["Only cite provided sources."],
    o="Review in academic style.")

add(t="Market research", c=C, g=["market", "trends", "sizing"],
    d="Market overview, sizing, trends, and opportunities.",
    r="a market research consultant",
    goal="Assess the market opportunity.",
    i=[("market", "Market/industry"), ("geography", "Region"), ("purpose", "Why you need it")],
    s=["Define market.", "Size with top-down and bottom-up methods.", "Key players.", "Trends and drivers.", "Customer segments.", "Opportunities and threats."],
    k=["Mark estimates and their basis."],
    o="Report with tables.")

add(t="Survey and questionnaire design", c=C, g=["survey", "questionnaire", "research"],
    d="Unbiased survey that answers your research question.",
    r="a survey methodologist",
    goal="Design a survey that yields valid data.",
    i=[("objective", "Research objective"), ("audience", "Respondents"), ("length", "Max time to complete")],
    s=["Define what to measure.", "Write neutral questions with correct scale types.", "Order questions logically.", "Avoid leading/double-barreled questions.", "Plan analysis."],
    k=["Keep within the time limit."],
    o="Survey questions with types and options.")

# ───────────────────────── Education & Learning ─────────────────────────
C = "Education & Learning"
add(t="Explain a concept at any level", c=C, g=["explain", "learning", "eli5"],
    d="Layered explanation from simple to expert with examples.",
    r="a world-class teacher",
    goal="Make the concept truly understood.",
    i=[("concept", "Concept"), ("level", "Learner's level"), ("context", "Why they're learning it")],
    s=["One-sentence definition.", "Analogy.", "Step-by-step explanation.", "Worked example.", "Common misconceptions.", "Check-for-understanding questions with answers."],
    k=["Build from what the learner already knows."],
    o="Structured explanation.")

add(t="Create a learning roadmap", c=C, g=["roadmap", "curriculum", "self-study"],
    d="Week-by-week plan to learn a skill with resources and projects.",
    r="a learning designer and mentor",
    goal="Create a roadmap to reach the goal.",
    i=[("skill", "Skill"), ("current_level", "Current level"), ("goal", "Goal"), ("time", "Hours per week and deadline")],
    s=["Break into phases and milestones.", "Weekly topics.", "Practice projects.", "Resource types.", "Self-assessment checkpoints."],
    k=["Realistic for the time available."],
    o="Roadmap table.")

add(t="Create a lesson plan", c=C, g=["teaching", "lesson plan", "classroom"],
    d="Complete lesson plan with objectives, activities, and assessment.",
    r="an experienced teacher",
    goal="Plan an engaging lesson.",
    i=[("subject", "Subject and topic"), ("grade", "Grade/level"), ("duration", "Duration")],
    s=["Learning objectives (Bloom's).", "Materials.", "Warm-up.", "Instruction.", "Guided and independent practice.", "Assessment.", "Differentiation."],
    k=["Timed sections."],
    o="Lesson plan.")

add(t="Generate quiz and practice questions", c=C, g=["quiz", "assessment", "flashcards"],
    d="Questions of varied type and difficulty with answers.",
    r="an assessment designer",
    goal="Create questions that test real understanding.",
    i=[("material", "Material or topic"), ("count", "Number of questions"), ("types", "MCQ, short answer, coding, etc.")],
    s=["Mix difficulty levels.", "Plausible distractors.", "Answer key with explanations."],
    k=["One correct answer per MCQ."],
    o="Questions, then answer key.")

add(t="Socratic tutor", c=C, g=["tutor", "socratic", "practice"],
    d="Learn by guided questioning instead of answers.",
    r="a Socratic tutor",
    goal="Guide me to understand {{topic}} through questions.",
    i=[("topic", "Topic"), ("level", "My level")],
    s=["Ask one question at a time.", "Wait for my answer.", "Give hints, not answers, when I'm stuck.", "Summarize what I learned at the end."],
    k=["Never give the full answer unless I ask twice."],
    o="Conversational, one question per turn.")

# ───────────────────────── Design & UX ─────────────────────────
C = "Design & UX"
add(t="UX review of a screen or flow", c=C, g=["ux", "heuristics", "usability"],
    d="Heuristic evaluation with prioritized fixes.",
    r="a senior UX designer",
    goal="Identify usability problems and solutions.",
    i=[("ui", "Screen/flow description or screenshot"), ("users", "Users and goals")],
    s=["Evaluate against Nielsen's 10 heuristics.", "List issues with severity.", "Suggest concrete fixes.", "Note what works well."],
    k=["User-centred reasoning."],
    o="Issues table, recommendations.")

add(t="Create user personas", c=C, g=["personas", "research", "users"],
    d="Evidence-based personas with goals and pains.",
    r="a UX researcher",
    goal="Create personas for the product.",
    i=[("product", "Product"), ("research", "Research data available")],
    s=["Create 3 personas: name, role, goals, frustrations, behaviours, quote, scenario."],
    k=["Base on provided data; mark assumptions."],
    o="Persona cards.")

add(t="Write UX microcopy", c=C, g=["microcopy", "ux writing", "ui text"],
    d="Buttons, errors, empty states, and onboarding text.",
    r="a UX writer",
    goal="Write clear, helpful interface text.",
    i=[("screens", "Screens/states"), ("voice", "Voice and tone")],
    s=["Write text per element.", "Errors: what happened + how to fix.", "Empty states with a next action.", "Give 2 options for key strings."],
    k=["Concise, action-oriented."],
    o="Table: element, copy, notes.")

add(t="Create a design system spec", c=C, g=["design system", "tokens", "components"],
    d="Tokens, typography, components, and usage rules.",
    r="a design systems lead",
    goal="Define a design system foundation.",
    i=[("brand", "Brand attributes"), ("platforms", "Platforms")],
    s=["Color tokens (light/dark) with contrast checks.", "Type scale.", "Spacing scale.", "Core component specs.", "Usage guidelines."],
    k=["WCAG AA contrast."],
    o="Spec document with token tables.")

# ───────────────────────── Image, Video & Audio Generation ─────────────────────────
C = "Image, Video & Audio"
add(t="Image generation prompt", c=C, g=["midjourney", "dall-e", "stable diffusion", "image"],
    d="Detailed prompt for AI image generators.",
    r="an expert AI art director",
    goal="Write image prompts that produce exactly the intended image.",
    i=[("idea", "What the image shows"), ("style", "Style (photo, illustration, 3D, etc.)"), ("tool", "Midjourney, DALL-E, Stable Diffusion, Flux, etc."), ("aspect", "Aspect ratio")],
    s=["Describe subject, action, setting, composition, camera/lens, lighting, color palette, mood, style references, and detail level.",
       "Add tool-specific parameters.", "Give a negative prompt if supported.", "Give 3 variations."],
    k=["No living artists' names or trademarks unless permitted."],
    o="Main prompt, negative prompt, variations.")

add(t="Video script and storyboard", c=C, g=["video", "youtube", "storyboard"],
    d="Script with shots, visuals, and timing.",
    r="a video producer",
    goal="Create a script and storyboard.",
    i=[("topic", "Topic"), ("platform", "YouTube, TikTok, Reels, ad"), ("length", "Length")],
    s=["Hook in first 3 seconds.", "Shot list with visuals, voiceover, on-screen text, duration.", "CTA."],
    k=["Fits platform norms."],
    o="Table: time, visual, audio, text.")

add(t="AI video generation prompt", c=C, g=["sora", "runway", "veo", "video ai"],
    d="Prompt for text-to-video models with camera and motion detail.",
    r="a cinematographer writing for AI video models",
    goal="Write a video prompt.",
    i=[("scene", "Scene"), ("duration", "Duration"), ("style", "Style")],
    s=["Describe subject, action, environment, camera movement, lens, lighting, pacing, and mood.", "Give 2 variations."],
    k=["One continuous shot per prompt unless the tool supports cuts."],
    o="Prompts.")

add(t="Podcast episode plan", c=C, g=["podcast", "audio", "interview"],
    d="Episode outline, interview questions, and show notes.",
    r="a podcast producer",
    goal="Plan an episode.",
    i=[("topic", "Topic"), ("guest", "Guest (if any)"), ("length", "Length")],
    s=["Outline segments with timing.", "Interview questions.", "Intro/outro script.", "Show notes and title options."],
    k=["Conversational."],
    o="Episode plan.")

# ───────────────────────── Career & Hiring ─────────────────────────
C = "Career & Hiring"
add(t="Tailor a resume to a job", c=C, g=["resume", "cv", "job search"],
    d="Rewrite resume bullets to match a job description.",
    r="a career coach and technical recruiter",
    goal="Tailor the resume for this job.",
    i=[("resume", "Current resume"), ("job_description", "Job posting")],
    s=["Extract key requirements and keywords.", "Map resume experience to them.", "Rewrite bullets as achievement + metric.", "Suggest gaps to address.", "ATS-friendly formatting."],
    k=["Never invent experience."],
    o="Match analysis, revised resume, gap list.")

add(t="Interview preparation", c=C, g=["interview", "behavioral", "technical"],
    d="Likely questions with strong STAR answers.",
    r="an interview coach",
    goal="Prepare me for the interview.",
    i=[("role", "Role and company"), ("background", "My background")],
    s=["List likely behavioural, technical, and role-specific questions.", "Draft STAR answers from my background.", "Questions to ask them.", "Mock interview mode: ask one at a time and give feedback."],
    k=["Honest answers based on my real experience."],
    o="Question bank, answers, my questions.")

add(t="Write a job description", c=C, g=["hiring", "jd", "recruiting"],
    d="Inclusive, accurate job description.",
    r="a talent acquisition lead",
    goal="Write a job description that attracts the right candidates.",
    i=[("role", "Role"), ("team", "Team and company"), ("requirements", "Must-haves and nice-to-haves"), ("comp", "Compensation and location")],
    s=["Role summary.", "Responsibilities.", "Must-haves vs. nice-to-haves.", "Benefits.", "Hiring process."],
    k=["Inclusive language; no unnecessary requirements."],
    o="Job description.")

add(t="Create interview questions and rubric", c=C, g=["hiring", "rubric", "interviewing"],
    d="Structured interview with scoring rubric.",
    r="a hiring manager trained in structured interviewing",
    goal="Create a fair, structured interview.",
    i=[("role", "Role"), ("competencies", "Competencies to assess")],
    s=["Questions per competency.", "What good/average/poor looks like.", "Scoring 1-4."],
    k=["Job-related questions only."],
    o="Interview guide with rubric.")

# ───────────────────────── Productivity & Personal ─────────────────────────
C = "Productivity & Personal"
add(t="Plan a project", c=C, g=["project plan", "timeline", "tasks"],
    d="Work breakdown, timeline, risks, and owners.",
    r="a certified project manager",
    goal="Create an executable project plan.",
    i=[("project", "Project and goal"), ("deadline", "Deadline"), ("team", "Team/resources")],
    s=["Work breakdown structure.", "Dependencies.", "Timeline (Gantt in Mermaid).", "RACI.", "Risks and mitigations.", "Milestones."],
    k=["Realistic estimates with buffer."],
    o="Plan with tables and Gantt.")

add(t="Prioritize my tasks", c=C, g=["prioritization", "eisenhower", "focus"],
    d="Turn a messy task list into a focused plan.",
    r="a productivity coach",
    goal="Organize tasks into a realistic plan.",
    i=[("tasks", "Task list"), ("time", "Available time"), ("goals", "Goals")],
    s=["Classify with the Eisenhower matrix.", "Estimate time.", "Schedule into time blocks.", "Suggest what to delegate or drop."],
    k=["Fit within available time."],
    o="Matrix and schedule.")

add(t="Brainstorm ideas", c=C, g=["brainstorm", "ideas", "creativity"],
    d="Many diverse ideas, then the best ones developed.",
    r="a creative strategist",
    goal="Generate and evaluate ideas.",
    i=[("challenge", "Challenge"), ("constraints", "Constraints")],
    s=["Generate 20 ideas across different angles (safe, bold, cheap, tech-driven, unconventional).", "Score on impact/feasibility.", "Develop the top 3 with next steps."],
    k=["Quantity before judgement."],
    o="Idea list, scoring, top 3.")

add(t="Make a decision checklist", c=C, g=["checklist", "process", "sop"],
    d="Create a reusable checklist or SOP for any recurring task.",
    r="an operations expert",
    goal="Create a checklist that prevents mistakes.",
    i=[("task", "Recurring task"), ("mistakes", "Common mistakes")],
    s=["Break into ordered steps.", "Add verification points.", "Add 'don't forget' items."],
    k=["Short items, imperative verbs."],
    o="Checklist.")

# ───────────────────────── Language & Translation ─────────────────────────
C = "Language & Translation"
add(t="Translate with cultural adaptation", c=C, g=["translation", "localization", "i18n"],
    d="Natural, culturally adapted translation, not word for word.",
    r="a professional translator and localization expert for {{target_language}}",
    goal="Translate so it reads as if written natively.",
    i=[("text", "Text"), ("source_language", "Source language"), ("target_language", "Target language and region"), ("context", "Purpose and audience")],
    s=["Translate meaning, tone, and intent.", "Adapt idioms, units, dates, currency.", "Keep placeholders/code unchanged.", "List adaptation notes."],
    k=["Preserve formatting."],
    o="Translation, then notes.")

add(t="Localize a software product", c=C, g=["i18n", "l10n", "strings"],
    d="Translate UI strings with context and plural rules.",
    r="a software localization engineer",
    goal="Localize the strings file.",
    i=[("strings", "Strings file (JSON, .po, .strings, XML)"), ("target_language", "Target locale")],
    s=["Translate each string.", "Respect plural/gender rules and ICU syntax.", "Keep keys and placeholders.", "Flag strings likely to overflow UI."],
    k=["Output must be valid in the same format."],
    o="Localized file.")

add(t="Language practice partner", c=C, g=["language learning", "conversation"],
    d="Conversation practice with corrections.",
    r="a friendly native-speaker language tutor",
    goal="Help me practise {{language}}.",
    i=[("language", "Language"), ("level", "CEFR level"), ("topic", "Topic")],
    s=["Converse at my level.", "After each reply, correct my mistakes briefly.", "Introduce 3 new words per session."],
    k=["Mostly in the target language."],
    o="Conversation with corrections.")

# ───────────────────────── Finance & Legal (informational) ─────────────────────────
C = "Finance & Legal"
add(t="Explain a contract", c=C, g=["contract", "legal", "review"],
    d="Plain-language explanation of a contract and its risks.",
    r="a contracts analyst (not a lawyer; informational only)",
    goal="Explain the contract so I understand what I'm agreeing to.",
    i=[("contract", "Contract text"), ("my_role", "Which party I am")],
    s=["Summary of what it does.", "Key obligations for each party.", "Payment, term, termination, liability, IP, confidentiality.", "Unusual or risky clauses.", "Questions to ask a lawyer."],
    k=["Informational, not legal advice."],
    o="Summary, clause table, risks, questions.")

add(t="Draft a privacy policy or terms outline", c=C, g=["privacy", "terms", "compliance"],
    d="First-draft outline to review with counsel.",
    r="a compliance specialist",
    goal="Draft an outline for review.",
    i=[("product", "Product and data collected"), ("jurisdictions", "Jurisdictions (GDPR, CCPA, etc.)")],
    s=["Sections required by the jurisdictions.", "Plain-language draft of each.", "List items needing legal review."],
    k=["Mark as draft for legal review."],
    o="Draft document.")

add(t="Personal budget plan", c=C, g=["budget", "personal finance", "saving"],
    d="Monthly budget with savings goals.",
    r="a financial planner (informational only)",
    goal="Build a realistic budget.",
    i=[("income", "Monthly income"), ("expenses", "Expenses"), ("goals", "Goals")],
    s=["Categorize expenses.", "Apply a framework (50/30/20 or zero-based).", "Find savings opportunities.", "Plan toward goals."],
    k=["Not financial advice."],
    o="Budget table and plan.")

add(t="Analyze financial statements", c=C, g=["financial analysis", "ratios", "investing"],
    d="Ratio analysis and health check of a company.",
    r="a financial analyst",
    goal="Assess the company's financial health.",
    i=[("statements", "Income statement, balance sheet, cash flow")],
    s=["Calculate profitability, liquidity, leverage, efficiency ratios.", "Trends.", "Red flags.", "Summary."],
    k=["Show formulas."],
    o="Ratio table and analysis.")

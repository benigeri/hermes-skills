# Choosing the Hermes owner

Read current official Hermes documentation and inspect the relevant live state first. These are options, not a rigid ladder: choose the simplest documented owner that fully enforces the behavior.

## Decision guide

- **Identity, voice, and standing interaction style:** `SOUL.md`; use a temporary personality overlay only for a temporary session need.
- **Durable user facts:** `USER.md` or `MEMORY.md`, following the active memory workflow.
- **Project-local rules:** `AGENTS.md` or `.hermes.md`.
- **Reusable judgment or procedure:** patch an existing class-level skill, or create a new class-level skill when it gives the task one clear canonical home. Keep always-on rules in `SKILL.md`; put optional depth in a small topical `references/` set.
- **Platform settings and built-in controls:** Hermes configuration, toolsets, approval gates, skill config, provider settings, memory settings, browser settings, and other documented options.
- **Long-lived separate agent:** a profile with its own identity and state. Create it from scratch and add only the skills, tools, credentials, memory, routes, jobs, model defaults, and working directory it needs.
- **Work ownership and steering:** profile routing, Kanban for tracked one-shot work, or Bot Chat for live cumulative steering.
- **Schedules and events:** cron for time-based work; webhooks for external events; event-triggered cron when an event should launch an existing routine.
- **External capabilities:** built-in tools, managed connections, or MCP servers with narrow exposure.
- **Hermes extension point:** a plugin or hook for tools, commands, platform adapters, providers, memory or context engines, UI surfaces, or bundled behavior.
- **Missing native capability:** inspect an available Hermes update and restart plan through the current documented path, after stating any local side effects that path may have. Do not update or restart without separate approval.
- **Custom tool or service:** use only for a proved gap that the supported options above do not solve; keep it bounded and removable.
- **Hermes core patch:** last resort, with focused tests, rollback, an upstream path when practical, and a removal trigger.

## Reject the plan when

- it chooses an implementation before inspecting current documentation and live setup;
- two places become the canonical owner for one rule;
- a script contains judgment, approvals, routing policy, or a hidden queue;
- a new profile is only branding, a temporary model choice, or supposed operating-system isolation;
- a broad profile is cloned instead of building the least-needed profile from scratch;
- a plugin is rejected merely because it contains code, or chosen when configuration, MCP, or a built-in extension already owns the requirement more simply;
- success is inferred from process state rather than the real consumer result; or
- a standing behavior change has no rollback or timed one-time follow-up check.

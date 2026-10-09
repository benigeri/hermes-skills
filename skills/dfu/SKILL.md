---
{
  "name": "dfu",
  "description": "Audit Hermes changes: DFU, don't fuck up, don't fuck it up.",
  "version": "1.0.0",
  "author": "benigeri",
  "license": "MIT",
  "metadata": {
    "hermes": {
      "tags": ["hermes", "architecture", "review", "skills", "profiles", "configuration", "plugins"]
    }
  }
}
---

# DFU — Don't Fuck It Up

Audit a lasting Hermes change before it ships. DFU is a review method and skill, not a separate profile.

## When to use

Treat **DFU**, **don't fuck up**, and **don't fuck it up** as the same call. Load DFU before proposing, implementing, or auditing a lasting change to skills, context files, configuration, tools, profiles, routing, Kanban, Bot Chat, cron, webhooks, memory, MCP, plugins, updates, write authority, or Hermes core code.

Keep the review read-only unless the requester separately authorizes implementation. An available update, restart plan, plugin, profile design, or code patch is not approval to install, restart, create, or publish it.

Use verified organization or project policy when one exists. Otherwise use the defaults in `references/recommended-policies.md`. Local policy may strengthen the defaults; weakening a safety boundary requires explicit approval from the policy owner.

## Seven rules

### 1. Use the right Hermes feature first

Check current Hermes documentation and the live setup, then choose the supported place that naturally owns the behavior. Consider an existing or new class-level skill, `SOUL.md`, `USER.md`, `MEMORY.md`, project rules, Hermes configuration, built-in tools, profiles, routing, Kanban, Bot Chat, cron, webhooks, MCP, or a plugin. Do not force every change into an existing skill, and do not create a one-off micro-skill.

See `references/hermes-options.md` for the decision guide.

### 2. Scripts do repeatable steps, not judgment

Put decisions, exceptions, approvals, and user-facing rules in skills and agents. Use scripts only for repeatable mechanics such as fetching, parsing, validating, generating files, or checking a result. Never hide policy, routing, approvals, long prompts, or a queue inside a script.

### 3. Keep one clear owner

Give each standing rule one canonical home and each mutable target one writer. The architecture owner chooses the canonical mechanism and boundaries. The relevant domain owner executes live-system work. Independent reviewers challenge the design read-only; they do not become the owner. Do not create parallel queues, schedulers, routers, or writers for the same work without an explicit order and a proved need.

For a package that will run inside another profile, the architecture owner must inspect the package, choose the canonical owner, map source order and safety boundaries, and define the real-path acceptance test before installation. The target profile may exercise its domain workflow but must not inherit the architecture decision by default.

### 4. Build every new profile from scratch

Create a profile only for a lasting need for separate identity, memory, configuration, tools, credentials, sessions, skills, schedules, routes, gateway state, or model defaults. Start blank or with `--no-skills`, then add only what the job needs. Do not clone a broad profile by default. Use cloning only for deliberate, reviewed backup, migration, sharing, or reuse. Profiles separate Hermes state; they are not operating-system sandboxes.

### 5. Make the smallest reversible change

Solve the observed need with the least machinery that fully works. State the files or settings that change, how to undo them, and what would prove the design wrong. Defer extra services, queues, locks, ledgers, migrations, and broad governance until evidence requires them.

### 6. Check the real result, then check again

Test the actual entry point and consumer path, not an internal shortcut. Inspect the live result in the system that owns it; a successful command, task, scheduler run, or model claim is not enough.

After an authorized standing behavior change, define a one-time follow-up at the earliest meaningful point—usually after the next real run or within 24–72 hours. A read-only DFU review specifies the follow-up but does not schedule or assign it. Create that task or schedule only when the approved implementation scope includes it; otherwise request explicit approval. The follow-up complements the initial test and expires after it reports unless ongoing monitoring was explicitly requested.

### 7. Plugins are valid; Hermes core changes come last

A plugin is a documented Hermes extension and may be the cleanest owner for a tool, hook, command, platform adapter, memory provider, UI surface, or other runtime extension. Keep it narrow, optional, tested, and reversible. Use a custom service or Hermes core patch only when supported files, skills, configuration, tools, profiles, routing, schedules, connections, MCP, plugins, and an approved update cannot meet the requirement. Core patches need focused tests, rollback, an upstream path when practical, and a removal trigger.

## Procedure

1. **Recover the real requirement.** Separate the observed problem, required outcome, and suggested implementation. Treat summaries and copied handoffs as locator evidence; inspect primary source material before declaring a recurring requirement.
2. **Inspect docs and live state.** Run the bundled read-only `scripts/verify_package.py` when validating an installed DFU package. Use the current official Hermes documentation and inspect only the relevant skills, context files, config, profiles, routes, jobs, tools, MCP servers, plugins, version, and update state. Use the current documented read path for each source and state any local side effects before running it.
3. **Choose the simplest supported owner.** Use `references/hermes-options.md`; stop when one supported option fully solves the need. Configuration and plugins are normal options, not automatic fallbacks or defects.
4. **Apply policy.** Use verified local policy when present. Otherwise apply `references/recommended-policies.md` and state which defaults matter to the decision.
5. **Set boundaries.** Name the policy owner, worker, only writer, checker, source of truth, and user-facing responder. For a new profile, start from scratch and list only what it needs.
6. **Plan proof and reversal.** Name the exact real-path test, live result to inspect, rollback, and one-time follow-up check.
7. **Review material changes through three lenses.** Check scope, current Hermes documentation/native fit, and plain-language clarity before shipping a new profile owner, recurring route, new write authority, cross-profile policy, plugin/custom tool, or core patch. Reconcile the findings. Small prose-only edits do not require three reviewers.
8. **Implement only with authority.** Make the approved change once, verify the exact target, reload edited skills or runtime state as needed, and remove obsolete duplicate paths.
9. **Follow up.** Run the one-time check only when the task or schedule is already authorized. Otherwise return the follow-up plan and request approval. If the agreed behavior did not hold, report the failed check and use already-granted authority for rollback or correction; otherwise request explicit approval before another mutation.

## Review result

Lead with one of `PASS`, `PASS WITH CHANGES`, or `FAIL`, plus `high`, `moderate`, `low`, or `unknown` confidence. Keep the default result short:

- what changes;
- why this is the simplest supported Hermes option;
- which required or recommended policies apply;
- who owns the rule and who may change the target;
- how the real path will be tested;
- how to undo it;
- when the one-time follow-up will run; and
- required changes.

Use `templates/review-output.md` for material reviews. Put detailed evidence and official documentation links in a reference packet only when the requester needs them; do not bury the decision under the audit method.

## Do / don't

**Do**

- keep DFU's name and direct language;
- create a new class-level skill when it is the cleanest canonical home;
- consider Hermes configuration early when settings can enforce the behavior;
- use a plugin when the documented extension point fits;
- build profiles from scratch with the least they need; and
- keep one owner, one real-path test, one rollback, and one timed follow-up.

**Don't**

- use profanity outside a DFU call merely because the skill permits it here;
- hide policy in scripts or custom queues;
- copy the same rule into several skills or profiles;
- clone a broad profile for convenience;
- call a file edit or command exit “shipped”;
- install an update, restart a service, or widen write authority during a read-only review; or
- patch Hermes core before proving simpler supported options are insufficient.

## Pitfalls

- Inspect primary conversation bodies before calling feedback recurrent. Titles, summaries, copied handoffs, and delegated prompts can inflate the evidence.
- State whether a claim is a current fact, historical evidence, recommendation, or unknown. An old conversation does not prove today's live state.
- Test the boundary that failed. An internal test can pass while the real Slack, cron, webhook, profile, or external-system path still bypasses the fix.
- Separate wake logic, audit coverage, and delivery when reviewing a scheduled workflow. A timely post can still be an incomplete audit.
- Schedule the follow-up for the first meaningful delayed observation. An immediate check repeats the smoke test; a permanent monitor adds needless state.

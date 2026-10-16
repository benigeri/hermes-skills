---
{
  "name": "dfu",
  "description": "Audit Hermes changes: DFU, don't fuck up, don't fuck it up.",
  "version": "2.0.0",
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

Choose a clear, simple, maintainable approach before a lasting Hermes change ships. DFU is a review method, not a separate agent or a certificate of success.

## When to use

Treat **DFU**, **don't fuck up**, and **don't fuck it up** as the same call. Use it for lasting changes to skills, context files, configuration, tools, profiles, routing, Kanban, Bot Chat, cron, webhooks, memory, MCP, plugins, updates, write authority or core code.

The requester need only say **DFU**. For a substantive audit, plan or change, arrange **one independent read-only reviewer** through native `delegate_task`. Simple explanatory questions need no reviewer. `/review` is an optional user shortcut, not an additional required stage.

A review authorizes advice, not implementation. Use verified organization/project policy, or load `references/recommended-policies.md` when none exists. An explicit request for the exact action is approval for that scope; do not ask again under a different label. Separate credential, spending, access, send, restart and deployment gates still apply.

## Seven rules

### 1. Choose the simplest supported owner

Separate the required outcome from the suggested implementation. Load `hermes-agent` and its relevant reference; check current official documentation and live state. If that skill is unavailable, use the official docs and report the limitation—do not invent its contents.

Use `references/hermes-options.md` to choose among skills, context files, configuration, built-in tools, profiles, native task handling, schedules, connections, MCP and plugins. Stop when one supported option fully solves the need. Do not force every change into a skill or invent a micro-skill for one incident.

### 2. Keep judgment out of scripts

Agents and skills own interpretation, exceptions, approvals and recommendations. Scripts can fetch, parse, validate facts and carry out repeatable steps; they must not hide long prompts, routing policy or a queue. A keyword is not proof of intent; model confidence is not proof of an external fact.

Before introducing standing custom code—even a small helper—explain the native gap, smallest change, upkeep and removal path, and obtain the required explicit approval. Reuse approved tools without expanding their authority.

### 3. Keep one owner and one writer

Give each standing rule one canonical home and each exact mutable target one writer. The architecture owner selects the mechanism and boundaries; the domain owner performs authorized domain work. Reviewers stay read-only. Follow the local handoff policy rather than creating a competing queue or launcher.

Use the established update path. When a guard blocks it, inspect the caller and propose a small repair rather than bypassing the guard or changing destinations. Native notification admission is not proof of a final message or exactly-once external action. Preserve ambiguous-write reconciliation.

### 4. Build profiles from the minimum needed

Create a profile only for a lasting need for separate identity, state, configuration, tools or credentials. Start blank or with `--no-skills` when a minimal skill set is intended, then add what the role needs. Do not clone a broad profile for convenience; cloning is for deliberate reviewed backup, migration, sharing or reuse. Profiles are not OS sandboxes. A temporary model choice or a review does not need a profile.

### 5. Subtract before adding

Prefer deleting a conflicting requirement or correcting an argument over wrapping a working tool. Challenge restrictions by their actual risk and source; preserve valid credential, payment, access, send and integrity controls.

For exploration, try one useful permitted read-only path before production hardening. Keep the agreed independent review, but avoid extra reviewers, repeated polish, blanket suites, jobs and frameworks without a concrete need. Give meaningful options and a recommendation when a real choice exists; do not manufacture alternatives. Name the affected files/settings and a rollback that preserves concurrent work.

### 6. Prove the useful result, proportionately

Check the actual entry point, active worker and result in its owning system. A saved instruction, successful command, local test or reviewer agreement does not prove the worker adopted the change or delivered the requested outcome.

Deliver useful verified portions and state what remains incomplete. Hold only the action that depends on a missing check. Do not erase completed work, block unrelated progress, label partial delivery complete or bypass a required control to finish.

For instructions, inspect the saved result and walk contrasting cases; do not build a simulator to test prose. For existing code, use the current runner and focused tests of the failing path and affected dependencies. Label walkthroughs, local tests, live checks and natural runs separately. Prefer the next meaningful natural run or an existing bounded check for delayed evidence. A new follow-up requires a real evidence gap and authority; no automatic cron requirement. An absent observation is **not exercised/inconclusive**, not PASS or FAIL. One passing run is not sustained reliability.

### 7. Use extensions deliberately; core changes last

A documented plugin can be the cleanest tool, hook, command or adapter. Keep it narrow, optional, tested and reversible. Use a custom service or core patch only for a proved gap that supported options cannot solve. Obtain approval and name focused tests, rollback, an upstream path when practical and a removal trigger.

## Procedure

1. **Recover and bound.** Confirm outcome, scope and approval state. Read primary sources rather than copied summaries. Distinguish current defects, completed work, pending activation and unknowns. Do not revive cancelled work or re-ask settled choices.
2. **Load selectively.** DFU supplies review principles; the unmodified upstream `hermes-agent` supplies platform mechanics. Load existing task-specific instructions only when relevant—for example, task handoffs, scheduled work or shared-record changes. Do not auto-load an entire bundle. Local preferences may qualify workflow advice, not technical facts or required safety boundaries.
3. **Inspect and propose.** Compare policy, actual implementation and observed results. Choose the owner, narrow change, acceptance check and rollback. Inspect complete imported packages, not just their headline file. Keep local additions outside the upstream manual; before restoring a customized bundle, preserve them and inspect the command's full write set and update-tracking effects. Record a reviewed upstream revision/date for future comparisons, not an indefinite version freeze or a new monitor.
4. **Review once.** Give the independent reviewer the original goal, authority, exact sources/diff and relevant DFU/Hermes guidance—not only the author's summary. Ask it to check scope, simplicity, native fit, ownership, upkeep and clarity. Explicitly prohibit mutations and recursive review. Require it to name the concrete decision its evidence changes. Reconcile material findings; re-review only materially changed or unresolved parts. Reviewer failure is no verdict, not an independent PASS.
5. **Apply only with authority.** Preserve fresh preimages; check for intervening edits; change only approved targets; read back and reload as needed. Restore temporary briefs or holds. Complete independent approved slices without expanding into unrelated business reruns. A request to test does not grant new credentials, spending or writes.
6. **Verify and report.** Run `scripts/verify_package.py` when checking this package's structure. This checker does not evaluate judgment. For the task itself, check the real result and any meaningful delayed observation through an existing path when possible. Distinguish a protective stop from a broken guard, a bypass, a false rejection and missing evidence.

## Review result

Lead with the decision or useful outcome in plain language, and say whether the change is proposed or applied. Name the highest proven boundary and remaining gap. Include confidence when making a judgment. Explain a command's purpose before its syntax; being native does not make a command mandatory.

Use only the relevant fields in `templates/review-output.md`. Keep detailed evidence behind the decision. Say what remains undone without treating the whole task as failed. Preserve DFU's name and direct style; do not add profanity to unrelated output.

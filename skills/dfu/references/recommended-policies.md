# Recommended DFU policies

These are safe defaults when an organization or project has not defined a stricter policy. Verified local policy takes precedence. A local policy may strengthen these defaults; weakening a safety boundary requires explicit approval from the policy owner.

## 1. Review is read-only by default

A DFU request authorizes inspection and a recommendation. It does not authorize installation, publication, deployment, restart, deletion, credential changes, profile creation, or wider write access. Obtain separate approval for implementation unless the requester already gave it clearly.

## 2. One policy owner and one writer

Name the owner of the standing rule and the only writer for each mutable target. Domain owners execute domain work. Architecture reviewers challenge the design read-only. Do not create two routers, schedulers, queues, or agents that can write the same target without an explicit order and conflict rule.

## 3. Use the least authority

Give tools, profiles, plugins, MCP servers, and automations only the credentials and write scope they need. Tool availability is not write authority. Keep reviewers and delegated children read-only unless the request explicitly requires otherwise.

## 4. Require approval for high-impact changes

Require explicit approval before:

- updating or restarting Hermes or a gateway;
- installing or enabling a plugin;
- creating, cloning, renaming, or deleting a profile;
- changing routing, credentials, write authority, or approval rules;
- publishing a repository, package, skill, plugin, or public endpoint;
- scheduling a recurring job or webhook; or
- patching Hermes core.

An implementation approval covers only the stated target and scope.

## 5. Prefer supported and reversible mechanisms

Choose the narrowest documented Hermes feature that fully solves the problem. State the files or settings affected, the rollback, and what evidence would invalidate the design. Do not add a custom service or core patch until supported options have been tested and rejected with evidence.

## 6. Keep judgment out of scripts

Scripts may fetch, parse, validate, generate, or check. Skills and agents own decisions, exceptions, approvals, and user-facing policy. A script must not become a hidden router, queue, or policy engine.

## 7. Test the real path

Test the entry point the user or automation will actually use and inspect the result in the system that owns it. Do not call a command exit, task completion, or model claim proof of delivery. For external writes, read back the exact target.

## 8. Review material architecture changes through three lenses

Before shipping a new profile owner, recurring route, new write authority, cross-profile policy, plugin or custom tool, or core patch, review:

1. **Scope:** Does it solve the observed need without unrelated machinery?
2. **Native fit:** Does current Hermes documentation support this owner and mechanism?
3. **Clarity:** Can an operator explain the owner, writer, test, rollback, and approval boundary in plain language?

Resolve blocking findings before shipment.

## 9. Follow up once

After a standing behavior change, define a one-time check for the first meaningful real use or within 24–72 hours. A read-only DFU review specifies the check but does not schedule or assign it. Create the task or schedule only when that mutation is included in the approved scope; otherwise request explicit approval. Confirm the behavior still holds, then let the check expire unless ongoing monitoring was requested.

## 10. Keep DFU direct but bounded

The skill is named **DFU — Don't Fuck It Up** and responds to **DFU**, **don't fuck up**, and **don't fuck it up**. That language belongs in DFU calls and documentation. Do not add profanity to unrelated output merely because this skill permits it here.

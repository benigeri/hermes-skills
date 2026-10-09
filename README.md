# Hermes Skills

Public skill tap for reusable Hermes workflows maintained by Paul Benigeri.

## DFU — Don't Fuck It Up

DFU reviews lasting changes to Hermes before they ship. It triggers on `DFU`, `don't fuck up`, and `don't fuck it up`.

Install it into each named Hermes profile that should use it. Replace `<profile>` with the exact profile name; omit `-p <profile>` only when installing into the default profile.

```bash
hermes -p <profile> skills tap add benigeri/hermes-skills
hermes -p <profile> skills inspect benigeri/hermes-skills/dfu
hermes -p <profile> skills install benigeri/hermes-skills/dfu --category autonomous-ai-agents
```

Start a fresh Hermes session after installation so the skill index reloads.

Verify the installed files with the bundled read-only checker. For a named profile:

```bash
python3 ~/.hermes/profiles/<profile>/skills/autonomous-ai-agents/dfu/scripts/verify_package.py
hermes -p <profile> skills list --enabled-only
```

For the default profile:

```bash
python3 ~/.hermes/skills/autonomous-ai-agents/dfu/scripts/verify_package.py
hermes skills list --enabled-only
```

Require the checker to return JSON with `"status": "pass"` and require `dfu` in the installed-skill list. Then start a fresh session and run one representative DFU review through the entry point the team will use. A successful download or model claim alone is not proof that the package works.

Check and apply later revisions to a named profile with:

```bash
hermes -p <profile> skills check dfu
hermes -p <profile> skills update dfu
```

To remove DFU from a named profile:

```bash
hermes -p <profile> skills uninstall dfu
```

To roll back a published release, revert its reviewed repository commit, merge the revert, run `hermes -p <profile> skills update dfu --force`, and rerun the bundled verifier plus the representative review. Do not delete the prior release history.

## Repository layout

```text
skills/
  dfu/
    LICENSE
    SKILL.md
    references/
    scripts/
    templates/
```

Each skill must remain self-contained. Put required instructions in `SKILL.md`; keep optional depth in `references/`, deterministic mechanics in `scripts/`, and reusable output forms in `templates/`.

## Changes

Submit changes through a reviewed pull request. A release must include:

- an updated skill version when behavior changes;
- a clean-profile install and load test;
- one representative real-path review;
- rollback instructions; and
- a one-time follow-up check after the first real use or within 24–72 hours.

## License

MIT. See `LICENSE`.

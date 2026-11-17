# Using Project Kickoff

## A new project

Open the intended project folder. Invoke the skill in your agent and describe the product, preferred interface, authorized scope and desired coordinator/executor arrangement. State whether installations and model calls are already authorized and whether you need a prototype or a durable first version.

The first useful outcome is a small approved plan, not a large configuration inventory. The skill should ask about consequential unknowns, inspect only relevant configuration and preserve existing files.

## A project that already exists

Tell the agent to preserve uncommitted changes and reuse prior decisions. Profile preparation should not rewrite an existing architecture or restart product discovery. If the current chat belongs to another repository, select the correct folder before generating files.

## Direct delegation

Installing this skill does not connect tools. Claude needs a supported way to invoke an installed Codex CLI, an authenticated dedicated profile, bounded task instructions and an observable result. Start with a read-only smoke test, then one implementation task. Authentication should use official interactive flows, never copied credentials.

Coordinate edits to prevent agents writing the same files concurrently. Keep authority and acceptance criteria explicit. The coordinator inspects changes and reruns relevant checks; the user need not copy every message between agents.

## Resume

Provide the project checkpoint and recent relevant results. The agent should verify only changed or uncertain prerequisites, then continue the approved plan. A failed check is a reason for targeted diagnosis, not a complete setup restart.

## Sensitive data

Use fictional or properly authorized data for the first workflow. Separate settings are not a read sandbox. Review model data flows, environment inheritance, logs and tool permissions before real accounts or data. For stronger separation, choose appropriate system-level controls; this repository does not implement them.

## Installation troubleshooting

- **Skill missing:** inspect your installed agent's discovery rules, current profile and project scope; restart if required.
- **Global installation invisible:** this is expected when the profile excludes global skills. Copy/install the skill in the intended scope.
- **Plugin command differs:** verify official help for the installed version. Manual copying of the skill directory avoids plugin registration.
- **Codex not found/authenticated:** check executable discovery and the selected profile without printing credentials.
- **Browser test cannot run:** report the missing dependency and seek authorization for a scoped installation; do not claim static screenshots tested interaction.
- **Denied action:** explain it and use supported approval; never suggest disabling protections to make the command pass.

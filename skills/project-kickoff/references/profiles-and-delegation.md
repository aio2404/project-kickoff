# Profiles and direct delegation

Read only when configuring or diagnosing the execution environment. These are verification goals, not version-independent CLI recipes.

## Establish the baseline once

Inspect the target directory, applicable instructions and uncommitted changes. Record relevant tool versions and availability without printing credentials or environment values. Do not crawl a user's home directory. Inspect only configuration sources relevant to the requested isolation: instructions, skills, plugins, MCP, hooks, permissions, memory and update behavior.

Git is useful for comparison but is not a prerequisite for a small prototype. Initialize it only within existing authorization. Otherwise use a scoped baseline copy outside the executor's writable paths. Timestamps alone do not establish that contents are unchanged.

## Dedicated profiles

Use clearly named project-specific configuration directories if the installed tools support them. Current official documentation should determine how to pass profile settings to each process; never change HOME or export a project's profile globally in shell startup files. Preserve existing profiles and do not copy authentication files. The user authenticates through the official flow; never display tokens.

For Claude, inspect ancestor instruction discovery, user skills, synced plugins/skills, account connectors, hooks and permissions. Prefer a mode that asks about sensitive actions initially, without claiming every read or command prompts. Desktop and editor support must be checked separately; app-wide settings may affect other projects.

For Codex, check skills discovered outside its configuration directory, bundled skills, registered execution rules, plugins, MCP, hooks and memories independently. An empty profile directory alone is not proof of an empty effective environment. Disable unrelated components using supported settings; do not delete their global sources.

Finding a key in a binary is weaker evidence than a supported parser accepting it. If a validator is available, check a valid configuration and a deliberately invalid control without inference when supported. An unauthenticated invocation can still attempt network requests. Do not repeat inconclusive diagnostics indefinitely: report the specific uncertainty and its practical consequence.

## Optional skills

Verify current upstream instructions:

- Impeccable: https://github.com/pbakaus/impeccable
- webapp-testing: https://github.com/anthropics/skills/tree/main/skills/webapp-testing
- Superpowers: https://github.com/obra/superpowers
- Claude Code: https://code.claude.com/docs/
- Codex: https://developers.openai.com/codex/

Prefer project activation and dedicated caches when supported. Disclose cache writes outside the project. A global installation excluded by an isolated profile is not automatically available. Install only the selected webapp-testing directory when possible rather than a larger unrelated bundle. Record source revision and changed files.

Inspect installers and relevant hooks before executing them. For design tooling, check catalogue requests, telemetry and any subprocess that bypasses permissions. Revalidate opt-out variable names and their actual effect. For workflow packs, inspect branch completion, commit, subagent and external-action procedures. They remain subject to user authorization.

Install Python/browser dependencies when browser testing becomes necessary, in a scoped environment. An existing Chromium binary is not proof of compatibility. Static screenshots cannot silently replace interaction tests.

After reload, check the actual instruction, skill, plugin and hook inventory with commands supported by the installed version. Do not remove a security protection without explaining a suitable replacement.

## Claude launches Codex

Start with one executor. Prefer supported non-interactive Codex execution for bounded tasks: explicit working directory, prompt input, final result and structured event log. Verify flags locally. Do not build a custom orchestration platform for the first handoff or assume a historical MCP-hosting command is still supported.

The coordinator's profile, permissions, instructions and skills do not automatically apply to Codex. Supply project rules and task-specific references, then inspect effective context. Keep design/testing skills with the coordinator if appropriate; give the executor only what its role needs.

Scope writable paths and command/network capabilities to the task. Disabling command networking does not disable the model connection. A non-escalating approval policy, where supported, refuses escalation; it does not prohibit every command. Prompt instructions restricting file reads are not technical read controls. Use a container, VM or other appropriate boundary before exposing sensitive data if read access remains broad.

Plan for temporary files, test caches and browser profiles. A project-local temporary directory can work if tools actually honor it. Do not break tests through blanket restrictions and then weaken protections without explaining the change. Verify capability on a small relevant action.

An explicit request to have Claude run Codex authorizes necessary calls within an already accepted quota/budget. Do not repeat the question for every run. Clarify genuinely missing cost boundaries or a new billing path; never promise calls are free.

First smoke test: a read-only task limited to the project rules. Inspect its response and events and compare the baseline. If instructions were already injected, no file-read tool may be needed. This tests delegation/context transfer, not file editing, tool absence or effective sandbox enforcement.

For implementation, specify objective, allowed paths, acceptance criteria, checks and exclusions. Protect reference instructions/configuration from unauthorized modification. The coordinator inspects diffs and events and reruns relevant checks. Resumed tasks must explicitly retain the intended profile and restrictions; do not assume resume preserves every setting.

# Project Kickoff

**A reusable skill for starting a software project with scoped agent profiles, focused context, and a verified first result.**

[Français](README.fr.md) · [Usage](docs/usage.md) · [Security](SECURITY.md) · [Contributing](CONTRIBUTING.md)

Project Kickoff guides an AI coding agent from a new or existing folder to a small, testable implementation. When requested, Claude plans and reviews while launching Codex directly for implementation. It is an instruction package, **not an autonomous agent launcher or a sandbox**.

## What it helps with

- Preserve an existing project and avoid writing into the wrong repository.
- Check tool versions and effective configuration without exposing credentials.
- Prepare separate Claude/Codex profiles using currently supported settings.
- Select relevant skills instead of loading every available workflow.
- Transfer project rules and bounded tasks from Claude to Codex.
- Verify outcomes, maintain a short checkpoint, and avoid repeating setup on resume.

No installer, hook, telemetry collector or model client ships in this repository. Following the workflow can involve external tools, downloads and model calls; those tools have their own permissions, costs and data policies.

## Install the skill

### Skills CLI

If you already use the third-party Skills CLI, select the target agent and project scope when prompted:

```bash
npx skills add aio2404/project-kickoff --skill project-kickoff
```

`npx` may download and execute the Skills CLI. Review its prompts. This command is documented for convenience; it is not an installer maintained by this repository.

### Manual project-local installation

Clone this repository into a separate folder, then copy **only** `skills/project-kickoff`:

```bash
git clone https://github.com/aio2404/project-kickoff.git
```

For Claude Code, copy it to `<your-project>/.claude/skills/project-kickoff/`.
For Codex, copy it to `<your-project>/.agents/skills/project-kickoff/`, subject to the discovery rules of your installed version.
Preserve an existing destination rather than overwriting it. Start a new agent session and verify the skill is discovered.

### Claude Code plugin

The repository includes a marketplace and plugin manifest. Where supported by your installed Claude Code version:

```text
/plugin marketplace add aio2404/project-kickoff
/plugin install project-kickoff@project-kickoff-marketplace
```

Choose project scope when offered. The plugin contains this skill only; it does not bundle Impeccable, Superpowers, webapp-testing or Codex. Namespaced invocation is `/project-kickoff:project-kickoff`. With manual skill installation, use `/project-kickoff`.

An isolated profile may exclude a global installation. Install or expose this skill in the profile/project you actually use; do not assume it is inherited.

## Start

In Claude Code:

```text
Use project-kickoff to prepare this project. I prefer the terminal.
Claude should plan and review; Codex should implement tasks launched by Claude.
Preserve existing files. Ask before installations or changes outside the project.
Do not commit or publish. Start with a small prototype using fictional data.
```

In Codex, invoke `$project-kickoff`. The host can guide setup or act with available tools. Naming Claude does not give Codex control of a Claude session, and installing the skill does not connect the two tools automatically.

## Optional web-project tools

The workflow may propose [Impeccable](https://github.com/pbakaus/impeccable) for UI work, [webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) for browser interaction checks, and [Superpowers](https://github.com/obra/superpowers) for development workflows. They are optional, independently maintained and not redistributed here. Backend or non-web projects should use a different selection when appropriate.

## Requirements and limits

- An agent supporting `SKILL.md` and access to the project directory.
- For direct delegation: installed/authenticated Codex with supported non-interactive execution, plus a coordinator able to launch it.
- Live documentation/help checks: tool options and profile discovery change over time.
- Python 3.10+ only for this repository's dependency-free maintenance checks.

This skill does not enforce filesystem isolation, certify regulatory compliance, guarantee model performance or prevent all unsafe actions. Evaluate it with your actual agent versions and tasks. Read [security boundaries](SECURITY.md) before using real data.

## Validation

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Checks cover package structure, local references, manifests and common private-data patterns. They are not a comprehensive secret scanner or a benchmark of agent performance. [Behavioral scenarios](docs/evaluation.md) describe manual evaluation; no automatic live-model benchmark is claimed.

## Layout

```text
skills/project-kickoff/
  SKILL.md
  agents/openai.yaml
  references/profiles-and-delegation.md
  references/product-and-delivery.md
.claude-plugin/     Optional Claude Code plugin packaging
scripts/           Dependency-free package and privacy checks
tests/             Checks for validator behavior
docs/              Usage, boundaries and evaluation scenarios
```

## License

[MIT](LICENSE). This independent project is not affiliated with Anthropic, OpenAI or the authors of the optional tools. Their names identify supported workflows, not endorsements.

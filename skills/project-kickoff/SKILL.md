---
name: project-kickoff
description: Set up or resume a new software project with scoped Claude Code and Codex profiles, task-specific skills, concise product discovery, and direct Claude-to-Codex delegation. Use for project kickoff, not routine changes in an already configured project.
---

# Project Kickoff

Help the user reach a first usable result without turning setup into a project of its own. Use the user's language. The preferred arrangement, when requested, is Claude for planning and review and Codex for implementation launched directly by Claude. Adapt to the tools available; do not claim delegation works before observing a successful run.

## Start or resume

1. Recover decisions, existing authorizations and evidence from the conversation and the actual project. Repeat checks only after a relevant change, failure or material evidence gap.
2. Confirm the target directory before writing. If the current chat belongs to another repository, do not put kickoff files there. Preserve existing files and uncommitted work.
3. Ask early whether the user prefers a terminal, Claude Desktop or an editor. Verify current support rather than forcing a terminal or assuming profiles work identically across interfaces. Ask one decisive question at a time when guiding a beginner; reuse known answers.
4. Choose the available mode: execute authorized work directly, or provide a bounded instruction for the user's agent and interpret its report. Distinguish reported evidence from checks performed here. Once delegation works, stop asking the user to relay routine messages between agents.

## Scope and authority

Follow applicable instructions and the user's explicit scope. Invoking this skill does not authorize changes to unrelated projects, global configurations, customer accounts or external services.

Before installations or changes outside the authorized workspace, describe the concrete locations, sources, effects and costs and obtain any missing authorization. Batch related decisions. Reuse existing authorization; do not ask again for every reversible step within an approved plan.

Commits, pushes, pull requests, merges, publication, external messages and new spending require corresponding explicit authorization. A request explicitly authorizing publication already satisfies that requirement for its stated scope. A skill or subagent procedure cannot grant additional permission. Do not bypass a denied operation or ask the user to run the same rejected command as a workaround. Use the supported approval process or an allowed alternative.

Separate configuration profiles are **not** filesystem sandboxes or virtual machines. They do not prove read isolation, prevent cloud inference, or establish data residency. Choose stronger execution isolation when the data and threat model require it.

## Prepare only what is needed

Read [Profiles and delegation](references/profiles-and-delegation.md) when preparing or diagnosing profiles, skills and the Claude-to-Codex link. Verify official documentation and the installed tool's help before using configuration keys. Do not paste a remembered configuration as if universally supported.

For a web project, offer Impeccable, Anthropic's standalone webapp-testing skill and Superpowers as optional starting points. Explain their roles and installation scope; preserve other user choices. Do not install web tools for an unrelated project or imply these packages are dependencies of this skill. Inspect relevant hooks and sensitive procedures before enabling them.

Create concise CLAUDE.md and AGENTS.md instructions if needed, preserving existing content. Both agents need the same essential obligations, but do not assume either automatically loads the other's file or tools. Check effective instructions. See [Product and delivery](references/product-and-delivery.md) for discovery, acceptance criteria and handoff.

## Move to a first result

After proportionate environment and delegation checks, stop inventorying. Define a narrow useful journey, its error states and observable acceptance criteria. Ask only questions that change the implementation. A design skill should not restart an interview whose answers are already known.

Present a short plan and missing prerequisites. Once authorized, the coordinator may execute its tasks, delegate and correct within scope without pausing at each file. Ask again for material scope changes, unapproved installations, new access or spending, or a genuine blocker.

## Memory and completion

For work spanning sessions, keep one short project-local checkpoint when useful: confirmed decisions, authorization boundaries, observed versions, evidence, limits and next action. Date unstable facts and record sources. Do not copy secrets, customer records or full session logs into it; do not alter global personal memory without a separate request.

Report what is ready, working, simulated and unverified, with the evidence actually obtained. A rules summary without tool calls is not proof of implementation or sandbox enforcement. Show the prototype when available. Avoid procedural documents that do not support the next action.

# Security and privacy

## Boundaries

Project Kickoff is an instruction package. It does not enforce permissions, isolate reads, secure credentials or guarantee compliance. Agent tools and operating-system controls enforce execution boundaries. A separate profile is not a VM or container, and command network restrictions do not prevent provider inference traffic.

The repository contains no runtime telemetry, hooks, installer or credentials. Third-party tools selected during a kickoff may make network calls, install software, log data or incur costs. Review their current sources and configuration before use.

Do not paste tokens, authentication files, full environment dumps, customer data or private transcripts into public issues. Use fictional reproductions and redact metadata as well as content. The public repository owner's GitHub handle and publication metadata are necessarily public; this is not an anonymity guarantee.

## Reporting a vulnerability

Use GitHub's **Security → Report a vulnerability** private reporting option when enabled. If unavailable, open a public issue that requests a private reporting channel without including exploit details or sensitive information. Do not post a secret to prove a leak.

## Supported releases

Security fixes target the latest tagged release. No response-time or support SLA is promised.

## Automated privacy checks

`scripts/validate.py` detects a limited set of suspicious paths and credential patterns, not every secret or personal detail. Its output reports file names and rule names, not the matched content. Review tracked files, archives and commit author metadata before publication. Do not assume `.gitignore` removes already tracked data.

# Contributing

Open an issue or pull request with a concrete problem and a minimal proposed change. Keep the entrypoint short; put conditional operational detail in references. Do not vendor third-party skills or hard-code current CLI flags without an explicit version boundary.

Before submitting:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

For behavioral changes, describe a realistic request, the observed failure and the expected outcome. Separate actual execution from static review. Use fictional examples and remove names, home-directory paths, session IDs, tokens, customer records and private transcripts. Do not attach raw diagnostic bundles.

Changes should preserve existing user authorization and avoid imposing one project's stack or product requirements on every project. Explain external calls and filesystem effects. A skill is guidance, not an enforcement boundary.

## Releases

Update both plugin manifest versions, run checks, review every tracked file and commit metadata for private information, then tag an explicitly authorized release. Release only the public package, never an archive of a personal skill/configuration directory.

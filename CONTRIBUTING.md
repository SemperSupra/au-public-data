# Contributing

AU Public Data is currently in repository bootstrap. Contributions should preserve the project's public-data and provenance boundaries while the implementation takes shape.

## Scope

Please keep proposed work within the public repository's scope:

- information and source material that is already public;
- deterministic collection, parsing, normalization, validation, and publication code;
- schemas, tests, documentation, and safe fixtures;
- improvements to provenance and source-quality handling.

Private student information and account-specific material do not belong in this repository.

## Source-backed changes

Changes that add or alter a collector/parser should identify the public source it targets and explain why that source is authoritative for the data being normalized.

When practical, include a small safe fixture or deterministic test that demonstrates the source structure and expected normalized result without depending on a live network request for every test run.

## Provenance

New normalized fields should have a clear provenance story. If a value is derived rather than directly stated by the source, document the rule/evidence used to derive it.

See [`docs/PROVENANCE.md`](docs/PROVENANCE.md).

## Pull requests

Keep pull requests bounded and reviewable. A PR should explain:

- what source or capability it changes;
- what evidence supports the interpretation;
- what validation was run;
- whether generated public outputs change;
- any source/licensing considerations.

Do not mix unrelated refactors with source-interpretation changes when they can be reviewed separately.

## License status

The public software license has not yet been selected. Until a `LICENSE` file is added, contributions should not assume a particular outbound open-source license. License selection is part of the repository bootstrap and will be recorded explicitly before substantive public-code release.

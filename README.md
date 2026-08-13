# AU Public Data

> **Unofficial project.** This repository is not affiliated with, endorsed by, or operated by Assumption University of Thailand. It republishes normalized representations of information that is already publicly available from university-controlled or otherwise authoritative public sources, with provenance back to those sources.

AU Public Data is an open-source project for collecting, normalizing, validating, and publishing public Assumption University administrative, calendar, event, and deadline information in machine-friendly formats.

## Status

Repository bootstrap is in progress. No production feed or compatibility guarantee exists yet.

## Goals

The project aims to make already-public university information easier to consume by:

- people using calendar subscriptions;
- scripts and deterministic automation;
- agents that need structured, source-traceable inputs;
- downstream applications that prefer JSON, Atom/RSS, ICS, XML, or static HTTP resources over scraping pages directly.

The project does not make a normalized record authoritative merely because it exists here. The originating university source remains the authority.

## Public-data boundary

This repository is limited to information already available publicly from Assumption University or an explicitly justified authoritative public source.

It must not contain:

- authenticated AU SPARK state;
- private AU Microsoft 365 mail or files;
- personalized registration/completion state;
- grades, billing/payment records, or private student records;
- reusable authentication material or other secrets.

A future personalized student agent, if built, will be a separate private system and repository boundary.

## Initial source scope

Initial collection work will prioritize first-party sources such as:

1. Office of the University Registrar announcements, rules, and official academic-calendar links;
2. main AU event/publication systems and university repositories;
3. VMES, OIA, and other school/office public sources for domain-specific information.

Third-party mirrors may help locate an original source, but should not replace a university-owned source of record when one is available.

## Provenance

Normalized items should retain enough information to trace them back to their source evidence, including source/publisher identity, original URL or document identifier, retrieval information, content type, source hash, authority tier, and collector/parser version where applicable.

See [`docs/PROVENANCE.md`](docs/PROVENANCE.md).

## Planned outputs

The initial static publication model is expected to converge on resources similar to:

```text
public/
  api/v1/
    announcements.json
    deadlines.json
    events.json
    rules.json
    changes.json
    sources.json
  feeds/
    registrar.atom
    registrar.rss
    deadlines.atom
    academic-calendar.ics
    admin-deadlines.ics
    events.ics
    opportunities.ics
    all.ics
  index.html
  openapi.json
```

GitHub Pages can eventually serve these static outputs without requiring a dynamic application server.

## Processing principle

The project separates collection, interpretation, validation, and publication:

```text
public source -> evidence-preserving collector -> normalizer -> canonical records
              -> validation -> JSON / Atom-RSS / ICS / HTML publication
```

Core rule:

> Collectors collect evidence; normalizers interpret it; publishers do not discard provenance.

Deterministic extraction is preferred. LLM-assisted extraction may propose candidate facts during development, but it must not become the authority for source data without deterministic validation against the retained source evidence.

## Repository relationship

Development may begin in the private companion repository, but public changes arrive here through an explicit review/release gate. This repository is a real OSS product repository, not a shell for unrelated private computation.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions must respect the public-data, privacy, provenance, and source-authority boundaries above.

## License

A public software license has **not yet been selected**. Do not assume an open-source license grant until a `LICENSE` file is added and this section is updated. The licensing/redistribution status of generated or source-derived university data is evaluated separately from the software license.

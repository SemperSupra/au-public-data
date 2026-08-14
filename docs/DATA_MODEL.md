# Initial Data Model

AU Public Data uses a small canonical envelope so downstream consumers can rely on stable provenance and identity even when individual record types evolve.

This is bootstrap documentation, not yet a compatibility guarantee.

## Record classes

Initial normalized records are expected to include classes such as:

- `announcement`
- `deadline`
- `event`
- `rule`
- `opportunity`

Record-specific fields may be introduced through later schemas. The common envelope should remain useful across those classes.

## Common identity

Each normalized record should have:

- a stable project-controlled `id`;
- a `record_type`;
- a human-readable title;
- a reference to the registered public source that supplied the evidence;
- a provenance block;
- an explicit fact status.

Stable identity matters particularly for calendar publication, where the logical event should retain its identity across revisions.

## Fact status

Normalized values distinguish three cases:

- `explicit` — directly stated by retained authoritative evidence;
- `derived` — deterministically computed from an explicit published rule/date and traceable to that evidence;
- `candidate` — proposed interpretation that has not yet passed the publication validation gate.

Published production feeds should not expose unvalidated `candidate` facts as authoritative records.

## Provenance

The common provenance envelope captures the minimum audit link between a normalized record and source evidence:

- source registry ID;
- canonical source URL or artifact location;
- retrieval timestamp;
- source artifact SHA-256 when an artifact is retained or hashed;
- source publication timestamp when supplied by the publisher;
- collector and normalizer versions when applicable;
- evidence references supporting the normalized facts.

Missing publisher metadata stays absent rather than being invented.

## Time fields

Dates and times should retain their source semantics. Where a source supplies a local date/time, normalization should also preserve the relevant IANA timezone when known rather than silently converting an ambiguous wall-clock value.

The project should not infer a deadline time merely because a date is known.

## Source registry

`sources/registry.json` is the public declarative source inventory. Verified source candidates and their current status are documented in `docs/SOURCE_VERIFICATION.md`. Registry entries are added separately from source verification, and source-specific implementation remains a follow-on step.

Each source record captures authority tier and public source identity. Collector-specific implementation belongs outside the registry schema.

## Schemas

Bootstrap schemas live in `schemas/`:

- `source.schema.json` — one registered source;
- `source-registry.schema.json` — the registry document;
- `normalized-record.schema.json` — common normalized record envelope.

Schemas use JSON Schema Draft 2020-12 and are intentionally permissive enough for later record-specific extensions.

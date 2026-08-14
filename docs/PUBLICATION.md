# Publication architecture

AU Public Data publishes a machine-oriented, provenance-preserving representation of Assumption University's public information surface.

The public distribution layer is intentionally more than a set of current snapshots. It should behave like an append-oriented public data log hosted through GitHub Pages, with stable projections that are easy for automation and agents to consume.

## Design goals

Publication must be:

- reproducible from retained evidence plus versioned adapters/schemas;
- repeatable on a schedule;
- reversible to source evidence and prior normalized states;
- idempotent when inputs and versions have not changed;
- append-oriented for historical changes;
- easy to consume without understanding the collectors;
- static-host friendly so GitHub Pages can serve the complete public distribution surface.

GitHub Pages is the primary public distribution surface. Raw evidence storage may use a separate immutable object store, but every published record/change must carry enough provenance to resolve the evidence used to produce it.

## Two publication layers

### 1. Append-oriented canonical publication ledger

The historical publication record is an ordered stream of immutable change events. New information appends events; previously published events are not silently rewritten or deleted.

Examples of event operations include:

- `assert` — publish a new entity/claim/value;
- `revise` — publish a new version that supersedes an earlier published value;
- `retract` — record that a previously published assertion was withdrawn or invalidated;
- `supersede` — mark a curriculum/rule/source version as replaced while retaining it historically;
- `source-drift` — record a source/format transition relevant to published data;
- `publication-rebuild` — identify a deterministic regeneration under a new schema/projection version when appropriate.

A change event should include at least:

- stable event ID;
- stable entity/claim ID;
- operation;
- UTC acquisition/observation/publication timestamps where applicable;
- source ID and evidence/capture IDs;
- evidence SHA-256;
- adapter/parser version;
- canonical schema version;
- projection/publication version;
- previous event/version reference when applicable;
- semantic payload or deterministic reference to the published entity version;
- correlation/run ID.

Retractions and corrections are new events. They do not erase old events.

### 2. Consumer projections

Most consumers should not have to replay the full ledger. The publication build deterministically projects the ledger/canonical state into convenient formats.

These projections may be regenerated in place because their historical derivation remains recoverable from the append-oriented ledger and retained evidence.

## GitHub Pages layout

The exact paths may evolve before v1, but the publication contract should follow a stable shape such as:

```text
/
  index.html
  manifest.json
  coverage.json
  health.json

  log/
    index.json
    2026/
      08/
        13.ndjson
        14.ndjson

  snapshots/
    latest.json
    latest.sqlite
    latest.csv
    2026-08-13T180000Z/
      dataset.json
      dataset.sqlite
      coverage.json

  entities/
    programs.json
    curricula.json
    courses.json
    rules.json
    services.json
    opportunities.json
    sources.json

  feeds/
    announcements.atom
    announcements.rss
    opportunities.atom
    opportunities.rss
    changes.atom
    changes.rss

  calendars/
    academic.ics
    deadlines.ics
    events.ics
    opportunities.ics

  schemas/
    ...
```

Historical log segments are immutable after publication except for an explicit, separately recorded repository-repair procedure. New records append to a new segment or append-only build artifact.

`latest.*`, feed files, calendar files, manifests, and current entity snapshots are mutable projections/pointers. Their history remains reconstructable from Git history plus the append-oriented publication ledger and retained evidence.

Git history is useful audit evidence but is not the sole archival mechanism.

## Append-only log format

NDJSON is the preferred primary log projection because it is streamable, line-oriented, easy to append, simple to parse in almost every language, and efficient for agents/batch systems.

Each line is one independently parseable event object.

Large histories should be segmented by UTC date or another deterministic bounded interval. A top-level `log/index.json` should enumerate segments, hashes, first/last event IDs, time ranges, schema version, byte sizes, and successor/predecessor relationships where useful.

Consumers should be able to:

1. download/replay the entire history;
2. start from a snapshot and consume only later log segments;
3. bookmark a last-seen event/segment and resume incrementally;
4. verify segment hashes;
5. detect gaps.

## Snapshot contract

Periodic/current snapshots accelerate consumers that do not need to replay history.

At minimum publish:

- canonical JSON snapshot;
- portable SQLite snapshot;
- CSV projections where the entity shape is tabular enough to be useful;
- coverage and source-health manifests.

Every snapshot identifies:

- snapshot ID;
- generated-at UTC timestamp;
- canonical schema version;
- highest incorporated log event/sequence;
- source coverage manifest/hash;
- build/repository revision;
- content hashes for distributed artifacts.

A consumer can therefore load `latest.sqlite` and then continue from the next log event without re-crawling AU.

## RSS and Atom

RSS/Atom are first-class public interfaces, not decorative site features.

Publish separate feeds for meaningful consumer domains such as:

- announcements;
- opportunities;
- important deadlines;
- material dataset changes;
- source/coverage health changes when useful for operators.

Feed entries use stable IDs that correspond to canonical entity/change IDs. A correction updates the current feed representation while the append-only ledger retains the complete change history.

Feeds should contain source/provenance links and machine-readable references back to canonical JSON records whenever practical.

Atom is preferable where its semantics are helpful, but RSS should also be emitted for broad compatibility.

## ICS

ICS is a projection of event-like canonical records, never the canonical data model.

Publish stable subscription URLs for useful calendar families, for example:

- academic-calendar events;
- registration/deadline events;
- university events;
- opportunities/application deadlines.

Rules:

- logical events retain stable `UID`s across revisions;
- revisions update the existing event and increment `SEQUENCE` as appropriate;
- cancellation/withdrawal uses calendar semantics such as `STATUS:CANCELLED` rather than silently disappearing when appropriate;
- source/provenance URLs are retained in event metadata/descriptions where practical;
- date-only and date-time semantics remain distinct;
- `Asia/Bangkok` is used when the source defines local AU time and no more specific timezone semantics apply;
- individual-student applicability is never inferred from public data.

The historical sequence of calendar changes remains represented in the canonical publication ledger even though the subscription `.ics` file normally represents the current calendar state.

## JSON and JSON-LD

Publish stable JSON resources for canonical entities and relationships. JSON-LD or another graph-friendly projection should expose relationships among programs, curriculum versions, courses, requirements, sources, claims, and evidence without forcing consumers to infer joins from prose.

Stable IDs must not depend on transient URLs when a durable semantic identity exists.

## CSV

CSV is useful for simple tabular reuse and human inspection. Do not flatten complex requirement/claim structures so aggressively that semantics are lost; use CSV only for projections where the tabular representation remains honest.

## SQLite

Publish a portable SQLite snapshot as a primary agent/automation interface.

It should allow an agent to download one static file and query the public AU model locally without repeated network calls or knowledge of the collection pipeline.

SQLite should include provenance/evidence identifiers and relationships needed to trace values back to source records.

## Coverage and health

The publication surface must make incompleteness visible.

`coverage.json` / `health.json` should report, per source family/source/entity family where useful:

- discovered/verified/configured/unsupported status;
- last successful acquisition;
- newest incorporated evidence;
- current source-definition/capture-format/adapter versions;
- drift/compatibility state;
- last-known-good publication revision;
- consecutive failures;
- freshness status/SLA;
- historical coverage start;
- known gaps.

The system should never imply complete AU coverage merely because a snapshot successfully built.

## Provenance and traceability

Every projection must expose a path back to canonical records/claims and then to source evidence.

A consumer should be able to answer:

- where did this value come from?;
- what source artifact and capture produced it?;
- what parser/schema version interpreted it?;
- what did the project publish previously?;
- when and why did the value change?;
- can the result be regenerated from retained evidence?

## Build and deployment behavior

A scheduled GitHub Actions publication run should conceptually:

1. acquire and archive source evidence;
2. append acquisition/change/drift records;
3. normalize changed evidence;
4. validate canonical invariants and regression fixtures;
5. compute semantic changes;
6. append new publication-log events;
7. regenerate current snapshots/projections;
8. validate RSS/Atom/ICS/JSON/SQLite artifacts;
9. atomically publish the Pages tree only after validation succeeds;
10. preserve the prior Pages publication if the new build fails.

Repeated execution against unchanged source evidence and unchanged code/schema versions must produce no new semantic events and equivalent current projections.

## Publication failure semantics

Source drift or a parser failure must not cause known-good public information to disappear.

Instead:

- archive the new raw evidence;
- record source/drift health state;
- retain the last-known-good normalized/public projection for affected records;
- mark freshness/compatibility explicitly;
- repair/reprocess retained evidence later;
- append resulting correction/revision events after deterministic validation.

## Relationship to raw archive

The public Pages log is the history of the project's machine-readable observations and normalized publication state. It is not necessarily a byte-for-byte mirror of every raw source object.

Raw web captures/PDFs/source artifacts belong in the content-addressed evidence archive where lawful/practical. Pages publishes their hashes, identities, provenance records, and normalized consequences.

This keeps the public machine interface small and reusable while preserving full traceability to the evidence archive.

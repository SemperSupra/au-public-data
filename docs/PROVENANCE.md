# Provenance Policy

## Purpose

AU Public Data republishes normalized representations of public information. Every published record should remain traceable to the evidence used to create it.

The normalized output is a convenience layer; the originating authoritative source remains the source of record.

## Source authority

Prefer sources in this order unless a specific domain requires a documented exception:

1. Assumption University Registrar announcements, rules, and official calendar documents.
2. Main AU event/publication systems and university repositories.
3. School/office sources such as VMES and OIA for their own public material.
4. Third-party sources only as discovery aids or when an exception is explicitly documented.

An official domain is not sufficient by itself to prove that every embedded link or item is trustworthy. Anomalous content should be reviewed before republication.

## Required provenance fields

Canonical schemas should support, where applicable:

- publisher or university office;
- canonical source URL;
- source domain;
- source document/file identifier;
- source publication timestamp;
- retrieval timestamp;
- media/content type;
- source artifact SHA-256;
- authority tier;
- collector version;
- parser/normalizer version;
- original attachment/artifact links;
- prior artifact hash/version for change tracking.

Not every source exposes every field. Missing source metadata should remain explicitly absent rather than fabricated.

## Raw evidence and normalized records

Collectors should preserve enough source evidence to support later verification of normalized facts. Expensive parsing should not be repeated when the source artifact has not changed.

Normalization should distinguish:

- **explicit facts** stated by an authoritative source;
- **derived facts** computed from published rules or dates;
- **inferences/candidates** that require further validation.

Derived values should identify the rule/source evidence from which they were derived.

## Change tracking

Meaningful changes should be first-class where practical. For example, a changed deadline should preserve before/after values and the time the change was detected rather than silently replacing the previous value with no trace.

Git history may provide the initial audit/history mechanism for generated public data, while record-level change metadata can serve downstream consumers that need semantic change information directly.

## Calendar identity

Published ICS events should retain stable UIDs across revisions. When an existing event changes, update the existing event representation, update revision timestamps, and increment `SEQUENCE` as appropriate rather than issuing a new UID for the same logical event.

## Automated and AI-assisted extraction

Deterministic parsers are preferred when the source structure supports them.

AI-assisted extraction may be used during development to identify candidate facts or parser strategies, but an AI-generated interpretation is not authoritative merely because it is plausible. Publication must remain grounded in retained source evidence and the project's validation rules.

## Collection behavior

Collectors should be conservative toward university infrastructure:

- prefer native machine-readable feeds when available;
- use change-detection mechanisms such as ETag, Last-Modified, or content hashes when available;
- avoid unnecessary repeated downloads and parsing;
- use bounded polling frequencies;
- respect publisher access and usage controls.

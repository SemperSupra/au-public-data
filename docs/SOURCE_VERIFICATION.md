# Verified Public Sources

Verification date: 2026-08-13

This document records the first bounded set of public first-party Assumption University sources verified for the source registry. Collector implementation is not authorized by this document.

## Tier 1 — Office of the University Registrar

### Registrar academic calendar

- Stable ID: `registrar-academic-calendar`
- Publisher: Office of the University Registrar, Assumption University
- URL: `https://registrar.au.edu/academic-calendar/`
- Source type: HTML landing page with embedded academic-calendar material
- Authority: Tier 1
- Scope: official semester calendars, admissions calendar material, academic-year calendar, and university public-holiday calendar links
- Collection status: disabled pending collector/parser review

The public page identifies itself as the Office of the University Registrar and currently presents Semester 1/2026, Calendar Academic Year 2026, admissions calendars, and university public-holiday calendar material.

### Registrar announcements

- Stable ID: `registrar-announcements`
- Publisher: Office of the University Registrar, Assumption University
- URL: `https://registrar.au.edu/news-cats/all-announcement/`
- Source type: HTML listing
- Authority: Tier 1
- Scope: official Registrar announcements and student-administration schedules/notices
- Collection status: disabled pending collector/parser review

The current public listing includes 2026 registration, adding/withdrawal, examination, student-ID, scholarship, and other Registrar notices.

### Registrar academic rules and regulations

- Stable ID: `registrar-academic-rules`
- Publisher: Office of the University Registrar, Assumption University
- URL: `https://registrar.au.edu/academic-rules-regulation/`
- Source type: HTML rules index
- Authority: Tier 1
- Scope: public academic rules and regulations including prerequisites, course-load limits, examinations, and related academic policies
- Collection status: disabled pending collector/parser review

The public rules index currently links Registrar-controlled rule material and is appropriate as the authoritative discovery surface for rule normalization.

## Tier 2 — Main Assumption University site

### Assumption University events

- Stable ID: `au-events`
- Publisher: Assumption University of Thailand
- URL: `https://www.au.edu/event/`
- Source type: HTML event calendar/listing
- Authority: Tier 2
- Scope: university-wide public event dates, times, locations, and descriptions
- Collection status: disabled pending collector/parser review

The current public event calendar exposes list/month/day views and current 2026 university events.

## Registry promotion

These four sources are ready to become the first entries in `sources/registry.json` with `enabled: false`. They remain disabled until source-specific collection/parsing is reviewed separately.

Registry promotion is pending only because the GitHub mutation layer rejected the registry rewrite during this bootstrap session; the source verification itself is complete.

## Machine-readable endpoint status

No stable public RSS, Atom, ICS, JSON, or XML endpoint has yet been verified for these four sources. Do not infer one from apparent site technology or URL conventions.

Before implementing collectors, separately verify whether a native machine-readable endpoint exists and prefer it over HTML scraping when available.

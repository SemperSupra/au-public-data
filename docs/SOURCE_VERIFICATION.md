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

The public page currently presents Semester 1/2026, Semester 2/2026, Calendar Academic Year 2026, admissions calendars, and university public-holiday calendar material. The current semester/year calendars are embedded as separate public Google Drive PDF artifacts.

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

The public rules index is the authoritative discovery surface for Registrar-controlled academic rule material.

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

## Tier 3 — School and office sources

### Office of International Affairs / AU Study Abroad

- Stable ID: `oia-study-abroad`
- Publisher: Office of International Affairs, Assumption University
- URL: `https://oia.au.edu/`
- Source type: HTML site
- Authority: Tier 3
- Scope: public exchange, study-abroad, short-program, international internship, scholarship/opportunity, and OIA event information
- Collection status: disabled pending collector/parser review

OIA identifies itself and the AU Study Abroad Centre as internal Assumption University units serving inbound/outbound mobility and global opportunities.

### VMES news and events

- Stable ID: `vmes-news-events`
- Publisher: Vincent Mary School of Engineering, Science and Technology, Assumption University
- URL: `https://vmes.au.edu/`
- Source type: HTML site/news surface
- Authority: Tier 3
- Scope: VMES public news, events, school activities, program-related opportunities, and announcements relevant to Engineering/Science/Technology students
- Collection status: disabled pending collector/parser review

The current VMES site exposes a News & Events section and latest school news.

### VMES current-student information

- Stable ID: `vmes-student-life`
- Publisher: Vincent Mary School of Engineering, Science and Technology, Assumption University
- URL: `https://vmes.au.edu/student-life/`
- Source type: HTML current-student index
- Authority: Tier 3
- Scope: public current-student information, including school academic milestone/checklist material and related student links
- Collection status: disabled pending collector/parser review

The current Student Life page explicitly points current students to faculty information and an Academic Milestone Checklist.

## Deferred source candidates

### Student Affairs / Career Development

Current AU event and news pages identify Student Affairs and the Center for Career Development & Counseling as organizers of student-life and career activities and point to `https://sa.au.edu/`. The main AU event calendar already carries examples such as Career Week and Club Week.

A separate Student Affairs/CCDC registry source is deferred until a stable public listing surface can be directly verified for deterministic collection. Do not duplicate the same events from the main AU event source merely because organizer pages exist.

## Registry promotion

These seven sources are ready to become the initial entries in `sources/registry.json` with `enabled: false`. They remain disabled until source-specific collection/parsing is reviewed separately.

Registry promotion is pending only because the GitHub mutation layer rejected the registry rewrite during this bootstrap session; the source verification itself is complete.

## Machine-readable endpoint status

No stable public RSS, Atom, ICS, JSON, or XML endpoint has yet been verified for these seven sources. Do not infer one from apparent site technology or URL conventions.

Before implementing collectors, separately verify whether a native machine-readable endpoint exists and prefer it over HTML scraping when available.

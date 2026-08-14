# Resource governance

AU Public Data must be low-impact by default. Free-tier capacity is a ceiling, not a target, and data providers should not experience the project as a noisy crawler or resource hog.

Core requirements:

- do no work when no work is needed;
- prefer native feeds/APIs and conditional HTTP GET before full retrieval;
- cache discovery results and deduplicate URLs/artifacts;
- use per-host concurrency 1 by default and avoid bursts;
- honor Retry-After, cache, rate-limit, robots/access rules, and platform restrictions;
- adapt cadence to source change frequency rather than polling everything equally;
- batch due sources into a small number of orchestrated GitHub Actions runs;
- set explicit workflow timeouts and prevent overlapping scheduled runs;
- keep no-change runs short and do not rebuild/deploy GitHub Pages when canonical state is unchanged;
- treat browser rendering and AI as exception-driven fallbacks, not routine steps;
- configure soft/hard free-tier budgets and preserve reserve capacity for real drift events;
- track Actions runtime, HTTP requests/bytes, 304 rate, browser minutes, AI calls/tokens, storage operations, and publication builds;
- back off safely when providers are slow, failing, rate-limited, or nearing quota;
- retain last-known-good public state with degraded freshness metadata rather than retrying aggressively.

Suggested initial cadence classes:

- urgent operational sources: normally up to twice daily, with temporary documented acceleration only during known active windows;
- ordinary announcements/events/opportunities/services: daily or every other day;
- curricula/rules/course descriptions/program requirements/study plans: weekly;
- external regulatory/reference sources: weekly to monthly;
- historical/superseded material: very infrequent checks after capture.

Repeated unchanged observations should lengthen intervals; failures use exponential backoff with jitter. A 304, identical evidence hash, or semantically identical reparse normally produces no public log event and no Pages deployment.

Resource governance is part of correctness: production adapters/workflows must have bounded cadence, concurrency, retries, runtime, provider budgets, telemetry, and a fast no-change path.
# Resource-governance acceptance checklist

A production collection/publication workflow must demonstrate:

- source-specific cadence and `next_eligible_check_at` scheduling;
- conditional/cached acquisition where supported;
- per-host concurrency and retry/backoff bounds;
- explicit GitHub Actions wall-clock timeout and non-overlap concurrency policy;
- a fast no-change path;
- no public commit or Pages deployment on no semantic change;
- browser and AI disabled on the routine path;
- provider soft/hard budgets and reserve capacity;
- resource telemetry for HTTP, Actions, browser, AI, storage, and publication;
- safe degraded/stale behavior when a source/provider is unavailable or near quota;
- regression tests proving unchanged inputs do not create publication churn.

# Public Source Registry

`sources/registry.json` is the declarative inventory of public sources approved for collection work.

The bootstrap registry is intentionally empty. A source should be added only after its ownership, authority, public accessibility, scope, and expected content type have been verified.

Each source entry must validate against `schemas/source.schema.json` and should use a stable lowercase kebab-case ID.

Authority tiers follow `docs/PROVENANCE.md`:

1. Registrar rules, announcements, and official academic-calendar material.
2. Main AU event/publication systems and university repositories.
3. School/office sources for their own public material.
4. Third-party material only as a documented exception or discovery aid.

Collector implementation does not belong in the registry. The registry identifies what may be collected; code determines how collection is performed.

# Public Source Registry

`sources/registry.json` is the declarative inventory of public sources approved for collection work.

Source verification is recorded in `docs/SOURCE_VERIFICATION.md`. The first pass has verified seven first-party Assumption University surfaces. They are candidates for registry promotion with collection disabled; the registry remains empty until that promotion is successfully applied and reviewed.

Each source entry must validate against `schemas/source.schema.json` and should use a stable lowercase kebab-case ID.

Authority tiers follow `docs/PROVENANCE.md`:

1. Registrar rules, announcements, and official academic-calendar material.
2. Main AU event/publication systems and university repositories.
3. School/office sources for their own public material.
4. Third-party material only as a documented exception or discovery aid.

Collector implementation does not belong in the registry. Source verification identifies eligible source surfaces; it does not itself authorize collection code.

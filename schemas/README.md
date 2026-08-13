# Schemas

Bootstrap contracts use JSON Schema Draft 2020-12.

- `source.schema.json` describes one verified public source.
- `source-registry.schema.json` describes `sources/registry.json`.
- `normalized-record.schema.json` defines the common normalized-record envelope.
- `temporal.schema.json`, `provenance.schema.json`, and `applicability.schema.json` provide reusable normalized-record components.

## Deterministic local validation

The checked-in validator is `scripts/validate.py`. It performs no network retrieval: local schema resources are registered in-memory for `$ref` resolution, then the script validates all checked-in schemas, `sources/registry.json`, and every JSON fixture under `fixtures/normalized/`.

Use a normal Python environment with the `jsonschema` package and its non-GPL format extras:

```text
python -m pip install "jsonschema[format-nongpl]>=4.22,<5"
python scripts/validate.py
```

A successful run exits 0 and prints a compact `PASS` summary. Validation errors are written to stderr and return a nonzero exit code.

These schemas remain bootstrap contracts rather than a stable compatibility guarantee until the bootstrap PR is merged and the project explicitly versions the public data contract.

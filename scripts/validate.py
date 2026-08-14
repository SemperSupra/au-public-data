#!/usr/bin/env python3
"""Validate checked-in AU Public Data schemas and fixtures without network access."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
REGISTRY_FILE = ROOT / "sources" / "registry.json"
FIXTURES = ROOT / "fixtures" / "normalized"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_registry(schema_docs: dict[str, object]) -> Registry:
    registry = Registry()
    for name, schema in schema_docs.items():
        registry = registry.with_resource(name, Resource.from_contents(schema))
    return registry


def validate_instance(instance, schema, registry: Registry, label: str) -> list[str]:
    validator = Draft202012Validator(
        schema,
        registry=registry,
        format_checker=FormatChecker(),
    )
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    messages = []
    for error in errors:
        path = ".".join(str(part) for part in error.absolute_path) or "<root>"
        messages.append(f"{label}: {path}: {error.message}")
    return messages


def main() -> int:
    schema_paths = sorted(SCHEMAS.glob("*.schema.json"))
    schema_docs = {path.name: load_json(path) for path in schema_paths}

    failures: list[str] = []

    for name, schema in schema_docs.items():
        try:
            Draft202012Validator.check_schema(schema)
        except Exception as exc:  # jsonschema reports the precise schema failure.
            failures.append(f"schema {name}: {exc}")

    registry = build_registry(schema_docs)

    source_registry_schema = schema_docs["source-registry.schema.json"]
    failures.extend(
        validate_instance(
            load_json(REGISTRY_FILE),
            source_registry_schema,
            registry,
            "sources/registry.json",
        )
    )

    normalized_schema = schema_docs["normalized-record.schema.json"]
    for fixture in sorted(FIXTURES.glob("*.json")):
        failures.extend(
            validate_instance(
                load_json(fixture),
                normalized_schema,
                registry,
                str(fixture.relative_to(ROOT)).replace("\\", "/"),
            )
        )

    if failures:
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        return 1

    print(f"PASS schemas={len(schema_paths)} registry=1 fixtures={len(list(FIXTURES.glob('*.json')))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

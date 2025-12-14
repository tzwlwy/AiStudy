import json
from jsonschema import validate, ValidationError


class SchemaValidator:
    def validate(self, raw_output: str, schema: dict):
        try:
            data = json.loads(raw_output)
        except Exception:
            raise ValueError("Invalid JSON")

        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            raise ValueError(f"Schema error: {e.message}")

        return data

from .json_validator import validate_json_with_schema


class SchemaValidator:
    def validate(self, raw_output, schema):
        # 现在只有 json，一点都不复杂
        return validate_json_with_schema(raw_output, schema)

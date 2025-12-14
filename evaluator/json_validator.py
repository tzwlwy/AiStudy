import json
from typing import Type
from pydantic import BaseModel, ValidationError as PydanticError
from .result import ValidationResult, ValidationError


def validate_json_with_schema(
    raw_output: str,
    schema: Type[BaseModel]
) -> ValidationResult:

    # 1️⃣ JSON 解析
    try:
        data = json.loads(raw_output)
    except json.JSONDecodeError as e:
        return ValidationResult(
            ok=False,
            data=None,
            raw_output=raw_output,
            errors=[
                ValidationError(
                    code="JSON_PARSE_ERROR",
                    field=None,
                    message=str(e)
                )
            ]
        )

    # 2️⃣ Schema 校验
    try:
        obj = schema.model_validate(data)
        return ValidationResult(
            ok=True,
            data=obj.model_dump(),
            raw_output=raw_output,
            errors=[]
        )
    except PydanticError as e:
        errors = []
        for err in e.errors():
            field = ".".join(map(str, err.get("loc", [])))
            errors.append(
                ValidationError(
                    code="SCHEMA_VALIDATION_ERROR",
                    field=field,
                    message=err.get("msg")
                )
            )

        return ValidationResult(
            ok=False,
            data=None,
            raw_output=raw_output,
            errors=errors
        )

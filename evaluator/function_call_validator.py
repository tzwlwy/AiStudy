from adapters.function_call_adapter import extract_function_args
from evaluator.result import ValidationResult, ValidationError


def validate_function_call(raw_output, schema) -> ValidationResult:
    try:
        parsed = extract_function_args(raw_output)
        obj = schema.model_validate(parsed)
        return ValidationResult(
            ok=True,
            data=obj.model_dump(),
            raw_output=raw_output,
            errors=[]
        )
    except Exception as e:
        return ValidationResult(
            ok=False,
            data=None,
            raw_output=raw_output,
            errors=[
                ValidationError(
                    code="FUNCTION_CALL_ERROR",
                    field=None,
                    message=str(e)
                )
            ]
        )

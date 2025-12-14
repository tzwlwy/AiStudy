from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ValidationError:
    code: str              # error_type
    field: Optional[str]   # 哪个字段
    message: str           # 人可读信息


@dataclass
class ValidationResult:
    ok: bool
    data: Optional[Dict[str, Any]]
    errors: List[ValidationError]
    raw_output: str        # 永远保留原始输出

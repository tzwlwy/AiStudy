# schemas/registry.py

from schemas.user import UserSchema
from schemas.order import OrderSchema

SCHEMA_REGISTRY = {
    "user_generate": UserSchema,
    "order_generate": OrderSchema,
}

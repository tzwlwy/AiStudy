# schemas/user.py
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str

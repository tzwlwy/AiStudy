# schemas/order.py
from pydantic import BaseModel


class OrderSchema(BaseModel):
    order_id: int
    amount: float

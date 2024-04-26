from typing import Optional
from pydantic import BaseModel


class UserVerify(BaseModel):
    name: str
    created_date_time: Optional[str] = None
    updated_date_time: Optional[str] = None
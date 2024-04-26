from typing import Optional, List
from pydantic import BaseModel
from src.api_models.step import Steps


class Tutorials(BaseModel):
    name: str
    created_date_time: Optional[str] = None
    steps: List[Steps]
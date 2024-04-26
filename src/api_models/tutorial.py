from typing import Optional, List
from pydantic import BaseModel
# from src.api_models.step import Steps

class Steps(BaseModel):
    position: int
    image_url: str
    headline: str
    description: str
    marker: dict

class GetSteps(BaseModel):
    id: int
    position: int
    image_url: str
    headline: str
    description: str
    marker: dict


class Tutorials(BaseModel):
    id: int
    name: str
    created_date_time: str = None
    steps: List[GetSteps]

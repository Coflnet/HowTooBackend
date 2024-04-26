from typing import Optional, List
from pydantic import BaseModel
# from src.api_models.step import Steps

class Steps(BaseModel):
    position: int
    image_url: str
    headline: str
    description: str
    marker: dict


class Tutorials(BaseModel):
    id: int
    name: str
    created_date_time: Optional[str] = None
    steps: List[Steps]
    

class UpdateTutorials(BaseModel):
    name: Optional[str]
    steps: Optional[List[Steps]]
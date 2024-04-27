from typing import Optional, List, Dict
from pydantic import BaseModel
# from src.api_models.step import Steps


class PostSteps(BaseModel):
    position: int
    file_name: str
    description: str
    marker: Dict[str, str]

class GetSteps(BaseModel):
    id: int
    position: int
    image_url: Optional[str]
    description: str
    marker: Dict[str, str]


class Tutorials(BaseModel):
    id: int
    name: str
    created_date_time: str = None
    steps: List[GetSteps] 


class PostTutorials(BaseModel):
    name: str
    created_date_time: str = None
    steps: List[PostSteps] 

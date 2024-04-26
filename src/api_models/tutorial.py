from typing import Optional, List
from pydantic import BaseModel
# from src.api_models.step import Steps
from fastapi import FastAPI, File, UploadFile

class PostSteps(BaseModel):
    position: int
    file: UploadFile = File(...)
    description: str
    marker: dict

class GetSteps(BaseModel):
    id: int
    position: int
    image_url: str
    description: str
    marker: dict


class Tutorials(BaseModel):
    id: int
    name: str
    created_date_time: str = None
    steps: List[GetSteps] 


class PostTutorials(BaseModel):
    name: str
    created_date_time: str = None
    steps: List[PostSteps] 

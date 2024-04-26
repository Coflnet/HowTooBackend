from pydantic import BaseModel


class Step(BaseModel):
    position: int
    image_url: str
    headline: str
    description: str
    tutorial_id: int

from pydantic import BaseModel


class Steps(BaseModel):
    position: int
    image_url: str
    headline: str
    description: str
    marker: dict
    tutorial_id: int

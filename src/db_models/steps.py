from typing import Optional
from sqlmodel import Relationship, SQLModel, Field
from sqlalchemy import JSON
from src.db_models.tutorials import TutorialsTable

class StepsTable(SQLModel, table=True):
    __tablename__ = "steps"

    id: Optional[int] = Field(default=None, primary_key=True)
    position: int
    image_path: Optional[str] = Field(default=None)
    headline: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    marker: dict = Field(sa_type=JSON())
    tutorials_id: int = Field(default=None, foreign_key="tutorials.id")
    tutorials: "TutorialsTable" = Relationship(back_populates="steps")


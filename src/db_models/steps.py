from typing import Optional
from sqlmodel import Relationship, SQLModel, Field, Column
from sqlalchemy import JSON
from sqlalchemy.types import Integer

class StepsTable(SQLModel, table=True):
    __tablename__ = "steps"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer(6), primary_key=True))
    position: int
    image_url: Optional[str] = Field(default=None)
    description: str
    marker: dict = Field(sa_type=JSON())
    tutorials_id: int = Field(default=None, foreign_key="tutorials.id")
    tutorials: "TutorialsTable" = Relationship(back_populates="steps")


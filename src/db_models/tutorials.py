from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship, Column
from sqlalchemy.types import Integer


class TutorialsTable(SQLModel, table=True):
    __tablename__ = "tutorials"

    id: Optional[int] = Field(default=None, sa_column=Column(Integer, primary_key=True))
    name: str
    created_date_time: str
    steps: List["StepsTable"] = Relationship(back_populates="tutorials")
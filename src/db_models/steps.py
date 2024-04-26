from typing import Optional, Dict
from sqlmodel import Relationship, SQLModel, Field

class StepsTable(SQLModel, table=True):
    __tablename__ = "steps"

    id: Optional[int] = Field(default=None, primary_key=True)
    position: int
    image_path: Optional[str] = Field(default=None)
    description: str
    marker: Dict[str,str]
    tutorials_id: int = Field(default=None, foreign_key="tutorials.id")
    tutorials: "TutorialsTable" = Relationship(back_populates="steps")


from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class TutorialsTable(SQLModel, table=True):
    __tablename__ = "tutorials"

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str
    challenge_id: str
    text: Optional[str] = Field(default=None)
    image_path: Optional[str] = Field(default=None)
    steps: List["StepsTable"] = Relationship(back_populates="tutorials")
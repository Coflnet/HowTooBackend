from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from src.api_models.tutorial import Tutorials, UpdateTutorials
from src.api_models.step import Steps
from src.db_models.steps import StepsTable
from src.db.session import get_db
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=["Users"])


@router.post("/api/tutorials")
async def create_new_tutorial_with_steps(
    steps: List[Steps],
    db: Session = Depends(get_db),
) -> List[Steps]:
    # db_users = db.exec(select(TutorialsTable)).all()
    # return db_users
    return


@router.get("/api/tutorials/{tutorial_id}")
async def get_list_of_steps_from_tutorial_id(
    tutorial_id: str,
    db: Session = Depends(get_db),
) -> Tutorials:
    # db_user = db.exec(select(TutorialsTable).where(TutorialsTable.id == tutorial_id)).first()
    # return db_user
    return
    

@router.get("/api/tutorials")
async def get_all_tutorials(
    db: Session = Depends(get_db),
) -> List[Tutorials]:
    # db_user = db.exec(select(TutorialsTable).where(TutorialsTable.id == tutorial_id)).first()
    # return db_user
    return


@router.put("/api/tutorials/{tutorial_id}")
async def update_steps_of_a_tutorial(
    tutorial_id: str,
    steps: List[Steps],
    db: Session = Depends(get_db),
) -> UpdateTutorials:
    # try:
    #     db.add(user)
    # except IntegrityError:
    #     raise HTTPException(status_code=400, detail="Username or email already exists.")
    # db.commit()
    # db.refresh(user)
    # return user
    return
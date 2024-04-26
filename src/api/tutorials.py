from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from src.db_models.tutorials import TutorialsTable
from src.db_models.steps import StepsTable
from src.db.session import get_db
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=["Users"])


@router.post("/api/tutorials")
async def get_all_users(
    db: Session = Depends(get_db),
) -> List[TutorialsTable]:
    # db_users = db.exec(select(TutorialsTable)).all()
    # return db_users
    return


@router.get("/api/tutorials/{tutorial_id}")
async def get_user_by_id(
    tutorial_id: str,
    db: Session = Depends(get_db),
) -> TutorialsTable:
    # db_user = db.exec(select(TutorialsTable).where(TutorialsTable.id == tutorial_id)).first()
    # return db_user
    return
    

@router.get("/api/tutorials")
async def get_user_by_id(
    tutorial_id: str,
    db: Session = Depends(get_db),
) -> TutorialsTable:
    # db_user = db.exec(select(TutorialsTable).where(TutorialsTable.id == tutorial_id)).first()
    # return db_user
    return


@router.put("/api/tutorials")
async def post_new_users(
    user: TutorialsTable,
    db: Session = Depends(get_db),
) -> TutorialsTable:
    # try:
    #     db.add(user)
    # except IntegrityError:
    #     raise HTTPException(status_code=400, detail="Username or email already exists.")
    # db.commit()
    # db.refresh(user)
    # return user
    return
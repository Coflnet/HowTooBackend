from typing import List
import boto3
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from src.db.s3 import upload_file
from src.db_models.tutorials import TutorialsTable
from src.db_models.steps import StepsTable
from fastapi import APIRouter, Depends, HTTPException, status
from src.api_models.tutorial import Tutorials, PostTutorials
from src.db.session import get_db
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError

router = APIRouter(tags=["Users"])


@router.post("/api/tutorials", status_code=status.HTTP_200_OK)
async def create_new_tutorial_with_steps(
    tutorial: PostTutorials,
    db: Session = Depends(get_db),
) -> int:
    # db_users = db.exec(select(TutorialsTable)).all()
    # return db_users
    return


@router.get("/api/tutorials/{tutorial_id}", status_code=status.HTTP_200_OK)
async def get_list_of_steps_from_tutorial_id(
    tutorial_id: int,
    db: Session = Depends(get_db),
) -> Tutorials:
    # db_user = db.exec(select(TutorialsTable).where(TutorialsTable.id == tutorial_id)).first()
    # return db_user
    return
    

@router.get("/api/tutorials", status_code=status.HTTP_200_OK)
async def get_all_tutorials(
    db: Session = Depends(get_db),
) -> List[Tutorials]:
    # db_user = db.exec(select(TutorialsTable).where(TutorialsTable.id == tutorial_id)).first()
    # return db_user
    return


@router.put("/api/tutorials", status_code=status.HTTP_200_OK)
async def update_tutorial_and_steps(
    tutorial: Tutorials,
    db: Session = Depends(get_db),
) -> int:
    # try:
    #     db.add(user)
    # except IntegrityError:
    #     raise HTTPException(status_code=400, detail="Username or email already exists.")
    # db.commit()
    # db.refresh(user)
    # return user
    return
@router.post("/api/test-image-upload")
async def upload_test_image(
        file: UploadFile = File(...),
):
    upload_file(file)
    return {"filename": file.filename}




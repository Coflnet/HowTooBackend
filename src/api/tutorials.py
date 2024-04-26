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

router = APIRouter(tags=["Tutorials"])


@router.post("/api/tutorials", status_code=status.HTTP_200_OK)
async def create_new_tutorial_with_steps(
    tutorial: PostTutorials,
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db),
) -> int:
    tutorials_entry = TutorialsTable(
        name= tutorial.name,
        created_date_time = tutorial.created_date_time
    )
    db.add(tutorials_entry)
    db.commit()
    db.refresh(tutorials_entry)
    
    for step in tutorial.steps:
        for file in files:
            if step.file_name == file.filename:
                file_path = upload_file(file)
            else:
                file_path = None
        step_entry = StepsTable(
            position=step.position,
            image_path=file_path,
            description=step.description,
            marker=step.marker,
            tutorials_id=tutorials_entry.id,
        )
    db.add(step_entry)
    db.commit()
    db.refresh(step_entry)
    return

# @router.post("/api/test-image-upload")
# async def upload_test_image(
#         file: UploadFile = File(...),
# ):
#     upload_file(file)
#     return {"filename": file.filename}


@router.get("/api/tutorials/{tutorial_id}", status_code=status.HTTP_200_OK)
async def get_list_of_steps_from_tutorial_id(
    tutorial_id: int,
    db: Session = Depends(get_db),
) -> TutorialsTable:
# ) -> Tutorials:
    tutorial_entry = db.exec(select(TutorialsTable).where(TutorialsTable.id == tutorial_id)).first()
    return tutorial_entry
    

@router.get("/api/tutorials", status_code=status.HTTP_200_OK)
async def get_all_tutorials(
    db: Session = Depends(get_db),
) -> List[Tutorials]:

    tutorial_entries = db.exec(select(TutorialsTable)).all()
    return tutorial_entries


@router.put("/api/tutorials", status_code=status.HTTP_200_OK)
async def update_tutorial_and_steps(
    tutorial: Tutorials,
    db: Session = Depends(get_db),
) -> int:
    # tutorial_entry = db.exec(select(TutorialsTable).where(TutorialsTable.id == tutorial.id)).first()
    # tutorial_entry.name = tutorial.name
    # tutorial_entry.created_date_time = tutorial.created_date_time
    # db.add(tutorial_entry)
    # db.commit()
    # for step in tutorial.steps:
    #     step_entry = db.exec(select(StepsTable).where(StepsTable.id == tutorial.id)).first()
    #     step_entry.GetSteps

    return





from typing import List
import boto3
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from src.db.s3 import upload_file
from src.db_models.tutorials import TutorialsTable
from src.db_models.steps import StepsTable
from fastapi import APIRouter, Depends, HTTPException, status
from src.api_models.tutorial import Tutorials, GetSteps
from src.db.session import get_db
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError
import json
import random

router = APIRouter(tags=["Tutorials"])


@router.post("/api/tutorials", status_code=status.HTTP_200_OK)
async def create_new_tutorial_with_steps(
    tutorial_str: str = Form(...),  # PostTutorials
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db),
) -> int:
    try:
        tutorial = json.loads(tutorial_str)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON in Form field")

    tutorials_entry = TutorialsTable(
        id=random.randint(100_000_000, 999_999_999),
        name=tutorial["name"],
        created_date_time=tutorial["created_date_time"],
    )
    db.add(tutorials_entry)
    db.commit()
    db.refresh(tutorials_entry)

    for step in tutorial["steps"]:
        for file in files:
            if step["file_name"] == file.filename:
                file_path = upload_file(file)
                continue
            else:
                file_path = None
        step_entry = StepsTable(
            id=random.randint(100_000_000, 999_999_999),
            position=step["position"],
            image_url=file_path,
            description=step["description"],
            marker=step["marker"],
            tutorials_id=tutorials_entry.id,
        )
        db.add(step_entry)
        db.commit()
        db.refresh(step_entry)
    return 200


@router.get("/api/tutorials/{tutorial_id}", status_code=status.HTTP_200_OK)
async def get_list_of_steps_from_tutorial_id(
    tutorial_id: int,
    db: Session = Depends(get_db),
) -> Tutorials:
    tutorial_entry = db.exec(
        select(TutorialsTable).where(TutorialsTable.id == tutorial_id)
    ).first()
    step_entries = db.exec(
        select(StepsTable).where(StepsTable.tutorials_id == tutorial_id)
    ).all()
    steps: List[GetSteps] = []
    for step in step_entries:
        steps.append(
            GetSteps(
                id=step.id,
                position=step.position,
                image_url=step.image_url or None,
                description=step.description,
                marker=step.marker,
            )
        )
    tutorial = Tutorials(
        id=tutorial_id,
        name=tutorial_entry.name,
        created_date_time=tutorial_entry.created_date_time,
        steps=steps,
    )
    return tutorial


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
    tutorial_entry = db.exec(
        select(TutorialsTable).where(TutorialsTable.id == tutorial.id)
    ).first()
    tutorial_entry.name = tutorial.name
    tutorial_entry.created_date_time = tutorial.created_date_time
    db.add(tutorial_entry)
    db.commit()
    step_entries = db.exec(
        select(StepsTable).where(StepsTable.tutorials_id == tutorial.id)
    ).all()
    existing_step_ids = {step.id for step in tutorial.steps}
    new_steps = [step for step in step_entries if step.id not in existing_step_ids]
    for step in new_steps:
        db.delete(step)
    for step in tutorial.steps:
        step_entry = db.exec(
            select(StepsTable).where(StepsTable.tutorials_id == tutorial.id)
        ).first()
        step_entry.position = step.position
        step_entry.image_url = step.image_url
        step_entry.description = step.description
        step_entry.marker = step.marker
        db.add(step_entry)
        db.commit()
    return 200

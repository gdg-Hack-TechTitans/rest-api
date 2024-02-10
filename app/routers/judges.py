from fastapi import APIRouter

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from ..schemas import judges_schemas
from ..crud import judges_crud


judges_router = APIRouter()

@judges_router.post("/v1/judges/", response_model=judges_schemas.JudgeWithPassword, status_code=201)
def create_judge(judge: judges_schemas.JudgeCreate, db: Session = Depends(get_db)):
    created_judges, random_password = judges_crud.create_judge(db=db, judge=judge)

    # Instead of returning a dictionary, return an instance of JudgeWithPassword
    response_judges = judges_schemas.JudgeWithPassword(
        id=created_judges.id,
        name=created_judges.name,
        email=created_judges.email,
        password=random_password
    )

    return response_judges

@judges_router.get("/v1/judges/", response_model=list[judges_schemas.Judge])
def get_judges(skip:int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return judges_crud.get_all_judges(db, skip, limit)


@judges_router.get("/v1/judges/{judges_id}/", response_model=judges_schemas.Judge)
def get_judge(judges_id: int , db: Session = Depends(get_db)):
    db_judges = judges_crud.get_judge(db,judge_id=judges_id)
    print(db_judges)
    if db_judges is None: 
        raise HTTPException(status_code=404, detail="User not found")
    return db_judges

@judges_router.delete("/v1/judges/{judges_id}/", response_model=judges_schemas.Judge)
def delete_judge(judges_id: int , db: Session = Depends(get_db)):
    return judges_crud.delete_judge(db, judge_id=judges_id)

@judges_router.put("/v1/judges/{judges_id}/", response_model=judges_schemas.Judge)
def update_judge(judges_id: int ,judge: judges_schemas.JudgeCreate, db: Session = Depends(get_db)):
    return judges_crud.update_judge(db, judge_id=judges_id, updated_judge=judge)

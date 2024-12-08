from fastapi import APIRouter, FastAPI, Depends, HTTPException, status

from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from ..oauth2 import get_current_user

router = APIRouter(
     prefix="/users",
     tags=['Users']

)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model= schemas.UserOut,)
def get_user(id:int,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

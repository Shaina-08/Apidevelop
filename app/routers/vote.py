from fastapi import FastAPI,APIRouter, Response,HTTPException, status, APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from typing import List, Optional
from ..oauth2 import get_current_user
router = APIRouter(
    prefix="/votes",
    tags=['Votes']
)
@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    vote_query=db.query(models.Vote).filter(models.Vote.post_id == vote.post_id , models.Vote.user_id == current_user.id)
    found_vote= vote_query.first()
    if(vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="You have already voted for this post")
        new_vote=models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"Vote registered"}

    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You have not voted for this post")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"Vote deleted"}
    return {"message":"Vote registered"}

        
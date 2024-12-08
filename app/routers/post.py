
from fastapi import FastAPI, Depends,APIRouter, Response,HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from typing import List, Optional
from ..oauth2 import get_current_user
from sqlalchemy import func



router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),current_user: int = Depends(get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""
 ):
    post = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    results = db.query(models.Post,func.count(models.Vote.post_id).label("Votes") ).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    print(results)
    return results
   


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post : schemas.PostCreate,db: Session = Depends(get_db), current_user: int = Depends(get_current_user) ):
    new_post = models.Post(owner_id = current_user.id,**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    

@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    # Query to fetch the post and vote count
    post_with_votes = (
        db.query(models.Post, func.count(models.Vote.post_id).label("Votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.id == id)
        .first()
    )

    if not post_with_votes:
        raise HTTPException(status_code=404, detail="Post not found")
    
   
    post, votes = post_with_votes

    #
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform requested action")
    
    
    return {"Post": post, "Votes": votes}

@router.delete("/{id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),current_user: int = Depends(get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id==id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform requested action")
    

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int , post:schemas.PostCreate,db: Session = Depends(get_db),current_user: int = Depends(get_current_user)):

    post_get = db.query(models.Post).filter(models.Post.id==id)
    post = post_get.first()
    if not post:
        raise HTTPException(status_code=404, detail=f"Not Found {id}")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform requested action")
    

    post_get.update(post.model_dump(), synchronize_session=False)
    db.commit()
   
    return post_get.first()

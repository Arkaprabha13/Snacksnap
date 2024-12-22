from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import crud
from ..db.models import Like
from ..core.auth import verify_token
from ..core.db import get_db

router = APIRouter()

# Like a recipe
@router.post("/")
def like_recipe(recipe_id: int, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    existing_like = db.query(Like).filter(Like.recipe_id == recipe_id, Like.user_id == token['sub']).first()
    if existing_like:
        raise HTTPException(status_code=400, detail="You've already liked this recipe")
    
    like = Like(recipe_id=recipe_id, user_id=token['sub'])
    db.add(like)
    db.commit()
    db.refresh(like)
    return like

# Get likes for a recipe
@router.get("/{recipe_id}")
def get_likes(recipe_id: int, db: Session = Depends(get_db)):
    likes = db.query(Like).filter(Like.recipe_id == recipe_id).all()
    return {"likes_count": len(likes)}

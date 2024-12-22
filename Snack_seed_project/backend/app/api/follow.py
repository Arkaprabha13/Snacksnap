from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import crud
from ..db.models import Follow
from ..core.auth import verify_token
from ..core.db import get_db

router = APIRouter()

# Follow a user
@router.post("/")
def follow_user(followed_user_id: int, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    existing_follow = db.query(Follow).filter(Follow.follower_user_id == token['sub'], Follow.followed_user_id == followed_user_id).first()
    if existing_follow:
        raise HTTPException(status_code=400, detail="You're already following this user")
    
    follow = Follow(follower_user_id=token['sub'], followed_user_id=followed_user_id)
    db.add(follow)
    db.commit()
    db.refresh(follow)
    return follow

# Get followers of a user
@router.get("/followers/{user_id}")
def get_followers(user_id: int, db: Session = Depends(get_db)):
    followers = db.query(Follow).filter(Follow.followed_user_id == user_id).all()
    return followers

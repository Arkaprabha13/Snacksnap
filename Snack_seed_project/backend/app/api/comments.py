
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import crud
from ..db.models import Comment
from ..core.auth import verify_token
from ..core.db import get_db

router = APIRouter()

# Add a comment
@router.post("/")
def add_comment(comment: Comment, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    comment.user_id = token['sub']
    db_comment = crud.create_comment(db, comment)
    return db_comment

# Get comments for a specific recipe
@router.get("/{recipe_id}")
def get_comments(recipe_id: int, db: Session = Depends(get_db)):
    comments = db.query(Comment).filter(Comment.recipe_id == recipe_id).all()
    return comments

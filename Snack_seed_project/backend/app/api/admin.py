from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import crud
from ..db.models import Recipe, User
from ..core.auth import verify_token
from ..core.db import get_db
from ..core.permissions import AdminPermission

router = APIRouter()

# Admin can delete any recipe
@router.delete("/recipe/{recipe_id}")
def delete_recipe(recipe_id: int, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    if not AdminPermission(token):
        raise HTTPException(status_code=403, detail="Not authorized")
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    
    db.delete(recipe)
    db.commit()
    return {"message": "Recipe deleted successfully"}

# Admin can get all users
@router.get("/users")
def get_users(token: str = Depends(verify_token), db: Session = Depends(get_db)):
    if not AdminPermission(token):
        raise HTTPException(status_code=403, detail="Not authorized")
    users = db.query(User).all()
    return users

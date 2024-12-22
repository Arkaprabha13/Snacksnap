from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import crud
from ..db.models import Recipe
from ..core.auth import verify_token
from ..core.db import get_db

router = APIRouter()

# Create a new recipe
@router.post("/")
def create_recipe(recipe: Recipe, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    recipe.user_id = token['sub']
    db_recipe = crud.create_recipe(db, recipe)
    return db_recipe

# Get all recipes
@router.get("/")
def get_recipes(db: Session = Depends(get_db)):
    recipes = db.query(Recipe).all()
    return recipes

# Get a single recipe by ID
@router.get("/{recipe_id}")
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

# Update a recipe
@router.put("/{recipe_id}")
def update_recipe(recipe_id: int, recipe: Recipe, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe or db_recipe.user_id != token['sub']:
        raise HTTPException(status_code=404, detail="Recipe not found or you're not the owner")
    
    db_recipe.title = recipe.title
    db_recipe.ingredients = recipe.ingredients
    db_recipe.instructions = recipe.instructions
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

# Delete a recipe
@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    db_recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not db_recipe or db_recipe.user_id != token['sub']:
        raise HTTPException(status_code=404, detail="Recipe not found or you're not the owner")
    
    db.delete(db_recipe)
    db.commit()
    return {"message": "Recipe deleted successfully"}

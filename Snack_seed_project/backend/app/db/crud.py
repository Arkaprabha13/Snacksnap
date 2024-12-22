from sqlalchemy.orm import Session
from .models import User, Recipe, Comment

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_recipe(db: Session, recipe: Recipe):
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    return recipe

def create_comment(db: Session, comment: Comment):
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..core.auth import hash_password, create_access_token, verify_password
from ..db import crud
from ..db.models import User
from ..core.db import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
def register(user: User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user.password = hash_password(user.password)
    db_user = crud.create_user(db=db, user=user)
    return {"message": "User created successfully"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

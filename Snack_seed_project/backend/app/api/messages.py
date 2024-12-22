from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import crud
from ..db.models import Message
from ..core.auth import verify_token
from ..core.db import get_db

router = APIRouter()

# Send a message
@router.post("/")
def send_message(message: Message, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    message.sender_id = token['sub']
    db_message = crud.create_message(db, message)
    return db_message

# Get messages for the authenticated user
@router.get("/")
def get_messages(token: str = Depends(verify_token), db: Session = Depends(get_db)):
    messages = db.query(Message).filter(Message.receiver_id == token['sub']).all()
    return messages

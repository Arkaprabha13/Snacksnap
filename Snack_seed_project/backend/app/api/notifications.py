from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import crud
from ..db.models import Notification
from ..core.auth import verify_token
from ..core.db import get_db

router = APIRouter()

# Get notifications for the authenticated user
@router.get("/")
def get_notifications(token: str = Depends(verify_token), db: Session = Depends(get_db)):
    notifications = db.query(Notification).filter(Notification.user_id == token['sub']).all()
    return notifications

# Create a notification (e.g., for likes, comments)
@router.post("/")
def create_notification(notification: Notification, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    notification.user_id = token['sub']
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification

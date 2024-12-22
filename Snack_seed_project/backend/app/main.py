from fastapi import FastAPI
from .api import users, recipes, comments, likes, messages, follow, notifications, admin
from .core.config import settings
from .db import models, session
from .db.session import engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(recipes.router, prefix="/recipes", tags=["Recipes"])
app.include_router(comments.router, prefix="/comments", tags=["Comments"])
app.include_router(likes.router, prefix="/likes", tags=["Likes"])
app.include_router(messages.router, prefix="/messages", tags=["Messages"])
app.include_router(follow.router, prefix="/follow", tags=["Follow"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

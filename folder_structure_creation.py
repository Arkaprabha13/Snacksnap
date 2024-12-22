import os

def create_structure(base_path):
    # Define the folder structure as a dictionary
    folder_structure = {
        "backend": {
            "app": {
                "api": [
                    "users.py", "recipes.py", "comments.py", "likes.py", "messages.py", 
                    "follow.py", "notifications.py", "admin.py"
                ],
                "core": [
                    "auth.py", "config.py", "permissions.py", "hashing.py"
                ],
                "db": [
                    "models.py", "crud.py", "schemas.py", "session.py", "migrations"
                ],
                "services": [
                    "recipe_service.py", "comment_service.py", "like_service.py", 
                    "message_service.py", "follow_service.py", "notification_service.py"
                ],
                "templates": [],
                "tests": [
                    "test_auth.py", "test_recipe.py", "test_comments.py", "test_likes.py"
                ],
                "main.py": None,
            },
            "Dockerfile": None,
            "requirements.txt": None,
            "alembic.ini": None
        },
        "frontend": {
            "public": {
                "index.html": None,
                "assets": []
            },
            "src": {
                "components": [
                    "RecipeCard.js", "RecipeForm.js", "Comment.js", "LikeButton.js", 
                    "Message.js", "Navbar.js", "FollowButton.js", "Notification.js", 
                    "ScrollToTopButton.js"
                ],
                "context": [
                    "AuthContext.js", "RecipeContext.js", "MessageContext.js", 
                    "FollowContext.js", "NotificationContext.js"
                ],
                "hooks": [
                    "useAuth.js", "useRecipes.js", "useComments.js", "useLikes.js", 
                    "useMessages.js", "useNotifications.js"
                ],
                "pages": [
                    "HomePage.js", "ProfilePage.js", "RecipePage.js", "LoginPage.js", 
                    "RegisterPage.js", "MessagesPage.js", "FollowersPage.js"
                ],
                "services": [
                    "api.js", "recipeService.js", "userService.js", "commentService.js", 
                    "likeService.js", "followService.js", "messageService.js", 
                    "notificationService.js"
                ],
                "App.js": None,
                "index.js": None,
                "App.css": None,
                "package.json": None
            }
        }
    }
    
    # Function to create directories and files
    def create_files(path, structure):
        for key, value in structure.items():
            if isinstance(value, dict):
                # Create the directory
                dir_path = os.path.join(path, key)
                os.makedirs(dir_path, exist_ok=True)
                create_files(dir_path, value)
            elif isinstance(value, list):
                for file_name in value:
                    # Create the file
                    file_path = os.path.join(path, key, file_name)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    open(file_path, 'w').close()  # Create an empty file
            else:
                # Create a single file (e.g., Dockerfile, main.py)
                file_path = os.path.join(path, key)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                open(file_path, 'w').close()  # Create an empty file

    # Start creating the structure from the base path
    create_files(base_path, folder_structure)
    print(f"Folder structure created at {base_path}")

# Define the base path where you want to create the folder structure
base_path = "Snack_seed_project"  # Change this to your desired path

# Create the folder structure
create_structure(base_path)

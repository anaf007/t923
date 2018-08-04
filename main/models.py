from main.extensions import login_manager
from main.user.models import User

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))
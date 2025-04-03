from app.models.user import User

class UserService:
  async def get_user(self, user_id: int) -> User:
    return User(id=user_id, name="John Doe")
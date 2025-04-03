from fastapi import APIRouter, Depends
from app.services.user_service import UserService
from app.core.auth import roles_required
from app.core.dependencies import get_user_service
from app.models.user import User
from app.core.logging_config import log_error

router = APIRouter()

@router.get("/user/{user_id}", response_model=User)
@roles_required(roles=["Admin"])
async def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):
  try:
    return await user_service.get_user(user_id)
  except Exception as e:
    log_error(e)
    raise e
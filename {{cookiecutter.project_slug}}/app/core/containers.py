from app.services.user_service import UserService
from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
  user_service = providers.Factory(UserService)

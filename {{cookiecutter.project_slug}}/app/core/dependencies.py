from fastapi import Depends
from app.services.user_service import UserService

def get_user_service() -> UserService:
  return UserService()

# app/containers.py
from dependency_injector import containers, providers
from app.services.user_service import UserService

class Container(containers.DeclarativeContainer):
  user_service = providers.Factory(UserService)
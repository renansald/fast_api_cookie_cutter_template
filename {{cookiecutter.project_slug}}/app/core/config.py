from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
  APP_NAME: str
  DESCRIPTION: str
  VERSION: str
  DEBUG: bool = True
  DATABASE_URL: str
  OKTA_ISSUE: str
  OKTA_AUDIENCE: str
  OKTA_CLIENT_ID: str
  AZURE_APP_INSIGTHS_CONNECTION_STRING: str

  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"

settings = Settings()
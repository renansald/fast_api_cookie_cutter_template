from fastapi import Depends, HTTPException, Request
from okta_jwt_verifier import BaseJWTVerifier
from typing import List
from app.core.config import settings
from functools import wraps
from app.middlewares.request_context import request_context
from .config import settings
from .logging_config import log_error

def get_token_from_header(request: Request) -> str:
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    return auth_header.split(" ")[1]

async def validate_access_token(access_token):
    try:
        baseJWTVerifier = BaseJWTVerifier(settings.OKTA_ISSUE, settings.OKTA_CLIENT_ID,settings.OKTA_AUDIENCE)
        await baseJWTVerifier.verify_access_token(access_token)
        return baseJWTVerifier.parse_token(access_token)[1].get("roles", [])
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

def roles_required(roles: List[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                request: Request = request_context.get()
                if request is None:
                    raise HTTPException(status_code=401, detail="Request context not found")
                token = get_token_from_header(request)
                user_roles = await validate_access_token(token)
                if not any(role in user_roles for role in roles):
                    raise HTTPException(status_code=403, detail="Not enough permissions")
                return await func(*args, **kwargs)
            except Exception as e:
                log_error(e)
                raise e
        return wrapper
    return decorator

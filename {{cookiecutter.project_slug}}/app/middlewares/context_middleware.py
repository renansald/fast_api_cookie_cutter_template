from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from .request_context import request_context

class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_context.set(request)
        try:
            response = await call_next(request)
        finally:
            request_context.set(None)
        return response
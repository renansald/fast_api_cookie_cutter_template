import contextvars
from fastapi import Request

request_context: contextvars.ContextVar[Request] = contextvars.ContextVar("request_context", default=None)
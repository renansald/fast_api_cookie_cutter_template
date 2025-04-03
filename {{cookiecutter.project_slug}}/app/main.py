from fastapi import FastAPI
import logging
from app.routes import register_routes
from fastapi.middleware.cors import CORSMiddleware
from app.core.containers import Container
from app.core.config import settings
from app.middlewares.context_middleware import RequestContextMiddleware
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.asgi import OpenTelemetryMiddleware
from app.core.app_insigths import azure_monitor

def create_app() -> FastAPI:
  logging.getLogger("azure").setLevel(logging.WARNING)

  origins = [
    "http://localhost:3000"
  ]

  container = Container()
  app = FastAPI(
    title=settings.APP_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
  )
  app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

  app.add_middleware(OpenTelemetryMiddleware)
  app.add_middleware(RequestContextMiddleware)
  FastAPIInstrumentor.instrument_app(app, tracer_provider=azure_monitor.tracer_provider)
  
  app.container = container
  register_routes(app)
  return app

app = create_app()
from loguru import logger
from opencensus.ext.azure.log_exporter import AzureLogHandler
import datetime
import traceback
from app.middlewares.request_context import request_context
from .config import settings
import json

logger.remove() 
logger.add(
    AzureLogHandler(connection_string=settings.AZURE_APP_INSIGTHS_CONNECTION_STRING), 
    level="INFO",
    serialize=True
)

def log_error(exception: Exception):
    request = request_context.get()
    error_data = {
        "requestId": request.headers.get("X-Request-Id", "unknown"),
        "message": str(exception),
        "stackTrace": traceback.format_exc(),
        "datetime": datetime.datetime.utcnow().isoformat(),
        "level": "ERROR",
    }
    logger.error(json.dumps(error_data))

def log_info(message: str):
    """Logs informational messages."""
    request = request_context.get()
    log_data = {
        "requestId": request.headers.get("X-Request-Id", "unknown"),
        "message": message,
        "datetime": datetime.datetime.utcnow().isoformat(),
        "level": "INFO",
    }
    logger.info(json.dumps(log_data))

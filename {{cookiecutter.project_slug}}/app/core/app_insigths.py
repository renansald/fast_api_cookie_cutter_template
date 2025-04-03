from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry import trace
from app.core.config import settings

class AzureMonitor:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AzureMonitor, cls).__new__(cls)
            
            cls._instance.tracer_provider = TracerProvider(
                resource=Resource.create({"service.name": settings.APP_NAME})
            )
            
            exporter = AzureMonitorTraceExporter(
                connection_string=settings.AZURE_APP_INSIGTHS_CONNECTION_STRING
            )
            cls._instance.tracer_provider.add_span_processor(BatchSpanProcessor(exporter))
            
            trace.set_tracer_provider(cls._instance.tracer_provider)

            LoggingInstrumentor().instrument(set_logging_format=True)

            RequestsInstrumentor().instrument()
        
        return cls._instance

azure_monitor = AzureMonitor()

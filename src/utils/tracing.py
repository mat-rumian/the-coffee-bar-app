from opentelemetry import trace
from opentelemetry.ext.jaeger import JaegerSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
    BatchExportSpanProcessor,
)
import opentelemetry.ext.requests


def configure_jaeger_span_exporter(configuration: dict):
    exporter = JaegerSpanExporter(
        service_name=configuration['service_name'],
        agent_host_name=configuration['agent_host'],
        agent_port=int(configuration['agent_port']),
    )

    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer(__name__)

    span_processor = BatchExportSpanProcessor(exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    trace.get_tracer_provider().add_span_processor(
        SimpleExportSpanProcessor(ConsoleSpanExporter())
    )


def configure_jaeger_span_exporter_with_manual_requests(configuration: dict):
    exporter = JaegerSpanExporter(
        service_name=configuration['service_name'],
        agent_host_name=configuration['agent_host'],
        agent_port=int(configuration['agent_port']),
    )

    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer(__name__)

    span_processor = BatchExportSpanProcessor(exporter)
    trace.get_tracer_provider().add_span_processor(span_processor)

    trace.get_tracer_provider().add_span_processor(
        SimpleExportSpanProcessor(ConsoleSpanExporter())
    )

    # Manual req
    opentelemetry.ext.requests.RequestsInstrumentor().instrument()

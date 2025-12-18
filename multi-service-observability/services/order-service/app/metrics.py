from fastapi import APIRouter, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

metrics_router = APIRouter()

REQUEST_COUNT = Counter(
    "order_service_requests_total",
    "Total requests to order service"
)

@metrics_router.get("/metrics")
def metrics():
    REQUEST_COUNT.inc()
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

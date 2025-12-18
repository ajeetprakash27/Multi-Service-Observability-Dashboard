from fastapi import FastAPI
from app.routes import router
from app.health import health_router
from app.metrics import metrics_router

app = FastAPI(title="User Service")

app.include_router(router, prefix="/api")
app.include_router(health_router)
app.include_router(metrics_router)

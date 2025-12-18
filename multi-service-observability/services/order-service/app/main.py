from fastapi import FastAPI
from routes import router
from health import health_router
from metrics import metrics_router

app = FastAPI(title="Order Service")

app.include_router(router, prefix="/api")
app.include_router(health_router)
app.include_router(metrics_router)

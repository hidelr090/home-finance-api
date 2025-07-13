from fastapi import FastAPI
from app.router import api_router
from app.config import setup_env

from app.shared.middlewares import RateLimiterMiddleware

setup_env()

app = FastAPI()
app.include_router(api_router)
app.add_middleware(RateLimiterMiddleware, limit=20, window_seconds=60)


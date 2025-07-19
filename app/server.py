from fastapi import FastAPI
from app.router import api_router
from app.error_handler import application_error_handler
from app.shared.middlewares import RateLimiterMiddleware
from app.shared.utils.exceptions import ApplicationError
from starlette.middleware.sessions import SessionMiddleware
from app.config import get_env

app = FastAPI()
app.include_router(api_router)
app.add_exception_handler(ApplicationError, application_error_handler)
app.add_middleware(RateLimiterMiddleware, limit=20, window_seconds=60)
app.add_middleware(SessionMiddleware, secret_key=get_env("SESSION_SECRET"))


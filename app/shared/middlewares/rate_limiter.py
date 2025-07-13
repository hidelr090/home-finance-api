from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response, HTTPException
from datetime import datetime, timedelta, timezone
from typing import Dict

class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, limit: int = 20, window_seconds: int = 60):
        super().__init__(app)
        self.limit = limit
        self.window_seconds = window_seconds
        self.requests: Dict[str, list[datetime]] = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host

        now = datetime.now(timezone.utc)
        window_start = now - timedelta(seconds=self.window_seconds)

        # Limpa requisições antigas
        self.requests.setdefault(client_ip, [])
        self.requests[client_ip] = [
            timestamp for timestamp in self.requests[client_ip]
            if timestamp > window_start
        ]

        if len(self.requests[client_ip]) >= self.limit:
            raise HTTPException(status_code=429, detail="Too Many Requests")

        self.requests[client_ip].append(now)

        response = await call_next(request)
        return response

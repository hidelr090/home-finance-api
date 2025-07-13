# app/dependencies/auth.py
from fastapi import Request, HTTPException, status, Depends
from datetime import datetime, timezone
from app.repositories.user_repository import UserRepository

async def auth_middleware(
    request: Request,
    user_repository: UserRepository = Depends(get_user_repository)
):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid token")

    token = auth_header.removeprefix("Bearer ").strip()

    user = await user_repository.get_user_by_token(token)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    if not user.token_expiration or user.token_expiration < datetime.now(timezone.utc):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Token expired")

    return user

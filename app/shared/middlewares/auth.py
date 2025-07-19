# app/dependencies/auth.py
from fastapi import Request, HTTPException, status, Depends
from datetime import datetime, timezone
from app.repositories.user_repository import UserRepository
from app.factories.repositories.user_repository_factory import user_repository_factory
from app.shared.types.session import AuthSession
from app.shared.utils.cryptography import decode as decoder
from box import Box

async def auth_middleware(
    request: Request,
    user_repository: UserRepository = Depends(user_repository_factory)
):
    auth_header = request.headers.get("authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Missing or invalid token")

    token = auth_header.split(" ")[1].strip()
    
    decoded_token = decoder(token)
    user_id = decoded_token.get("id") or decoded_token.get("id_1", {}).get("id")
    user = user_repository.get_by_id(user_id)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    if not user.token_expiration or user.token_expiration.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    
    session: AuthSession = Box({
        "user": {
            "id": user.id,
            "email": user.email
        },
        "token": token,
        "is_authenticated" : True
    })
    request.session.update(session)
    
    return user

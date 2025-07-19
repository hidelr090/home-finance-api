from typing import TypedDict

class SessionUser(TypedDict):
    id: int
    email: str

class AuthSession(TypedDict, total=False):
    user: SessionUser
    token: str
    is_authenticated: bool


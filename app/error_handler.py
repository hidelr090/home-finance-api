from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
import logging

from app.shared.utils.exceptions import (
    ApplicationError,
    AuthenticationError,
    AuthorizationError,
    ValidationError,
    NotFoundError,
    ConflictError,
    InfrastructureError,
    ServiceUnavailableError,
    RateLimitExceededError
)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api_errors")

async def application_error_handler(request: Request, exc: ApplicationError):
    logger.error(f"ApplicationError capturado na rota: {request.url}", exc_info=True)

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    error_message = exc.message
    error_code = exc.code if exc.code else "GENERIC_APPLICATION_ERROR"

    if isinstance(exc, AuthenticationError):
        status_code = status.HTTP_401_UNAUTHORIZED
        error_code = exc.code
        error_message = "Credenciais inválidas."
    elif isinstance(exc, AuthorizationError):
        status_code = status.HTTP_403_FORBIDDEN
        error_code = exc.code
        error_message = "Acesso negado para esta operação."
    elif isinstance(exc, NotFoundError):
        status_code = status.HTTP_404_NOT_FOUND
        error_code = exc.code
        error_message = exc.message
    elif isinstance(exc, ConflictError):
        status_code = status.HTTP_409_CONFLICT
        error_code = exc.code
        error_message = exc.message
    elif isinstance(exc, ValidationError):
        status_code = status.HTTP_400_BAD_REQUEST
        error_code = exc.code
        error_message = exc.message
    elif isinstance(exc, RateLimitExceededError):
        status_code = status.HTTP_429_TOO_MANY_REQUESTS
        error_code = exc.code
        error_message = exc.message
    elif isinstance(exc, ServiceUnavailableError):
        status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        error_code = exc.code
        error_message = "O serviço está temporariamente indisponível. Tente novamente mais tarde."
    elif isinstance(exc, InfrastructureError):
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        error_code = exc.code
        error_message = "Um erro interno de infraestrutura ocorreu. Tente novamente mais tarde."

    return JSONResponse(
        status_code=status_code,
        content={"message": error_message, "code": error_code}
    )
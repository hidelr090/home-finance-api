from typing import Optional


class ApplicationError(Exception):
    def __init__(self, message: str = "An application error occurred.", code: Optional[str] = None):
        self.message = message
        self.code = code
        super().__init__(message)


class BusinessError(ApplicationError):
    def __init__(self, message: str = "A business rule was violated.", code: Optional[str] = "BUS_000"):
        super().__init__(message, code)


class AuthenticationError(BusinessError):
    def __init__(self, message: str = "Invalid credentials.", code: str = "AUTH_001", original_error: Optional[Exception] = None):
        self.original_error = original_error
        display_message = message
        if original_error:
            display_message = f"{message} (Details: {original_error})"
        super().__init__(display_message, code)


class AuthorizationError(BusinessError):
    def __init__(self, message: str = "Forbidden access.", code: str = "AUTH_003"):
        super().__init__(message, code)


class ValidationError(BusinessError):
    def __init__(self, message: str = "Input data is invalid.", code: str = "VAL_001", details: Optional[dict] = None):
        self.details = details
        super().__init__(message, code)


class RepositoryError(ApplicationError):
    def __init__(self, message: str = "A repository error occurred.", code: Optional[str] = "REPO_000"):
        super().__init__(message, code)


class NotFoundError(RepositoryError):
    def __init__(self, entity_name: str, identifier: any, message: Optional[str] = None, code: str = "REPO_404"):
        if message is None:
            message = f"{entity_name} with identifier '{identifier}' not found."
        self.entity_name = entity_name
        self.identifier = identifier
        super().__init__(message, code)


class ConflictError(RepositoryError):
    def __init__(self, message: str = "Data conflict occurred.", code: str = "REPO_409"):
        super().__init__(message, code)


class InfrastructureError(ApplicationError):
    def __init__(self, message: str = "An infrastructure error occurred.", code: str = "INFRA_500", original_error: Optional[Exception] = None):
        self.original_error = original_error
        display_message = message
        if original_error:
            display_message = f"{message} (Details: {type(original_error).__name__}: {original_error})"
        super().__init__(display_message, code)


class ServiceUnavailableError(InfrastructureError):
    def __init__(self, message: str = "Service is temporarily unavailable.", code: str = "INFRA_503", original_error: Optional[Exception] = None):
        super().__init__(message, code, original_error)


class RateLimitExceededError(BusinessError):
    def __init__(self, message: str = "Rate limit exceeded.", code: str = "RATE_429"):
        super().__init__(message, code)
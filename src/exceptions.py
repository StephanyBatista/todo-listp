class BusinessError(Exception):
    """Base class for business errors."""

    def __init__(self, message: str):
        super().__init__(message)


class NotFoundError(Exception):
    """Raised when a requested resource is not found."""

    def __init__(self, message: str):
        super().__init__(message)

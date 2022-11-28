class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404

class NotAuthorized(BaseServiceError):
    code = 401

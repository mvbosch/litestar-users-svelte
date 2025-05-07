from uuid import uuid4

from litestar import Request, get

from .schemas import UiConfig


@get("/config", exclude_from_auth=True)
def get_config(request: Request) -> UiConfig:
    """
    Get the UI configuration.
    """
    session_id = str(uuid4())
    request.set_session({"session_id": session_id})
    return UiConfig(session_id=session_id)

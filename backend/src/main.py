from litestar import Litestar

from src.config import settings
from src.config.server import openapi_config
from src.server.controllers import main_router
from src.server.plugins import plugins

app = Litestar(
    debug=settings.app.DEBUG,
    plugins=plugins,
    route_handlers=[main_router],
    openapi_config=openapi_config,
)

from litestar import Router

from src.domain.system.controllers import get_config
from src.domain.users.controllers import token_notifier

main_router = Router("/api", route_handlers=[token_notifier, get_config])

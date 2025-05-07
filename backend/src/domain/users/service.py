from typing import Any, TYPE_CHECKING

from litestar_users.service import BaseUserService
from litestar.channels import ChannelsPlugin

from src.db.models.user import User
from src.config import settings

if TYPE_CHECKING:
    from litestar import Request


class UserService(BaseUserService[User, Any, Any]):  # type: ignore[type-var]
    async def send_password_reset_token(self, user: User, token: str) -> None:
        """Since this example is public, we won't be sending email etc.

        Instead, we'll provide a link via websocket to keep the flow in browser.
        """

    async def post_registration_hook(self, user: User, request: "Request | None" = None) -> None:
        token = self.generate_token(user_id=user.id, aud="verify")
        channels_plugin: ChannelsPlugin = request.app.plugins.get(ChannelsPlugin)
        channels_plugin.publish(
            data={"url": f"{settings.app.FRONTEND_BASE_URL}/verify?token={token}"},
            channels=request.session.get("session_id"),
        )

from typing import Any

from litestar_users.service import BaseUserService

from src.db.models.user import User
    
class UserService(BaseUserService[User, Any, Any]):  # type: ignore[type-var]
    async def send_password_reset_token(self, user: User, token: str) -> None:
        """Since this example is public, we won't be sending email etc.
        
        Instead, we'll provide a link via websocket to keep the flow in browser.
        """

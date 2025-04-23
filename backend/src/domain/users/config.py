from litestar_users import LitestarUsersConfig
from litestar.middleware.session.server_side import ServerSideSessionConfig
from litestar_users.config import (
    AuthHandlerConfig,
    CurrentUserHandlerConfig,
    PasswordResetHandlerConfig,
    RegisterHandlerConfig,
    UserManagementHandlerConfig,
    VerificationHandlerConfig,
)

from litestar.security.session_auth import SessionAuth
from src.config import settings
from src.db.models.user import User

from .service import UserService
from .schemas import UserReadDTO, UserRegistrationDTO, UserUpdateDTO

litestar_users_config = LitestarUsersConfig(
    auth_backend_class=SessionAuth,
    session_backend_config=ServerSideSessionConfig(),
    secret=settings.app.SECRET_KEY,
    user_model=User,  # pyright: ignore
    user_read_dto=UserReadDTO,
    user_registration_dto=UserRegistrationDTO,
    user_update_dto=UserUpdateDTO,
    user_service_class=UserService,  # pyright: ignore
    auth_handler_config=AuthHandlerConfig(),
    current_user_handler_config=CurrentUserHandlerConfig(),
    password_reset_handler_config=PasswordResetHandlerConfig(),
    register_handler_config=RegisterHandlerConfig(),
    user_management_handler_config=UserManagementHandlerConfig(),
    verification_handler_config=VerificationHandlerConfig(),
)

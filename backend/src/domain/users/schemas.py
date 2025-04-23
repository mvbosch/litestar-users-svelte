from dataclasses import dataclass

from advanced_alchemy.extensions.litestar.dto import SQLAlchemyDTO
from litestar.dto import DataclassDTO, DTOConfig

from src.db.models.user import User


@dataclass
class UserRegistrationSchema:
    email: str
    password: str


class UserRegistrationDTO(DataclassDTO[UserRegistrationSchema]):
    """User registration DTO."""


class UserReadDTO(SQLAlchemyDTO[User]):
    pass


class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = DTOConfig(partial=True)

from advanced_alchemy.base import UUIDBase

from litestar_users.adapter.sqlalchemy.mixins import SQLAlchemyUserMixin


class User(UUIDBase, SQLAlchemyUserMixin):
    """User model."""

from uuid import UUID

from msgspec import Struct


class UiConfig(Struct, rename="camel"):
    """UI configuration schema."""

    session_id: UUID

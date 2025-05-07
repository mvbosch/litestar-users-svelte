from dataclasses import InitVar, dataclass, field

from quicksettings import BaseSettings


@dataclass(init=False)
class ApplicationSettings(BaseSettings):
    """Provides application settings.

    Prefix environment variables with `APP_`.
    """

    env_prefix: InitVar[str] = "APP_"

    DEBUG: bool
    """Whether the application is in debug mode."""
    NAME: str
    """The name of the application."""
    VERSION: str
    """The version of the application."""
    ENVIRONMENT: str
    """The environment the application is running in."""
    LOG_LEVEL: str
    """The logging level for the application."""
    SECRET_KEY: str
    """The secret key for the application."""
    FRONTEND_BASE_URL: str
    """The base URL for the frontend application."""


@dataclass(init=False)
class DatabaseSettings(BaseSettings):
    """Provides database settings for the application.

    Prefix environment variables with `DATABASE_`.
    """

    env_prefix: InitVar[str] = "DATABASE_"

    URL: str
    """The URL for the database connection."""


@dataclass(init=False)
class OpenAPISettings(BaseSettings):
    """Provides OpenAPI settings for the application.

    Prefix environment variables with `OPENAPI_`.
    """

    env_prefix: InitVar[str] = "OPENAPI_"

    TITLE: str
    """The title of the OpenAPI documentation."""
    VERSION: str
    """The version of the OpenAPI documentation."""


@dataclass
class Settings:
    """Convenience class to group all settings together."""

    app: ApplicationSettings = field(default_factory=ApplicationSettings)
    database: DatabaseSettings = field(default_factory=DatabaseSettings)
    openapi: OpenAPISettings = field(default_factory=OpenAPISettings)


settings = Settings()

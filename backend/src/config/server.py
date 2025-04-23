from advanced_alchemy.extensions.litestar import (
    AsyncSessionConfig,
    EngineConfig,
    SQLAlchemyAsyncConfig,
    async_autocommit_before_send_handler,
)

from .general import settings

from litestar.config.cors import CORSConfig
from litestar.logging.config import LoggingConfig, StructLoggingConfig, default_structlog_standard_lib_processors
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin
from litestar.plugins.structlog import StructlogConfig
import structlog



cors_config = CORSConfig(allow_origins=["*"], allow_credentials=True)

logging_config = StructlogConfig(
    structlog_logging_config=StructLoggingConfig(
        log_exceptions="always",
        standard_lib_logging_config=LoggingConfig(
            root={"level": settings.app.LOG_LEVEL, "handlers": ["queue_listener"]},
            formatters={
                "standard": {
                    "()": structlog.stdlib.ProcessorFormatter,
                    "processors": default_structlog_standard_lib_processors(settings.app.ENVIRONMENT != "local"),
                },
            },
            loggers={
                "uvicorn.access": {
                    "propagate": False,
                    "level": settings.app.LOG_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "uvicorn.error": {
                    "propagate": False,
                    "level": settings.app.LOG_LEVEL,
                    "handlers": ["queue_listener"],
                },
                "sqlalchemy.pool": {
                    "propagate": False,
                    "level": settings.app.LOG_LEVEL,
                    "handlers": ["queue_listener"],
                },
            },
        ),
    ),
)

db_config = SQLAlchemyAsyncConfig(
    connection_string=settings.database.URL,
    before_send_handler=async_autocommit_before_send_handler,
    enable_touch_updated_timestamp_listener=False,
    engine_config=EngineConfig(echo=False),
    session_config=AsyncSessionConfig(expire_on_commit=False),
    session_dependency_key="session",
)

openapi_config = OpenAPIConfig(
    title=settings.openapi.TITLE,
    version=settings.openapi.VERSION,
    use_handler_docstrings=True,
    render_plugins=[ScalarRenderPlugin()],
)

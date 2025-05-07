from src.domain.users.config import litestar_users_config
from litestar_users import LitestarUsersPlugin
from litestar.plugins.structlog import StructlogPlugin
from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from src.config.server import db_config, logging_config
from litestar.channels import ChannelsPlugin
from litestar.channels.backends.memory import MemoryChannelsBackend

litestar_users = LitestarUsersPlugin(litestar_users_config)
structlog_plugin = StructlogPlugin(logging_config)
sqlalchemy_plugin = SQLAlchemyPlugin(db_config)
channels_plugin = ChannelsPlugin(backend=MemoryChannelsBackend(history=5), arbitrary_channels_allowed=True)

plugins = [litestar_users, structlog_plugin, sqlalchemy_plugin, channels_plugin]

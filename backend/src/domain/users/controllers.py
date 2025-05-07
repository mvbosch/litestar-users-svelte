from contextlib import asynccontextmanager
from typing import AsyncGenerator

from litestar import WebSocket, websocket_listener
from litestar.channels import ChannelsPlugin
from litestar.exceptions import WebSocketDisconnect


@asynccontextmanager
async def socket_lifespan(socket: WebSocket, channels: ChannelsPlugin) -> AsyncGenerator[None, None]:
    async with channels.start_subscription(socket.path_params["session_id"], history=5) as subscription:
        try:
            async with subscription.run_in_background(socket.send_data):
                yield
        except WebSocketDisconnect:
            return


@websocket_listener("/token/{session_id:str}", exclude_from_auth=True, connection_lifespan=socket_lifespan)
async def token_notifier(data: str, socket: WebSocket, session_id: str) -> None:
    """
    WebSocket endpoint to notify the client of the verification token.
    """
    if socket.session.get("session_id") != session_id:
        await socket.close(code=4000, reason="Session ID mismatch")
        return
    # don't call us, we'll call you
    return

FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Install the project into `/app`
WORKDIR /app/backend

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1 \
# Copy from the cache instead of linking since it's a mounted volume
    UV_LINK_MODE=copy

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    git \
    ssh-client \
    && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID --shell /bin/bash -m $USERNAME \
    && mkdir -p /home/$USERNAME/.local/bin /home/$USERNAME/.local/share/uv /home/$USERNAME/.cache/pre-commit \
    && chown -R $USERNAME:$USERNAME /home/$USERNAME/.local \
    && chown -R $USERNAME:$USERNAME /home/$USERNAME/.cache

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen \
    && chown -R $USERNAME:$USERNAME /app/backend/.venv

# Place executables in the environment at the front of the path
ENV PATH="/app/backend/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

CMD "while sleep 500; do :; done"

FROM node:22-bookworm-slim
WORKDIR /app/frontend

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    git \
    ssh-client \
    && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* \
    && chown -R node:node /app

USER node

COPY --chown=node:node package*.json ./

RUN npm install

FROM python:3.11-slim

USER root
RUN apt-get update --allow-unauthenticated && apt-get install -y --no-install-recommends \
curl \
&& rm -rf /var/lib/apt/lists/*

ARG UID=1000
ARG GID=1000
RUN groupadd -g "${GID}" python && \
    useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

WORKDIR /app
COPY --chown=python:python pyproject.toml uv.lock ./
RUN uv sync --locked

USER python
COPY --chown=python:python . .
ENTRYPOINT ["uv", "run", "uvicorn", "test_task2.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
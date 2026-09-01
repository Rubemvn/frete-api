FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:0.9 /uv /usr/local/bin/uv

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH" \
    UV_PROJECT_ENVIRONMENT="/app/.venv" \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy
ARG HOST_UID=1000
RUN useradd --create-home --uid ${HOST_UID} app

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project
COPY --chown=app:app src/ ./src/
RUN uv sync --frozen

USER app
EXPOSE 8000

WORKDIR /app/src
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
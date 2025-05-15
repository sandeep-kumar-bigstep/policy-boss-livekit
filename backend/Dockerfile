# Dockerfile for PolicyBoss LiveKit Agent
# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.11.6
FROM python:${PYTHON_VERSION}-slim

# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering
ENV PYTHONUNBUFFERED=1

# Create a non-privileged user that the app will run under
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/appuser" \
    --shell "/sbin/nologin" \
    --uid "${UID}" \
    appuser

# Install gcc, g++ and other build dependencies
RUN apt-get update && \
    apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

USER appuser

# Set up cache directory for the user
RUN mkdir -p /home/appuser/.cache
RUN chown -R appuser /home/appuser/.cache

WORKDIR /app

# Copy requirements first for better caching
COPY --chown=appuser:appuser requirements.txt .
RUN python -m pip install --user --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY --chown=appuser:appuser . .

# Download model files and dependencies at build time
RUN python agent.py download-files

# Expose healthcheck port
EXPOSE 8081

# Run the application
# Using agent.py as the entry point based on the project structure
CMD ["python", "agent.py", "start"]

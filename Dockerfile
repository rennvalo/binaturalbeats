# Lean production Dockerfile for Reflex
FROM python:3.12-slim

# Install system dependencies including curl and Node.js
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    unzip \
    build-essential \
    && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Bun for fast package execution
RUN curl -fsSL https://bun.sh/install | bash
ENV BUN_INSTALL="/root/.bun"
ENV PATH="${BUN_INSTALL}/bin:${PATH}"

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create persistent runtime directories and Reflex's static asset directory.
RUN mkdir -p /data /media /app/assets

# Copy application source and media served by the FastAPI static mount.
COPY rxconfig.py .
COPY binaturalbeats/ ./binaturalbeats/
COPY media/ /media/

# Expose mounted media through Reflex's frontend static asset server.
RUN ln -sfn /media /app/assets/media

# Initialize reflex and build frontend
RUN reflex init
RUN reflex export --frontend-only && rm -f frontend.zip backend.zip

EXPOSE 3000 8000

ENV PORT=3000
ENV API_URL=http://localhost:8000
ENV DATABASE_URL=sqlite:////data/app.db

CMD ["reflex", "run", "--env", "prod"]

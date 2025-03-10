FROM ubuntu:22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV QT_QPA_PLATFORM=xcb

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    libxcb-xinerama0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-xkb1 \
    libxkbcommon-x11-0 \
    libfontconfig1 \
    libdbus-1-3 \
    libnspr4 \
    libnss3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install PyQt6
RUN pip3 install --no-cache-dir PyQt6 PyQt6-WebEngine

# Create app directory
WORKDIR /app

# Copy all Python files and resources
COPY *.py /app/
COPY *.png /app/

# Create a simple wrapper script for environment setup
RUN echo '#!/bin/bash\n\
export DISPLAY=${DISPLAY:-:0}\n\
export QT_QPA_PLATFORM=xcb\n\
exec python3 /app/main.py "$@"\n\
' > /app/entrypoint.sh && chmod +x /app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

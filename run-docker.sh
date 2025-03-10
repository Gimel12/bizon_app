#!/bin/bash

# Script to build and run the Bizon Guide App in a Docker container
set -e

# Define colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Function to print colored messages
info() { echo -e "${GREEN}[INFO]${NC} $1"; }
warn() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Function to check dependencies
check_dependency() {
    if ! command -v "$1" &> /dev/null; then
        error "$1 is not installed. Please install it first."
        exit 1
    fi
}

# Check if Docker is installed
check_dependency "docker"

# Check if Docker Compose is installed
check_dependency "docker-compose"

# Create cache directory if it doesn't exist
CACHE_DIR="${HOME}/.bizon_app_cache"
if [ ! -d "$CACHE_DIR" ]; then
    info "Creating cache directory at $CACHE_DIR"
    mkdir -p "$CACHE_DIR"
fi

# Check if X server is running
if [ -z "$DISPLAY" ]; then
    warn "DISPLAY environment variable not set. GUI may not work properly."
fi

# Allow X server connections for GUI display
info "Configuring X server permissions..."
xhost +local:docker

# Function to handle cleanup on exit
cleanup() {
    info "Cleaning up..."
    xhost -local:docker
}

# Register the cleanup function to be called on exit
trap cleanup EXIT

# Build and run the Docker container
info "Building and starting the Bizon Guide App..."
docker-compose build
docker-compose up -d

if [ $? -eq 0 ]; then
    info "Bizon Guide App is now running!"
    info "To stop the app, run: ./run-docker.sh stop"
    info "To view logs, run: ./run-docker.sh logs"
else
    error "Failed to start Bizon Guide App. Check the logs for details."
    exit 1
fi

# Command handling
case "$1" in
    stop)
        info "Stopping Bizon Guide App..."
        docker-compose down
        ;;
    logs)
        info "Showing logs for Bizon Guide App..."
        docker-compose logs -f
        ;;
    restart)
        info "Restarting Bizon Guide App..."
        docker-compose restart
        ;;
esac

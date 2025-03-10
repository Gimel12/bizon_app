# Bizon Guide App

The Bizon Guide App provides easy access to guides, scripts, and support resources for Bizon products.

## Features

- Access to Bizon documentation and guides
- Scripts library for common tasks
- AI catalog integration
- Support portal access
- Automatic updates from GitHub

## Installation

### Using Docker (Recommended)

The easiest way to run the Bizon Guide App is using Docker:

1. Make sure Docker and Docker Compose are installed on your system:
   ```bash
   # For Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install docker.io docker-compose
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/Gimel12/bizon_app.git
   cd bizon_app
   ```

3. Allow X server connections (for GUI display):
   ```bash
   xhost +local:docker
   ```

4. Build and run the Docker container:
   ```bash
   docker-compose up -d
   ```

5. To stop the application:
   ```bash
   docker-compose down
   ```

### From Snap Store

Alternatively, you can install the app from the Snap Store once published:

```bash
sudo snap install bizon-guide
```

### Manual Snap Installation

To build and install the Snap package manually:

1. Install Snapcraft:
   ```bash
   sudo snap install snapcraft --classic
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/Gimel12/bizon_app.git
   cd bizon_app
   ```

3. Build the Snap package:
   ```bash
   snapcraft
   ```

4. Install the built package:
   ```bash
   sudo snap install bizon-guide_1.0.1_amd64.snap --dangerous
   ```

## Usage

After installation, you can launch the app from your application menu or by running:

```bash
bizon-guide
```

## Updating

The app includes an update button that allows you to pull the latest code from GitHub.

## Development

### Requirements

- Python 3.6+
- PyQt6
- Git

### Building from Source

To run the app directly from source:

```bash
python3 main.py
```

## License

Copyright © 2025 Bizon Technologies

# Bizon Guide App

The Bizon Guide App provides easy access to guides, scripts, and support resources for Bizon products.

## Features

- Access to Bizon documentation and guides
- Scripts library for common tasks
- AI catalog integration
- Support portal access
- Automatic updates from GitHub

## Installation

### From Snap Store (Recommended)

Once published, you can install the app directly from the Snap Store:

```bash
sudo snap install bizon-guide
```

### Manual Installation

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

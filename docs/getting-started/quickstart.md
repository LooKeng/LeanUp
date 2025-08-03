# Quick Start

## Installation

```bash
# Install from source
pip install -e /path/to/LeanUp

# Or clone the repository and install
git clone https://github.com/Lean-zh/LeanUp.git
cd LeanUp
pip install -e .
```

## Basic Usage

### Initialize Configuration

```bash
# Initialize LeanUp configuration
leanup init

# View current status
leanup status
```

### Install elan

```bash
# Install latest version of elan
leanup install

# Install specific version
leanup install v1.4.2

# Force reinstall
leanup install --force
```

### Manage Toolchains

```bash
# Proxy execute elan commands
leanup elan --help
leanup elan toolchain list
leanup elan toolchain install stable
leanup elan default stable
```

### Repository Management

```bash
# Install a repository
leanup repo install mathlib4

# Install with interactive configuration
leanup repo install mathlib4 --interactive

# Install from specific source
leanup repo install mathlib4 --source github

# Install from URL
leanup repo install --url https://github.com/leanprover-community/mathlib4.git

# List installed repositories
leanup repo list
```

## Using the RepoManager

The `RepoManager` class provides functionality for managing directories and git repositories:

```python
from leanup.repo import RepoManager

# Initialize a directory manager
repo = RepoManager("/path/to/your/directory")

# Check if it's a git repository
if repo.is_gitrepo:
    print("This is a git repository")
    status = repo.git_status()
    print(f"Current branch: {status['branch']}")
else:
    print("This is not a git repository")
    # Clone from remote
    repo.clone_from("https://github.com/username/repo.git")

# Read a file
content = repo.read_file("README.md")
print(content)

# Write to a file
repo.write_file("example.txt", "Hello, World!")

# Edit a file
repo.edit_file("example.txt", "Hello", "Hi")

# Execute a command
stdout, stderr, returncode = repo.execute_command("ls -la")
print(stdout)
```

## Configuration

LeanUp uses a configuration file at `~/.leanup/config.toml`. The configuration includes:

- Repository settings (default source, cache directory)
- elan settings (auto-installation)
- Interactive installation preferences

You can modify the configuration manually or use the interactive installation mode to set preferences.
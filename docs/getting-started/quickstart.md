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

```bash
# View help
leanup --help

# Install elan (Lean toolchain manager)
leanup install

# View status
leanup status

# Proxy execute elan commands
leanup elan --help
leanup elan toolchain list
leanup elan toolchain install stable
leanup elan default stable
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
# LeanUp

A Python package for managing Lean mathematical proof language environments.

## Features

- **🔧 elan Management**: Install and manage the Lean toolchain manager elan with a single command
- **📦 Repository Management**: Install and manage Lean repositories with interactive configuration
- **🌍 Cross-platform Support**: Works on Linux, macOS, and Windows
- **📦 Easy Installation**: Quick setup via `pip install -e /path/to/LeanUp`
- **🔄 Command Proxy**: Transparent proxy for all elan commands with streaming output support
- **📊 Status Monitoring**: Real-time view of Lean environment status and installed toolchains
- **⚙️ Configuration Management**: Flexible configuration system with interactive setup

## Quick Start

Check the [Quick Start](getting-started/quickstart.md) guide to begin using LeanUp.

## Command Line Interface

LeanUp provides a comprehensive CLI with the following commands:

### Main Commands

- `leanup init` - Initialize LeanUp configuration
- `leanup install [version]` - Install Lean toolchain version via elan
- `leanup status` - Show current status and configuration
- `leanup elan <args>` - Proxy elan commands

### Repository Management

- `leanup repo install <repository>` - Install Lean repositories
- `leanup repo list` - List installed repositories

## Modules

### CLI Module

The `leanup.cli` module provides the command-line interface:

- **Main CLI**: Core commands for elan management and status monitoring
- **Repository CLI**: Commands for managing Lean repositories
- **Configuration**: Centralized configuration management

### Utils Module

The `leanup.utils` module provides utility functions for the package:

- `execute_command`: Execute shell commands with proper error handling and cross-platform support
- `setup_logger`: Configure a logger with customizable output formats and color support

### Repo Module

The `leanup.repo` module provides functionality for repository management:

- `RepoManager`: A class for managing directory operations and git functionality
  - File operations (read, write, edit)
  - Command execution
  - Git operations (clone, status, add, commit, pull, push)

- `ElanManager`: A class for managing the Lean toolchain manager elan
  - Automatic elan installation and version management
  - Cross-platform installer download and execution
  - Command proxy with streaming output support
  - Toolchain management and status monitoring

## Architecture

LeanUp is built with a modular architecture:

- **CLI layer**: Command-line interface for user interactions
- **Utils layer**: Core utility functions for command execution and logging
- **Repo layer**: High-level abstractions for repository and toolchain management

The package uses the `execute_command` utility function from the utils module for all command execution, ensuring consistent behavior across different platforms and components.
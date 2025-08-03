# LeanUp

A Python package for managing Lean mathematical proof language environments.

## Features

- **🔧 elan management**: Install and manage the Lean toolchain manager elan with a single command
- **🌍 Cross-platform support**: Works on Linux, macOS, and Windows
- **📦 Easy to use**: Quick installation via `pip install -e /path/to/LeanUp`
- **🔄 Command proxy**: Transparent proxy for all elan commands with streaming output support
- **📊 Status monitoring**: Real-time view of Lean environment status and installed toolchains

## Quick Start

Check the [Quick Start](getting-started/quickstart.md) guide to begin using LeanUp.

## Modules

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

- **Utils layer**: Core utility functions for command execution and logging
- **Repo layer**: High-level abstractions for repository and toolchain management
- **CLI layer**: Command-line interface for user interactions

The package uses the `execute_command` utility function from the utils module for all command execution, ensuring consistent behavior across different platforms and components.
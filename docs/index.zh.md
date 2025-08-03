# LeanUp

一个用于管理 Lean 数学证明语言环境的 Python 工具。

## 功能特性

- **🔧 elan 管理**: 一键安装和管理 Lean 工具链管理器 elan
- **🌍 跨平台支持**: 支持 Linux、macOS 和 Windows
- **📦 简单易用**: 通过 `pip install -e /path/to/LeanUp` 快速安装
- **🔄 命令代理**: 透明代理所有 elan 命令，无缝体验
- **📊 状态监控**: 实时查看 Lean 环境状态和已安装工具链

## 快速开始

查看[快速开始](getting-started/quickstart.md)指南，开始使用 LeanUp。

## 模块

### Utils 模块

`leanup.utils` 模块提供了包的实用函数：

- `execute_command`: 执行 shell 命令，具有适当的错误处理
- `setup_logger`: 配置日志记录器，支持自定义输出格式和颜色

### Repo 模块

`leanup.repo` 模块提供了仓库管理功能：

- `RepoManager`: 用于管理目录操作和 git 功能的类
  - 文件操作（读取、写入、编辑）
  - 命令执行
  - Git 操作（克隆、状态、添加、提交、拉取、推送）
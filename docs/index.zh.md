# LeanUp

一个用于管理 Lean 数学证明语言环境的 Python 工具。

## 功能特性

- **🔧 elan 管理**: 一键安装和管理 Lean 工具链管理器 elan
- **📦 仓库管理**: 通过交互式配置安装和管理 Lean 仓库
- **🌍 跨平台支持**: 支持 Linux、macOS 和 Windows
- **📦 简单易用**: 通过 `pip install -e /path/to/LeanUp` 快速安装
- **🔄 命令代理**: 透明代理所有 elan 命令，支持流式输出
- **📊 状态监控**: 实时查看 Lean 环境状态和已安装工具链
- **⚙️ 配置管理**: 灵活的配置系统，支持交互式设置

## 快速开始

查看[快速开始](getting-started/quickstart.zh.md)指南，开始使用 LeanUp。

## 命令行界面

LeanUp 提供了完整的 CLI，包含以下命令：

### 主要命令

- `leanup init` - 初始化 LeanUp 配置
- `leanup install [version]` - 安装 Lean 工具链版本（通过 elan）
- `leanup status` - 显示当前状态和配置
- `leanup elan <args>` - 代理 elan 命令

### 仓库管理

- `leanup repo install <repository>` - 安装 Lean 仓库
- `leanup repo list` - 列出已安装的仓库

## 模块

### CLI 模块

`leanup.cli` 模块提供了命令行界面：

- **主 CLI**: elan 管理和状态监控的核心命令
- **仓库 CLI**: 管理 Lean 仓库的命令
- **配置**: 集中化配置管理

### Utils 模块

`leanup.utils` 模块提供了包的实用函数：

- `execute_command`: 执行 shell 命令，具有适当的错误处理和跨平台支持
- `setup_logger`: 配置日志记录器，支持自定义输出格式和颜色

### Repo 模块

`leanup.repo` 模块提供了仓库管理功能：

- `RepoManager`: 用于管理目录操作和 git 功能的类
  - 文件操作（读取、写入、编辑）
  - 命令执行
  - Git 操作（克隆、状态、添加、提交、拉取、推送）
- `LeanRepo`: 专门用于 Lean 项目的仓库管理器，扩展了 RepoManager 并支持 lake 功能
- `ElanManager`: 管理 Lean 工具链管理器 elan 的类
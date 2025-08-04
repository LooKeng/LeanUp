# 快速开始

## 安装

```bash
# 从源码安装
pip install -e /path/to/LeanUp

# 或者克隆仓库后安装
git clone https://github.com/Lean-zh/LeanUp.git
cd LeanUp
pip install -e .
```

## 基础使用

### 初始化配置

```bash
# 查看帮助
leanup --help

# 安装 elan 并初始化配置
leanup init

# 安装最新稳定版本
leanup install

# 查看当前状态
leanup status
```

### 安装 Lean 工具链

```bash
# 安装最新稳定版 Lean 工具链
leanup install

# 安装特定版本的 Lean 工具链
leanup install v4.14.0

# 强制重新安装
leanup install --force
```

### 管理工具链

```bash
# 代理执行 elan 命令
leanup elan --help
leanup elan toolchain list
leanup elan toolchain install stable
leanup elan default stable
```

### 仓库管理

```bash
# 安装仓库
leanup repo install mathlib4

# 使用交互式配置安装
leanup repo install mathlib4 --interactive

# 从特定源安装
leanup repo install mathlib4 --source github

# 从 URL 安装
leanup repo install --url https://github.com/leanprover-community/mathlib4.git

# 列出已安装的仓库
leanup repo list
```

## 使用 RepoManager

`RepoManager` 类提供了管理目录和 git 仓库的功能：

```python
from leanup.repo import RepoManager

# 初始化一个目录管理器
repo = RepoManager("/path/to/your/directory")

# 检查是否为git仓库
if repo.is_gitrepo:
    print("这是一个git仓库")
    status = repo.git_status()
    print(f"当前分支: {status['branch']}")
else:
    print("这不是一个git仓库")

# 克隆仓库
repo.clone_from("https://github.com/user/repo.git")

# 读取文件
content = repo.read_file("README.md")

# 写入文件
repo.write_file("test.txt", "Hello World")

# 执行命令
result = repo.execute_command(["ls", "-la"])
```

## 使用 LeanRepo

`LeanRepo` 类专门用于 Lean 项目管理：

```python
from leanup.repo import LeanRepo

# 初始化 Lean 项目管理器
lean_repo = LeanRepo("/path/to/lean/project")

# 获取 Lean 工具链版本
toolchain = lean_repo.get_lean_toolchain()
print(f"Lean 工具链: {toolchain}")

# 执行 lake 命令
lean_repo.lake_update()
lean_repo.lake_build()

# 执行自定义 lake 命令
result = lean_repo.lake(["build", "MyPackage"])
```
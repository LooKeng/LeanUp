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

```bash
# 查看帮助
leanup --help

# 安装 elan（Lean 工具链管理器）
leanup install

# 查看状态
leanup status

# 代理执行 elan 命令
leanup elan --help
leanup elan toolchain list
leanup elan toolchain install stable
leanup elan default stable
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
    # 从远程克隆
    repo.clone_from("https://github.com/username/repo.git")

# 读取文件
content = repo.read_file("README.md")
print(content)

# 写入文件
repo.write_file("example.txt", "Hello, World!")

# 编辑文件
repo.edit_file("example.txt", "Hello", "Hi")

# 执行命令
stdout, stderr, returncode = repo.execute_command("ls -la")
print(stdout)
```
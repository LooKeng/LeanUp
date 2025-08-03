# API 参考文档

## leanup.utils.basic

### execute_command

```python
def execute_command(
    command: list,
    cwd: Optional[str] = None,
    text: bool = True,
    input: Union[str, None] = None,
    capture_output: bool = True,
    timeout: Optional[int] = None
) -> Tuple[str, str, int]
```

使用 subprocess.Popen 执行命令。

**参数：**
- `command`: 命令参数列表
- `cwd`: 工作目录路径
- `text`: 是否以文本形式返回输出
- `input`: 传递给命令的输入字符串
- `capture_output`: 是否捕获 stdout/stderr
- `timeout`: 最大执行时间（秒）

**返回值：**
包含 stdout、stderr 和返回码的元组

## leanup.repo.elan

### ElanManager

用于管理 Lean 工具链管理器 elan 的类。

#### 方法

##### `__init__()`
使用 elan 主目录初始化 ElanManager。

##### `get_elan_executable() -> Optional[Path]`
获取 elan 可执行文件路径。

##### `is_elan_installed() -> bool`
检查 elan 是否已安装。

##### `get_elan_version() -> Optional[str]`
获取已安装的 elan 版本。

##### `install_elan(version: Optional[str] = None, force: bool = False) -> bool`
安装 elan，可选择指定版本。

##### `proxy_elan_command(args: List[str]) -> int`
代理执行 elan 命令，支持流式输出。

##### `get_installed_toolchains() -> List[str]`
获取已安装工具链列表。

##### `get_status_info() -> Dict[str, any]`
获取 elan 的综合状态信息。

## leanup.repo.manager

### RepoManager

用于管理目录操作和 git 功能的基类。

### LeanRepo

专门用于 Lean 项目的仓库管理器，扩展了 RepoManager 并支持 lake 功能。

#### 方法

##### `__init__(cwd: Union[str, Path])`
使用工作目录初始化 LeanRepo。

##### `get_lean_toolchain() -> Optional[str]`
读取 lean-toolchain 文件获取 Lean 版本。

**返回值：**
如果找到则返回 Lean 版本字符串，否则返回 None

##### `parse_dependencies() -> Dict[str, Any]`
从 lakefile.toml 或 lakefile.lean 解析依赖。

**返回值：**
包含解析依赖的字典

##### `lake(args: List[str]) -> Tuple[str, str, int]`
使用给定参数执行 lake 命令。

**参数：**
- `args`: lake 命令参数列表

**返回值：**
包含 stdout、stderr 和返回码的元组

##### `lake_build(target: Optional[str] = None) -> Tuple[str, str, int]`
使用 lake 构建 Lean 项目。

**参数：**
- `target`: 可选的构建目标

##### `lake_update() -> Tuple[str, str, int]`
使用 lake 更新依赖。

##### `lake_env_lean(filepath: Union[str, Path], js: bool = True) -> Tuple[str, str, int]`
在 lake 环境中运行 lean 文件。

**参数：**
- `filepath`: Lean 文件路径
- `js`: 是否使用 JavaScript 后端（默认：True）

##### `lake_clean() -> Tuple[str, str, int]`
使用 lake 清理构建产物。

##### `lake_test() -> Tuple[str, str, int]`
使用 lake 运行测试。

##### `get_project_info() -> Dict[str, Any]`
获取项目的综合信息，包括 Lean 版本、依赖和文件状态。
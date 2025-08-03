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
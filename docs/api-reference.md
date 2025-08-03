# API Reference

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

Execute command with subprocess.Popen.

**Parameters:**
- `command`: List of command arguments
- `cwd`: Working directory path
- `text`: Whether to return output as text
- `input`: Input string to pass to command
- `capture_output`: Whether to capture stdout/stderr
- `timeout`: Maximum execution time in seconds

**Returns:**
Tuple containing stdout, stderr, and return code

## leanup.repo.elan

### ElanManager

A class for managing the Lean toolchain manager elan.

#### Methods

##### `__init__()`
Initialize ElanManager with elan home directory.

##### `get_elan_executable() -> Optional[Path]`
Get elan executable file path.

##### `is_elan_installed() -> bool`
Check if elan is installed.

##### `get_elan_version() -> Optional[str]`
Get installed elan version.

##### `install_elan(version: Optional[str] = None, force: bool = False) -> bool`
Install elan with optional version specification.

##### `proxy_elan_command(args: List[str]) -> int`
Proxy execute elan command with streaming output support.

##### `get_installed_toolchains() -> List[str]`
Get list of installed toolchains.

##### `get_status_info() -> Dict[str, any]`
Get comprehensive elan status information.
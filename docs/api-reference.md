# API Reference

## leanup.cli.config

### ConfigManager

A class for managing LeanUp configuration.

#### Methods

##### `__init__(config_dir: Optional[Path] = None)`
Initialize ConfigManager with optional config directory.

##### `config_exists() -> bool`
Check if configuration file exists.

##### `init_config() -> bool`
Initialize configuration file with default values.

##### `load_config() -> Dict[str, Any]`
Load configuration from file.

##### `save_config(config: Dict[str, Any]) -> bool`
Save configuration to file.

##### `get_cache_dir() -> Path`
Get cache directory path.

##### `get_default_source() -> str`
Get default repository source URL.

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

## leanup.repo.manager

### RepoManager

Base class for managing directory operations and git functionality.

### LeanRepo

A specialized repository manager for Lean projects, extending RepoManager with lake support.

#### Methods

##### `__init__(cwd: Union[str, Path])`
Initialize LeanRepo with working directory.

##### `get_lean_toolchain() -> Optional[str]`
Read lean-toolchain file to get Lean version.

**Returns:**
Lean version string if found, None otherwise

##### `parse_dependencies() -> Dict[str, Any]`
Parse dependencies from lakefile.toml or lakefile.lean.

**Returns:**
Dictionary containing parsed dependencies

##### `lake(args: List[str]) -> Tuple[str, str, int]`
Execute lake command with given arguments.

**Parameters:**
- `args`: List of lake command arguments

**Returns:**
Tuple containing stdout, stderr, and return code

##### `lake_build(target: Optional[str] = None) -> Tuple[str, str, int]`
Build the Lean project using lake.

**Parameters:**
- `target`: Optional build target

##### `lake_update() -> Tuple[str, str, int]`
Update dependencies using lake.

##### `lake_env_lean(filepath: Union[str, Path], js: bool = True) -> Tuple[str, str, int]`
Run lean file with lake environment.

**Parameters:**
- `filepath`: Path to the Lean file
- `js`: Whether to use JavaScript backend (default: True)

##### `lake_clean() -> Tuple[str, str, int]`
Clean build artifacts using lake.

##### `lake_test() -> Tuple[str, str, int]`
Run tests using lake.

##### `get_project_info() -> Dict[str, Any]`
Get comprehensive project information including Lean version, dependencies, and file status.
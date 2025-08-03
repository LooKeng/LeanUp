import subprocess
from typing import Optional, Union, Tuple

def execute_command(command: list,
        cwd: Optional[str] = None,
        text: bool = True,
        input: Union[str, None] = None,
        capture_output: bool = True,
        timeout: Optional[int] = None) -> Tuple[str, str, int]:
    """
    Execute command with subprocess.Popen.

    Args:
        command: List of command arguments
        cwd: Working directory path
        text: Whether to return output as text
        input: Input string to pass to command
        capture_output: Whether to capture stdout/stderr
        timeout: Maximum execution time in seconds

    Returns:
        Tuple containing stdout, stderr, and return code
    """
    process = None
    try:
        stdout_pipe = subprocess.PIPE if capture_output else None
        stderr_pipe = subprocess.PIPE if capture_output else None
        process = subprocess.Popen(
            command,
            cwd=cwd,
            stdout=stdout_pipe,
            stderr=stderr_pipe,
            text=text
        )
        stdout, stderr = process.communicate(input=input, timeout=timeout)
        returncode = process.returncode
        stdout = stdout or ""
        stderr = stderr or ""
    except Exception as e:
        stdout, stderr, returncode = "", str(e), -1
    return stdout, stderr, returncode

import subprocess
from pathlib import Path
from typing import Optional, Union, List, Dict, Any, Tuple
import git
import platform

from leanup.utils.basic import execute_command
from leanup.utils.custom_logger import setup_logger

logger = setup_logger("repo_manager")

class RepoManager:
    """Class for managing directory operations and git functionality."""
    
    def __init__(self, cwd: Union[str, Path]):
        """Initialize with a working directory.
        
        Args:
            cwd: Working directory path
        """
        self.cwd = Path(cwd).absolute()
        self._git_repo = None
        self._check_git_repo()
    
    def _check_git_repo(self) -> None:
        """Check if the current directory is a git repository and initialize git.Repo if it is."""
        try:
            if (self.cwd / ".git").exists():
                self._git_repo = git.Repo(self.cwd)
                logger.debug(f"Git repository found at {self.cwd}")
            else:
                logger.debug(f"{self.cwd} is not a git repository")
        except Exception as e:
            logger.error(f"Error checking git repository: {e}")
    
    @property
    def is_gitrepo(self) -> bool:
        """Check if the current directory is a git repository.
        
        Returns:
            bool: True if the directory is a git repository, False otherwise
        """
        return self._git_repo is not None
    
    def clone_from(self, url: str, branch: Optional[str] = None, depth: Optional[int] = None) -> bool:
        """Clone a git repository to the current directory.
        
        Args:
            url: Git repository URL
            branch: Branch to clone (optional)
            depth: Depth for shallow clone (optional)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Prepare command
            cmd = ["git", "clone", url, "."]
            if branch:
                cmd.extend(["--branch", branch])
            if depth:
                cmd.extend(["--depth", str(depth)])
                
            # Execute clone command
            stdout, stderr, returncode = execute_command(cmd, cwd=str(self.cwd))
            
            if returncode == 0:
                logger.info(f"Successfully cloned {url} to {self.cwd}")
                self._check_git_repo()  # Refresh git repo status
                return True
            else:
                logger.error(f"Failed to clone repository: {stderr}")
                return False
        except Exception as e:
            logger.error(f"Error cloning repository: {e}")
            return False
    
    def execute_command(self, command: Union[str, List[str]]) -> Tuple[str, str, int]:
        """Execute a command in the current directory.
        
        Args:
            command: Command to execute (string or list of arguments)
            
        Returns:
            Tuple containing stdout, stderr, and return code
        """
        if isinstance(command, str):
            # Split the command string into a list
            if platform.system() == 'Windows':
                # For Windows, use shell=True for string commands
                process = subprocess.Popen(
                    command,
                    cwd=str(self.cwd),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True,
                    text=True
                )
                stdout, stderr = process.communicate()
                return stdout, stderr, process.returncode
            else:
                # For Unix-like systems, split the command
                import shlex
                command = shlex.split(command)
        
        return execute_command(command, cwd=str(self.cwd))
    
    def read_file(self, file_path: Union[str, Path]) -> str:
        """Read the contents of a file.
        
        Args:
            file_path: Path to the file (relative to cwd)
            
        Returns:
            str: File contents
        
        Raises:
            FileNotFoundError: If the file doesn't exist
        """
        path = self.cwd / file_path
        return path.read_text(encoding='utf-8')
    
    def write_file(self, file_path: Union[str, Path], content: str, append: bool = False) -> bool:
        """Write content to a file.
        
        Args:
            file_path: Path to the file (relative to cwd)
            content: Content to write
            append: Whether to append to the file (default: False)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            path = self.cwd / file_path
            # Create parent directories if they don't exist
            path.parent.mkdir(parents=True, exist_ok=True)
            
            mode = 'a' if append else 'w'
            with open(path, mode, encoding='utf-8') as f:
                f.write(content)
            return True
        except Exception as e:
            logger.error(f"Error writing to file {file_path}: {e}")
            return False
    
    def edit_file(self, file_path: Union[str, Path], 
                  find_text: str, replace_text: str, 
                  use_regex: bool = False) -> bool:
        """Edit a file by replacing text.
        
        Args:
            file_path: Path to the file (relative to cwd)
            find_text: Text to find
            replace_text: Text to replace with
            use_regex: Whether to use regex for find/replace
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            path = self.cwd / file_path
            if not path.exists():
                logger.error(f"File {file_path} does not exist")
                return False
                
            content = path.read_text(encoding='utf-8')
            
            if use_regex:
                import re
                new_content = re.sub(find_text, replace_text, content)
            else:
                new_content = content.replace(find_text, replace_text)
                
            path.write_text(new_content, encoding='utf-8')
            return True
        except Exception as e:
            logger.error(f"Error editing file {file_path}: {e}")
            return False
    
    def list_files(self, pattern: Optional[str] = None) -> List[Path]:
        """List files in the current directory, optionally filtered by pattern.
        
        Args:
            pattern: Glob pattern to filter files
            
        Returns:
            List of Path objects
        """
        if pattern:
            return list(self.cwd.glob(pattern))
        else:
            return [p for p in self.cwd.iterdir() if p.is_file()]
    
    def list_dirs(self, pattern: Optional[str] = None) -> List[Path]:
        """List subdirectories in the current directory, optionally filtered by pattern.
        
        Args:
            pattern: Glob pattern to filter directories
            
        Returns:
            List of Path objects
        """
        if pattern:
            return [p for p in self.cwd.glob(pattern) if p.is_dir()]
        else:
            return [p for p in self.cwd.iterdir() if p.is_dir()]
    
    # Git operations
    def git_status(self) -> Dict[str, Any]:
        """Get git status information.
        
        Returns:
            Dict containing status information or error message
        """
        if not self.is_gitrepo:
            return {"error": "Not a git repository"}
        
        try:
            return {
                "branch": self._git_repo.active_branch.name,
                "is_dirty": self._git_repo.is_dirty(),
                "untracked_files": self._git_repo.untracked_files,
                "modified_files": [item.a_path for item in self._git_repo.index.diff(None)]
            }
        except Exception as e:
            return {"error": str(e)}
    
    def git_add(self, paths: Union[str, List[str], None] = None) -> bool:
        """Add files to git staging area.
        
        Args:
            paths: File path(s) to add, or None to add all
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.is_gitrepo:
            logger.error("Not a git repository")
            return False
        
        try:
            if paths is None:
                # Add all files
                self._git_repo.git.add(A=True)
            elif isinstance(paths, str):
                # Add single file
                self._git_repo.git.add(paths)
            else:
                # Add multiple files
                for path in paths:
                    self._git_repo.git.add(path)
            return True
        except Exception as e:
            logger.error(f"Error adding files to git: {e}")
            return False
    
    def git_commit(self, message: str) -> bool:
        """Commit changes to git repository.
        
        Args:
            message: Commit message
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.is_gitrepo:
            logger.error("Not a git repository")
            return False
        
        try:
            self._git_repo.git.commit(m=message)
            return True
        except Exception as e:
            logger.error(f"Error committing changes: {e}")
            return False
    
    def git_pull(self, remote: str = "origin", branch: Optional[str] = None) -> bool:
        """Pull changes from remote repository.
        
        Args:
            remote: Remote name
            branch: Branch name (optional)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.is_gitrepo:
            logger.error("Not a git repository")
            return False
        
        try:
            if branch:
                self._git_repo.git.pull(remote, branch)
            else:
                self._git_repo.git.pull()
            return True
        except Exception as e:
            logger.error(f"Error pulling changes: {e}")
            return False
    
    def git_push(self, remote: str = "origin", branch: Optional[str] = None) -> bool:
        """Push changes to remote repository.
        
        Args:
            remote: Remote name
            branch: Branch name (optional)
            
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.is_gitrepo:
            logger.error("Not a git repository")
            return False
        
        try:
            if branch:
                self._git_repo.git.push(remote, branch)
            else:
                self._git_repo.git.push()
            return True
        except Exception as e:
            logger.error(f"Error pushing changes: {e}")
            return False

class LeanRepo(RepoManager):
    pass

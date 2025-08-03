
import os
import shutil
import subprocess
from pathlib import Path
from typing import Optional, List, Dict
import requests

from leanup.const import OS_TYPE, LEANUP_CACHE_DIR
from leanup.utils.basic import execute_command
from leanup.utils.custom_logger import setup_logger

logger = setup_logger("elan_manager")


class ElanManager:
    """Elan toolchain manager"""

    def __init__(self):
        self.elan_home = Path(os.environ.get('ELAN_HOME', Path.home() / '.elan'))
        self.elan_bin_dir = self.elan_home / 'bin'
        
    def get_elan_executable(self) -> Optional[Path]:
        """Get elan executable file path"""
        elan_exe = 'elan.exe' if OS_TYPE == 'Windows' else 'elan'
        elan_path = self.elan_bin_dir / elan_exe
        
        if elan_path.exists() and elan_path.is_file():
            return elan_path
        
        # Try to find in PATH
        elan_in_path = shutil.which('elan')
        if elan_in_path:
            return Path(elan_in_path)
            
        return None
    
    def is_elan_installed(self) -> bool:
        """Check if elan is installed"""
        return self.get_elan_executable() is not None
    
    def get_elan_version(self) -> Optional[str]:
        """Get installed elan version"""
        elan_path = self.get_elan_executable()
        if not elan_path:
            return None
            
        try:
            output, error, code = execute_command([str(elan_path), '--version'])
            if code == 0:
                # Extract version number from output
                for line in output.strip().split('\n'):
                    if 'elan' in line.lower():
                        parts = line.split()
                        for i, part in enumerate(parts):
                            if 'elan' in part.lower() and i + 1 < len(parts):
                                return parts[i + 1]
                return output.strip().split('\n')[0]
            return None
        except Exception as e:
            logger.error(f"Failed to get elan version: {e}")
            return None
    
    def get_download_url(self, version: Optional[str] = None) -> str:
        """Get elan installation script download URL"""
        if OS_TYPE == 'Windows':
            # Windows uses official PowerShell script
            return "https://elan.lean-lang.org/elan-init.ps1"
        else:
            # Linux and macOS use official shell script
            return "https://elan.lean-lang.org/elan-init.sh"
    
    def download_installer(self, url: str, target_path: Path) -> bool:
        """Download elan installer"""
        try:
            logger.info(f"Downloading elan installer: {url}")
            
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(target_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Give execution permission to installation script
            if OS_TYPE != 'Windows':
                target_path.chmod(0o755)
                
            logger.info(f"Download completed: {target_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to download elan installer: {e}")
            return False
    
    def install_elan(self, version: Optional[str] = None, force: bool = False) -> bool:
        """Install elan"""
        
        # Check if already installed
        if self.is_elan_installed() and not force:
            current_version = self.get_elan_version()
            logger.info(f"elan is already installed (version: {current_version})")
            if version is None or current_version == version:
                return True
            logger.info(f"Installing specified version: {version}")
        
        # Create temporary directory
        temp_dir = LEANUP_CACHE_DIR / 'temp'
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        try:
            download_url = self.get_download_url(version)
            
            if OS_TYPE == 'Windows':
                # Windows uses PowerShell to run script directly from network (official recommended way)
                logger.info("Installing elan via PowerShell...")
                # Set environment variables for non-interactive installation
                env = os.environ.copy()
                env['ELAN_HOME'] = str(self.elan_home)
                
                # Use PowerShell to download and execute as recommended by official docs
                script_content = f"""
                $env:ELAN_HOME = "{self.elan_home}"
                Invoke-WebRequest -Uri "https://elan.lean-lang.org/elan-init.ps1" -OutFile "elan-init.ps1"
                & .\\elan-init.ps1 -y
                Remove-Item "elan-init.ps1" -ErrorAction SilentlyContinue
                """
                
                cmd = ['powershell', '-ExecutionPolicy', 'Bypass', '-Command', script_content]
                output, error, code = execute_command(cmd, cwd=str(temp_dir))
                
                if code != 0:
                    logger.error(f"Installation failed: {error}")
                    return False
                    
            else:
                # Linux/macOS use shell script installation
                installer_path = temp_dir / 'elan-init.sh'
                if not self.download_installer(download_url, installer_path):
                    return False
                
                logger.info("Running elan installation script...")
                # Set environment variables for non-interactive installation
                env = os.environ.copy()
                env['ELAN_HOME'] = str(self.elan_home)
                
                cmd = ['sh', str(installer_path), '-y']
                output, error, code = execute_command(cmd)
                
                if code != 0:
                    logger.error(f"Installation failed: {error}")
                    return False
            
            # Verify installation
            if self.is_elan_installed():
                installed_version = self.get_elan_version()
                logger.info(f"elan installed successfully! Version: {installed_version}")
                return True
            else:
                logger.error("Installation completed, but elan executable not found")
                return False
                
        except Exception as e:
            logger.error(f"Error occurred during elan installation: {e}")
            return False
        finally:
            # Clean up temporary files
            try:
                if OS_TYPE != 'Windows' and 'installer_path' in locals() and installer_path.exists():
                    installer_path.unlink()
            except OSError:
                # Ignore file deletion errors
                pass
    
    def proxy_elan_command(self, args: List[str]) -> int:
        """Proxy execute elan command with streaming output"""
        elan_path = self.get_elan_executable()
        
        if not elan_path:
            logger.error("elan is not installed. Please run 'leanup install' to install elan first.")
            return 1
        
        # Build complete command
        cmd = [str(elan_path)] + args
        
        try:
            # Pass directly to subprocess to maintain interactivity and streaming
            result = subprocess.run(cmd, check=False)
            return result.returncode
        except Exception as e:
            logger.error(f"Failed to execute elan command: {e}")
            return 1
    
    def get_installed_toolchains(self) -> List[str]:
        """Get list of installed toolchains"""
        elan_path = self.get_elan_executable()
        if not elan_path:
            return []
        
        try:
            output, error, code = execute_command([str(elan_path), 'toolchain', 'list'])
            if code == 0:
                toolchains = []
                for line in output.strip().split('\n'):
                    line = line.strip()
                    if line and not line.startswith('#'):
                        # Remove status markers (like (default))
                        toolchain = line.split()[0]
                        toolchains.append(toolchain)
                return toolchains
            return []
        except Exception as e:
            logger.error(f"Failed to get toolchain list: {e}")
            return []
    
    def get_status_info(self) -> Dict[str, any]:
        """Get elan status information"""
        info = {
            'installed': self.is_elan_installed(),
            'version': None,
            'elan_home': str(self.elan_home),
            'executable': None,
            'toolchains': []
        }
        
        if info['installed']:
            info['version'] = self.get_elan_version()
            info['executable'] = str(self.get_elan_executable())
            info['toolchains'] = self.get_installed_toolchains()
        
        return info

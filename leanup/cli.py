import click
import sys
from loguru import logger
from .elan_manager import ElanManager
from .const import OS_TYPE


# 配置 loguru
logger.remove()
logger.add(sys.stderr, level="INFO", format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>")


@click.group()
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
def main(verbose):
    """LeanUp - Lean Environment Management Tool
    
    A Python tool for managing Lean mathematical proof language environments.
    """
    if verbose:
        logger.remove()
        logger.add(sys.stderr, level="DEBUG", format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>")


@main.command()
@click.argument('version', required=False)
@click.option('--force', '-f', is_flag=True, help='Force reinstall even if elan exists')
def install(version, force):
    """Install elan toolchain manager
    
    VERSION: Optional version number (installs latest version by default)
    
    Examples:
        leanup install          # Install latest version
        leanup install v1.4.2   # Install specific version
        leanup install --force  # Force reinstall
    """
    manager = ElanManager()
    
    click.echo(f"Installing elan for {OS_TYPE}...")
    
    if version:
        click.echo(f"Specified version: {version}")
    
    success = manager.install_elan(version=version, force=force)
    
    if success:
        click.echo("elan installation successful!")
        
        # Show installation info
        info = manager.get_status_info()
        click.echo(f"Installation location: {info['executable']}")
        click.echo(f"ELAN_HOME: {info['elan_home']}")
        click.echo(f"Version: {info['version']}")
        
        # Hint for next steps
        if OS_TYPE != 'Windows':
            click.echo("\nNote: You may need to restart your terminal or run the following commands to update PATH:")
            click.echo("   source ~/.bashrc")
            click.echo("   # or")
            click.echo("   source ~/.zshrc")
        
        click.echo("\nYou can now use the following commands:")
        click.echo("   leanup elan --help      # Show elan help")
        click.echo("   leanup status           # Check status")
    else:
        click.echo("elan installation failed!")
        sys.exit(1)


@main.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.pass_context
def elan(ctx):
    """Proxy elan commands
    
    Pass all arguments directly to the elan tool. This allows you to use leanup elan just like native elan.
    
    Examples:
        leanup elan --help                    # Show elan help
        leanup elan toolchain list            # List installed toolchains
        leanup elan toolchain install stable  # Install stable toolchain
        leanup elan default stable            # Set default toolchain
        leanup elan update                    # Update toolchains
    """
    manager = ElanManager()
    
    # 传递所有额外参数给 elan
    exit_code = manager.proxy_elan_command(ctx.args)
    sys.exit(exit_code)


@main.command()
def status():
    """Show LeanUp and elan status information"""
    manager = ElanManager()
    info = manager.get_status_info()
    
    click.echo("LeanUp Status Information")
    click.echo("=" * 50)
    
    click.echo(f"Operating System: {OS_TYPE}")
    
    if info['installed']:
        click.echo("elan Status: Installed")
        click.echo(f"Version: {info['version']}")
        click.echo(f"Executable: {info['executable']}")
        click.echo(f"ELAN_HOME: {info['elan_home']}")
        
        toolchains = info['toolchains']
        if toolchains:
            click.echo(f"Installed Toolchains ({len(toolchains)}):")
            for toolchain in toolchains:
                click.echo(f"   • {toolchain}")
        else:
            click.echo("Installed Toolchains: None")
            click.echo("Tip: Run 'leanup elan toolchain install stable' to install stable toolchain")
    else:
        click.echo("elan Status: Not Installed")
        click.echo("Tip: Run 'leanup install' to install elan")


@main.command()
def version():
    """Show LeanUp version information"""
    from . import __version__
    click.echo(f"LeanUp Version: {__version__}")


# 保留原有的 repo 组以保持向后兼容
@main.group()
def repo():
    """Manage Lean repository installations (experimental feature)"""
    pass


if __name__ == '__main__':
    main()


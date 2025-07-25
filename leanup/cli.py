import click
import sys
from loguru import logger
from .elan_manager import ElanManager
from .const import OS_TYPE


# 配置 loguru
logger.remove()
logger.add(sys.stderr, level="INFO", format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>")


@click.group()
@click.option('--verbose', '-v', is_flag=True, help='启用详细输出')
def main(verbose):
    """LeanUp - Lean 环境管理工具
    
    一个用于管理 Lean 数学证明语言环境的 Python 工具。
    """
    if verbose:
        logger.remove()
        logger.add(sys.stderr, level="DEBUG", format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>")


@main.command()
@click.argument('version', required=False)
@click.option('--force', '-f', is_flag=True, help='强制重新安装，即使 elan 已存在')
def install(version, force):
    """安装 elan 工具链管理器
    
    VERSION: 可选的版本号（默认安装最新版本）
    
    示例:
        leanup install          # 安装最新版本
        leanup install v1.4.2   # 安装指定版本
        leanup install --force  # 强制重新安装
    """
    manager = ElanManager()
    
    click.echo(f"正在为 {OS_TYPE} 安装 elan...")
    
    if version:
        click.echo(f"指定版本: {version}")
    
    success = manager.install_elan(version=version, force=force)
    
    if success:
        click.echo("elan 安装成功!")
        
        # 显示安装信息
        info = manager.get_status_info()
        click.echo(f"安装位置: {info['executable']}")
        click.echo(f"ELAN_HOME: {info['elan_home']}")
        click.echo(f"版本: {info['version']}")
        
        # 提示用户可能需要的下一步操作
        if OS_TYPE != 'Windows':
            click.echo("\n提示: 您可能需要重新启动终端或运行以下命令来更新 PATH:")
            click.echo("   source ~/.bashrc")
            click.echo("   # 或者")
            click.echo("   source ~/.zshrc")
        
        click.echo("\n现在您可以使用以下命令:")
        click.echo("   leanup elan --help      # 查看 elan 帮助")
        click.echo("   leanup status           # 查看状态")
    else:
        click.echo("elan 安装失败!")
        sys.exit(1)


@main.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
@click.pass_context
def elan(ctx):
    """代理执行 elan 命令
    
    将所有参数直接传递给 elan 工具。这允许您像使用原生 elan 一样使用 leanup elan。
    
    示例:
        leanup elan --help                    # 查看 elan 帮助
        leanup elan toolchain list            # 列出已安装的工具链
        leanup elan toolchain install stable  # 安装稳定版工具链
        leanup elan default stable            # 设置默认工具链
        leanup elan update                    # 更新工具链
    """
    manager = ElanManager()
    
    # 传递所有额外参数给 elan
    exit_code = manager.proxy_elan_command(ctx.args)
    sys.exit(exit_code)


@main.command()
def status():
    """显示 LeanUp 和 elan 的状态信息"""
    manager = ElanManager()
    info = manager.get_status_info()
    
    click.echo("LeanUp 状态信息")
    click.echo("=" * 50)
    
    click.echo(f"操作系统: {OS_TYPE}")
    
    if info['installed']:
        click.echo("elan 状态: 已安装")
        click.echo(f"版本: {info['version']}")
        click.echo(f"可执行文件: {info['executable']}")
        click.echo(f"ELAN_HOME: {info['elan_home']}")
        
        toolchains = info['toolchains']
        if toolchains:
            click.echo(f"已安装的工具链 ({len(toolchains)}):")
            for toolchain in toolchains:
                click.echo(f"   • {toolchain}")
        else:
            click.echo("已安装的工具链: 无")
            click.echo("提示: 运行 'leanup elan toolchain install stable' 安装稳定版工具链")
    else:
        click.echo("elan 状态: 未安装")
        click.echo("提示: 运行 'leanup install' 安装 elan")


@main.command()
def version():
    """显示 LeanUp 版本信息"""
    from . import __version__
    click.echo(f"LeanUp 版本: {__version__}")


# 保留原有的 repo 组以保持向后兼容
@main.group()
def repo():
    """管理 Lean 仓库安装 (实验性功能)"""
    pass


if __name__ == '__main__':
    main()


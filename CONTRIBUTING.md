# 贡献指南 / Contributing Guide

感谢您对 LeanUp 项目的关注！我们欢迎各种形式的贡献。

Thank you for your interest in contributing to LeanUp! We welcome all kinds of contributions.

## 🚀 快速开始 / Quick Start

### 环境准备 / Environment Setup

1. Fork 并克隆仓库 / Fork and clone the repository:
```bash
git clone https://github.com/yourusername/LeanUp.git
cd LeanUp
```

2. 创建虚拟环境 / Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

3. 安装依赖 / Install dependencies:
```bash
pip install -e .
pip install -r requirements_dev.txt
```

## 🧪 测试 / Testing

运行测试确保一切正常 / Run tests to ensure everything works:

```bash
# 运行所有测试 / Run all tests
pytest tests/ -v

# 运行测试并生成覆盖率报告 / Run tests with coverage
coverage run -m pytest tests/
coverage report -m

# 代码风格检查 / Code style check
ruff check .

# 类型检查 / Type checking
mypy .
```

## 📝 代码规范 / Code Standards

- 使用 Python 3.9+ / Use Python 3.9+
- 遵循 PEP 8 代码风格 / Follow PEP 8 style guide
- 添加适当的类型注解 / Add appropriate type hints
- 为新功能编写测试 / Write tests for new features
- 保持代码覆盖率 > 85% / Maintain code coverage > 85%

## 🔄 提交流程 / Submission Process

1. 创建功能分支 / Create feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. 进行更改并提交 / Make changes and commit:
```bash
git add .
git commit -m "描述你的更改 / Describe your changes"
```

3. 推送到你的 fork / Push to your fork:
```bash
git push origin feature/your-feature-name
```

4. 创建 Pull Request / Create Pull Request

## 📋 提交信息格式 / Commit Message Format

```
类型(scope): 简短描述

详细描述（可选）

类型 / Type:
- feat: 新功能 / new feature
- fix: 修复 bug / bug fix
- docs: 文档更新 / documentation update
- style: 代码格式化 / code formatting
- refactor: 代码重构 / code refactoring
- test: 测试相关 / test related
- chore: 构建/工具相关 / build/tooling related
```

## 🐛 报告问题 / Reporting Issues

报告 bug 或提出功能请求时，请提供：
When reporting bugs or requesting features, please provide:

- 操作系统和版本 / Operating system and version
- Python 版本 / Python version
- LeanUp 版本 / LeanUp version
- 重现步骤 / Steps to reproduce
- 期望行为 / Expected behavior
- 实际行为 / Actual behavior

## 💡 功能请求 / Feature Requests

我们欢迎新功能的建议！请确保：
We welcome suggestions for new features! Please ensure:

- 功能与项目目标一致 / Feature aligns with project goals
- 提供清晰的用例 / Provide clear use cases
- 考虑向后兼容性 / Consider backward compatibility

## 📞 联系我们 / Contact Us

- 通过 GitHub Issues 讨论 / Discuss via GitHub Issues
- 邮箱 / Email: leanprover@outlook.com

感谢您的贡献！🎉
Thank you for your contributions! 🎉

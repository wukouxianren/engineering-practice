# 安全认证系统

## 安装
```bash
pip install -e .


##使用
```bash
auth-login


##测试
```bash
pytest tests/


##项目结构
```test
src/
└── auth_system/
    ├── security.py      # 密码哈希与验证
    ├── authentication.py # 用户认证逻辑
    └── cli.py           # 命令行界面

提交

### 2. 提交到Git
```cmd
git init
git add .
git commit -m "完成安全认证系统模块化重构"
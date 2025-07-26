from setuptools import setup, find_packages

setup(
    name="auth-system",
    version="1.0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],  # 无外部依赖
    entry_points={
        'console_scripts': [
            'auth-login=auth_system.cli:run_login'
        ]
    }
)
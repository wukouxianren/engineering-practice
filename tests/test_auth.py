import pytest
from auth_system.authentication import authenticate, USER_DB
from auth_system.security import hash_password, verify_password

# 测试密码
TEST_PASSWORD = "test@123"
TEST_HASH = hash_password(TEST_PASSWORD)

def test_password_hashing():
    """测试哈希生成和验证"""
    assert verify_password(TEST_PASSWORD, TEST_HASH)
    assert not verify_password("wrong_password", TEST_HASH)

def test_authentication_success():
    """测试认证成功"""
    # 添加测试用户
    USER_DB["test_user"] = TEST_HASH
    assert authenticate("test_user", TEST_PASSWORD)

def test_authentication_failure():
    """测试认证失败"""
    assert not authenticate("unknown_user", TEST_PASSWORD)
    assert not authenticate("admin", "wrong_password")
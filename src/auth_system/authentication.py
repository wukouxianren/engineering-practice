from .security import hash_password, verify_password

# 生成初始admin密码（实际项目中应从数据库获取）
ADMIN_PASSWORD = "secret"
ADMIN_HASH = hash_password(ADMIN_PASSWORD)  # 生成后替换为固定值

USER_DB = {
    "admin": ADMIN_HASH
}

def authenticate(username: str, password: str) -> bool:
    """认证用户"""
    stored_hash = USER_DB.get(username)
    if not stored_hash:
        return False
    return verify_password(password, stored_hash)
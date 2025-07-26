import hashlib
import os

def hash_password(password: str) -> str:
    """使用PBKDF2_HMAC安全哈希密码"""
    salt = os.urandom(16)
    pwdhash = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'), 
        salt, 
        100000  # 迭代次数
    )
    return salt.hex() + pwdhash.hex()

def verify_password(password: str, hashed: str) -> bool:
    """验证密码是否匹配"""
    try:
        # 提取盐值和存储的哈希
        salt = bytes.fromhex(hashed[:32])  # 前32字符是salt的hex
        stored_hash = hashed[32:]
        
        # 计算输入密码的哈希
        pwdhash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        ).hex()
        
        return pwdhash == stored_hash
    except:
        return False
# 修改后的login.py
import bcrypt
import pyfiglet

def hash_password(password):
    """使用bcrypt生成安全哈希"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password, hashed):
    """验证密码是否匹配"""
    try:
        # bcrypt.checkpw 需要字节串输入
        return bcrypt.checkpw(password.encode('utf-8'), hashed)
    except Exception as e:
        print(f"验证错误: {e}")
        return False

def main():
    # 显示炫酷标题
    print(pyfiglet.figlet_format("SECURE LOGIN"))
    
    print("="*30)
    user = input("用户名: ")
    pwd = input("密码: ")
    
    # 预存储用户（实际应从数据库获取）
    valid_users = {
        "admin": b'$2b$12$cnpCK61P3PC7N3Gmjho2yuMPjzecyglPSx6OnPWn6j.XVWUxTyzge'  # 对应"secret"
    }
    
    stored_hash = valid_users.get(user)
    if stored_hash and verify_password(pwd, stored_hash):
        print("\n✅ 认证成功！安全访问授予")
    else:
        print("\n❌ 认证失败！入侵警报")
if __name__ == "__main__":
    main()
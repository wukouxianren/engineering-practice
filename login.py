# 修改后的login.py
import hashlib

def get_sha256(text):
    """生成SHA256哈希值"""
    return hashlib.sha256(text.encode()).hexdigest()

def authenticate(username, password):
    """带加密的认证函数"""
    valid_users = {
        "admin": get_sha256("123456"),
        "user1": get_sha256("password1")
    }
    return valid_users.get(username) == get_sha256(password)

# main函数保持不变...

def main():
    print("=== 登录系统 ===")
    user = input("用户名: ")
    pwd = input("密码: ")
    
    if authenticate(user, pwd):
        print("登录成功！")
    else:
        print("用户名或密码错误")

if __name__ == "__main__":
    main()
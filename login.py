# login.py
def authenticate(username, password):
    """简单认证函数"""
    valid_users = {"admin": "123456", "user1": "password1"}
    return valid_users.get(username) == password

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
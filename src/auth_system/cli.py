from .authentication import authenticate

def run_login():
    """命令行登录界面"""
    print("=" * 30)
    print("安全登录系统")
    print("=" * 30)
    
    user = input("用户名: ")
    pwd = input("密码: ")
    
    if authenticate(user, pwd):
        print("\n✅ 认证成功！安全访问授予")
        return True
    else:
        print("\n❌ 认证失败！请检查用户名或密码")
        return False

if __name__ == "__main__":
    run_login()
"""
改项目主要锻炼的是字典的增删改查

******注册页面******
输入姓名
输入密码
输入确认密码
输入邮箱
输入手机号
"""
print('----------欢迎来到注册页面----------')
# 新建一个空的列表，模型数据库
database = []
# 注册页面
while True:
    user = {}
    username = input('请输入用户名：')
    user['user'] = username
    # 两次密码输入不一致时，从新输入密码
    while True:
        password = input('请输入密码：')
        confirm_password = input('请再次输入密码（要保持一致）：')
        if confirm_password != password:
            print('您两次输入的密码不一致，请从新输入！')
            continue  # continue从头再次执行该循环，break是退出改循环
        else:
            user['password'] = password
            break
        # if confirm_password == password:
        #     user['password'] = password
        # else:
        #     print('您两次输入的密码不一致，请从新输入！')
        #     continue

    email = input('请输入邮箱地址：')
    user['email'] = email
    phone = input('请输入手机号码：')
    user['phone'] = phone
    database.append(user)
    answer = input('您是否继续注册（yes/no）：')
    answer = answer.lower()
    if answer != 'y':
        print('欢迎下次光临！')
        break
print(database)

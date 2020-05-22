"""
游戏
1，选择人物
2，购买武器，金币
3，打仗赢金币
4，选择删除武器
5，查看武器
6，退出游戏
"""
import random

print('*' * 30)
print('\t欢迎来到英雄联盟的世界')
print('*' * 30)
weapon_list = ['屠龙刀']
role = input("请选择游戏人物(1.鲁班 2.后裔 3.李白 4.孙尚香 5.貂蝉):")
coins = 1000
print('欢迎{}来到王者荣耀，当前的金币是{}：'.format(role, coins))

while True:
    choice = input('请选择：\n1.购买武器 \n2.打仗 \n3.删除武器 \n4.查看武器 \n5.退出\n')
    choice = int(choice)
    if choice == 1:
        # 购买武器
        print('欢迎来到武器库，请选择武器(您的剩余金币数为:{})：'.format(coins))
        weapons = [['屠龙刀', 500], ['倚天剑', 400], ['方天画戟', 1200], ['龙魂刀', 200], ['绝世好剑', 1000]]
        for weapon in weapons:
            print(weapon[0], weapon[1], sep='    ')
        # 提示输入购买的武器
        weapon_name = input("请输入你要购买的武器名称：")
        # 1，判断原来没有过武器 2，输入的武器明是否在武器库中
        if weapon_name not in weapon_list:
            #  输入的武器名称是否在武器库
            for weapon in weapons:
                if weapon_name in weapon[0]:
                    # 购买武器
                    if coins >= weapon[1]:
                        coins -= weapon[1]
                        weapon_list.append(weapon[0])  # 添加到自己的武器库中
                        print('购买武器成功,已成功添加到您的武器库中！')
                        print("您剩余的金币为{}".format(coins))
                        for new_weapon in weapon_list:
                            print("您现在武器库中的武器有：{}".format(new_weapon))

                        break
                    else:
                        print("金币不足，请赶紧打仗挣钱或购买其他武器")
                        break
            else:
                print("输入的武器名称错误！")
        elif weapon_name in weapon_list:
            print('您输入的武器名称已存在您的武器库中，请选择其他武器')

    elif choice == 2:
        # 打仗 假设你有多个武器，
        print("*"*20)
        print('进入战场.....')
        if len(weapon_list)>0:
            # 选择武器
            print('{}拥有的武器如下：'.format(role))
            for weapon in weapon_list:
                print(weapon)
            while True:
                weapon_name = input("请选择要带的武器：")
                if weapon_name in weapon_list:
                    #  进入战争状态，默认和张飞比试掷骰子，看谁大
                    ran1 = random.randint(1, 20)  # 张飞的随机数
                    ran2 = random.randint(1, 20)  # role的随机数
                    if ran1 > ran2:
                        print("张飞胜利，不增加金币数！")
                    elif ran1 < ran2:
                        coins += 200
                        print('恭喜{}胜利，金币数为{}'.format(role, coins))
                    else:
                        print("平局，请从新选择")
                    break
                else:
                    print("选择的武器不存在，请从新选择")
        else:
            print("您的武器库中还没有武器，请先购买武器")
    elif choice == 3:
        # 删除武器
        print("武器太多，需要扔掉几个")
        if len(weapon_list) > 0:
            print('{}拥有的武器如下：'.format(role))
            for weapon in weapon_list:
                print(weapon)
            while True:
                weapon_name = input("请输入您要删除的武器名称：")
                if weapon_name in weapon_list:
                    # 删除武器
                    weapon_list.remove(weapon_name)
                    print("武器删除成功")
                    # 思考，删除武器之后，需要归还金币
                    # print(weapon_list)
                    for weapon in weapons:
                        if weapon_name in weapon[0]:
                            coins += weapon[1]
                            print("返回金币数为:{},总金币数:{}".format(weapon[1],coins))
                            break
                    break
                else:
                    print("武器名称输入有误，")
        else:
            print("您武器库中没有武器，无法删除")

    elif choice == 4:
        print('{}拥有的武器如下：'.format(role))
        for weapon in weapon_list:
            print(weapon)
        print("总金币数为：{}".format(coins))
    elif choice == 5:
        answer = input("您确定要离开英雄联盟吗？（yes or no）")
        answer = answer.lower()
        if answer == 'yes':
            break
    else:
        print("您输入的数字不合法，请从新输入")

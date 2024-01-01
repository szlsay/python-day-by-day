'''
   a. 两个角色  玩家 player  - 电脑 robot
   b. 动作: 石头 0 , 剪刀 1,  布 2
   c. 我的出拳: 由输入完成
   d. 电脑的出拳: 随机数完成
   e. 比较出拳
   f. 相等 - 平局
   g. 玩家赢: p0:r1  p1:r2  p2:r0
   h. 剩下的情况就是电脑赢

'''

# 导入随机数模块
import random


# 定义一个函数
def game():
    # 定义一个玩家变量,从键盘输入值
    player = int(input('请输入一个状态(石头 0 , 剪刀 1,  布 2):'))

    # 定义一个电脑变量,使用随机数获取状态
    robot = random.randint(0, 2)

    # 比较状态
    # 先状态平局
    if player == robot:
        print('平局')
    # 再判断玩家赢的状态
    elif ((player == 0) and (robot == 1)) or ((player == 1) and (robot == 2)) or ((player == 2) and (robot == 0)):
        print('玩家赢')
    # 剩下就是电脑赢的状态
    else:
        print('你输出,电脑胜出')



# 函数调用,开始游戏
game()

'''
思考题:
    在这个题目上的基础上,让结果更加清晰
    
    
升级题:
    棒子老虎鸡:
    
    棒子-> 老虎 -> 鸡 -> 虫 -> 棒子
    
扩展题:
    将游戏重复执行,三局两胜

'''


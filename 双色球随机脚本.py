red = []                       #红球空序列
blue = []                      #蓝球空序列
red_win = []                   #随机后红球空序列
import random                  #调取随机模块
for r in range(1,33):          #生成红球序列
    red.append(r)
for b in range(1,17):          #生成蓝球序列
    blue.append(b)
while True:                    #生成不重复随机后红球序列
    r1 = random.choice(red)
    if r1 not in red_win:
        red_win.append(r1)
        if len(red_win) == 6:
            break
red_win.sort()                 #生成红球序列排序
blue_win = random.choice(blue) #生成随机蓝球
#打印双色球
print('随机红球：',red_win)
print('随机蓝球：',blue_win)

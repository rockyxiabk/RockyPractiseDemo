'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
import time


def printDiffNumber():
    res = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and i != k and j != k:
                    res.append("{0}{1}{2}".format(i, j, k))
    print(res)


'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，
可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''


def calcMonthPrize():
    currentMoney = input("Enter a number(0~10000000元):")
    moneyList = [1000000, 600000, 400000, 200000, 100000, 0]
    feeList = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    res = 0
    currentMoney = float(currentMoney)
    for i in range(0, 6):
        if currentMoney > moneyList[i]:
            res += (currentMoney - moneyList[i]) * feeList[i]
            currentMoney = moneyList[i]
        else:
            pass
    print("当前应发奖金：", res)


'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''


def sort_by_three():
    i = 0
    numbs = []
    while i < 3:
        num = int(input("input number:"))
        numbs.append(num)
        i += 1
    numbs.sort()
    print("result:", numbs)


'''
斐波那契数列
'''


def fib_number():
    n = int(input("input a number:"))
    res = fib(n)
    print("当前斐波那契结果：", res)


def fib(num):
    if num == 1 or num == 2:
        return 1
    return fib(num - 1) + fib(num - 2)


'''
输出 9*9 乘法口诀表。
'''


def fun_9_9():
    for i in range(1, 10):
        str_ = ""
        for j in range(1, i + 1):
            str_ += "{0}*{1}={2} \t".format(i, j, i * j)
        print(str_)


'''
暂停一秒输出。
'''


def stop_one_second():
    dic_ = {1: 'a', 2: 'b', 3: 'c'}
    for k in dic_.keys():
        print(k, ":", dic_[k])
        time.sleep(k)


'''
暂停一秒输出，并格式化当前时间。
'''


def format_time_print():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    time.sleep(1)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


'''
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
'''

'''
打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''


def print_water_flower():
    for n in range(100, 1000):
        i = n // 100
        j = n // 10 % 10
        k = n % 10
        if i ** 3 + j ** 3 + k ** 3 == n:
            print(n)

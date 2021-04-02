# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    print("hello world")
    print("你好")
    a = "abc"
    b = "cde"
    print(a)
    print(b)
    del a, b  # del 删除引用
    # 字符串截取
    str = "abcddefg"
    print(str)
    print("输出第一个字符:" + str[0])
    print("输出下标1-3的字符（左闭右开）" + str[1:3])
    print(str * 2)
    # list 列表
    list0 = [23, 'abc', '456', 98.7, 'rocky']
    list1 = ['jobh', 90]
    print("list 列表：", list0)
    print(list0[0])
    print(list0[1:])
    print(list0 * 2)
    print(list0 + list1)
    list1[0] = "ssss"
    print(list1)
    list0.append("jack")  # 增加
    del list0[0]  # 删除一个元素
    # tuple 元组
    tuple = (34, 'asf', "rocky", 39.3, "sdf")
    tuple2 = ('pops', 20)
    print('元组：', tuple)
    print(tuple[1])
    print(tuple[3:])
    print(tuple * 2)
    print(tuple + tuple2)
    del tuple2  # 元组只能删除整个，不能修改单个元素
    curr = list(tuple)
    print("元组->列表：", curr)
    # dict 字典 键值对 无序
    dict = {}
    dict[23] = "23"
    dict["abc"] = "abc"
    tinyDict = {"as": 45, 5: 33, 6: "0d"}
    print('字典：', dict)
    print(dict[23])
    print(dict.keys())
    print(dict.values())
    dict.clear()
    del dict
    # 运算符 +-*/ 加减乘除 ** 幂 % 取余 //向下取整
    a = 23
    b = 6
    print("a/b=", a / b)
    print("b^2=", b ** 2)
    print("a%b=", a % b)
    print("a//b=", a // b)
    print("b/a=", b / float(a))

    """
    var = 1
    while var == 1:
        inNum = raw_input("Enter a number:")
        print("Your enter number:", inNum)
    print("goodbye!")
    """
    for letter in 'apple':
        print('current letter:', letter)
    current = ['apple', 'orange', 'banana']
    # type1 循环
    for i in current:
        print("current friuts:", i)
    # type2 索引
    for j in range(len(current)):
        print("type2 current fruits:", current[j])
    # for else

    for num in range(10, 20):  # 迭代 10 到 20 之间的数字
        for i in range(2, num):  # 根据因子迭代
            if num % i == 0:  # 确定第一个因子
                j = num / i  # 计算第二个因子
                print(num, "%", i, "=", j)
                break  # 跳出当前循环
        else:  # 循环的 else 部分
            print(num, '是一个质数')

    # 嵌套循环
    i = 2
    while i < 100:
        j = 2
        while j <= (i / j):
            if not (i % j):
                break
            j = j + 1
        if j > i / j:
            print(i, " 是素数")
        i = i + 1
    print("Good bye!")
    '''
    break 跳出循环体
    continue 跳出当前循环，进入下一次循环
    '''
    print("aa:", 12, '-', "--0d", 3453, 34, 65)

import cutstom_fun
from utils import file_util
import math
import os

Money = 2000


def addmoney():
    global Money  # 如果要在当前作为全局变量 要加上此句声明
    Money = Money + 1
    return


if __name__ == '__main__':
    aa = cutstom_fun.rocky("dd")
    print("返回值：", aa)
    print("全局变量：", cutstom_fun.sum_total)
    print(Money)
    addmoney()
    print(Money)

    content = dir(cutstom_fun)
    print(content)
    content = dir(math)
    print(content)
    print("--------file-----------")
    try:
        fo = file_util.open_file("test.txt")
    finally:
        print("fo open end")

    print("file name:", fo.name)
    print("file mode:", fo.mode)
    print("file is close:", fo.closed)
    try:
        fo.write("this is test!")
    except IOError:
        print("IO error")
    else:
        print("input success")
    fo.close()
    print("file is close:", fo.closed)
    ro = file_util.read_file("test.txt")
    print("file content:", ro.read(15))
    print("-------os---------------")
    os.rename(ro.name, "rocky.txt")
    path = os.getcwd()  # 当前的目录
    print("path:", path)
    in_content=input("input:")
    print(in_content)
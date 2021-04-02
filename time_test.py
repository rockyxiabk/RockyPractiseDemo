import time
import calendar

if __name__ == '__main__':
    print("time stamp:", time.time())
    print("time local:", time.localtime(time.time()))
    print("本地时间：", time.asctime(time.localtime(time.time())))
    print("时间戳格式化：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    print("-----calendar------")
    calender1 = calendar.month(2021, 3)
    print(calender1)
    print("1900~2021之间的闰年个数：",calendar.leapdays(1900,2021))

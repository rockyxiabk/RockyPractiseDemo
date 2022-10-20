import re

if __name__ == '__main__':
    patternStr = "http://www.baidu.com"
    result0 = re.match('www', patternStr)
    '''
    在开始位置匹配
    '''
    print(result0)

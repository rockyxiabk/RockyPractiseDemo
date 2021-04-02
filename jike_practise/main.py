import clac_word_count

'''
分别用一行和多行条件循环语句，来实现这个功能吗？
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], 
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# expected output:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}, 
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}, 
{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
'''


def print_format():
    attributes = ['name', 'dob', 'gender']
    values = [['jason', '2000-01-01', 'male'],
              ['mike', '1999-01-01', 'male'],
              ['nancy', '2001-02-01', 'female']]
    res = [dict(zip(attributes, value)) for value in values]
    print('print_format:', res)


def print_format2():
    attributes = ['name', 'dob', 'gender']
    values = [['jason', '2000-01-01', 'male'],
              ['mike', '1999-01-01', 'male'],
              ['nancy', '2001-02-01', 'female']]
    res = []
    for value in values:
        res1 = {}
        for i in range(len(value)):
            res1[attributes[i]] = value[i]
        res.append(res1)
    print('print_format:', res)


'''
lambda 匿名函数
'''


def square_def(n):
    return n ** 2


square_def2 = lambda x: x ** 2

'''
对一个字典，根据值进行由高到底的排序
d = {'mike': 10, 'lucy': 2, 'ben': 30}
'''


def sort_def():
    d = {'mike': 10, 'lucy': 2, 'ben': 30}
    s = sorted(d.items(), key=lambda s: s[1], reverse=True)
    print(s)


if __name__ == '__main__':
    print(clac_word_count.solve())
    print_format()
    print_format2()
    print("square :", square_def(10))
    print("square2:", square_def2(10))
    sort_def()

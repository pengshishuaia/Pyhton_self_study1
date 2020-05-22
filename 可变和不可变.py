"""
可变参数 *args

关键字参数： key = value
**kwargs
"""
#  isinstance():isinstance() 函数是 python  中的一个内置函数，主要用于检测变量类型，返回值是bool值 ，
#  在python内置函数中，与该函数相似的还有另外一个内置函数  type()。



# 可变参数
def study(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)


study(3, 4, 4, 2, 4, 5, name='彭帅', age=28)
list1 = {'name':'彭帅','age':18}
study(3, 4, 4, 2, 4, 5, **list1)


# 关键字参数

def add(a, b=10):
    result = a + b
    print(result)


add(6)  # a = 6 b = 10
add(6, 4)  # a = 6 b=4

def add1(a,b=5,c=6):
    result = a+b+c
    print(result)
    isinstance()

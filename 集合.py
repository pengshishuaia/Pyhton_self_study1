"""
集合（set）：集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，
为 { } 是用来创建一个空字典。
特点：1，无序的 2，不重复的
     2，不支持*和+
 a - b    集合a中包含而集合b中不包含的元素
 a | b    集合a或b中包含的所有元素
 a & b    集合a和b中都包含了的元素
 a ^ b    不同时包含于a和b的元素
 1、添加元素
    s.add( x ),将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
    s.update( x )可以添加元素，且参数可以是列表，元组，字典等,x 可以有多个，用逗号分开：
 2.删除元素
    s.remove( x )将元素x从集合s中移除，如果元素不存在，则会发生错误
    s.discard( x )移除集合中的元素，且如果元素不存在，不会发生错误
    s.pop() 随机删除集合中的一个元素
 3.计算集合元素个数 len(s)
 4.清空集合 s.clear()
 5.判断元素是否在集合中存在，语法格式如下：x in s，判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。


"""

a = set('abracadabra')
b = set('alacazam')
print(a)
# print(type(a))
print(b)
# print(type(b))
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
c = set()
c.add('ps')
print(c)
c.update({'name':'彭帅'},{'age':99},(1,2,3,2))
print(c)
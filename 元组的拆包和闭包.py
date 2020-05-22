info = [('张三', 18, '中国', (90, 80, 70)),
        ('李四', 16, '中国', (67, 57, 87)),
        ('王五', 19, '中国', (96, 97, 98))]
for i in info:
    print(i)

'''
元组的特点：
1，符号（1,2,3） tuple
2,关键字：tuple
3,元组的元素只能截取，不能增删改
符号：* +  is not in not in
系统函数：
max()
min()
sum()
len()
sorted() ---- 排序，返回的结果是列表
tuple() ---强制转换元组类型
index（）
count（）
拆包和装包
x,*y = (1,2,34,56)
print(y)
print(*y)
'''
x,*y = (1,2,34,56)
print(y)
print(*y)
'''
查询
列表根据下表查询
字典根据key查询
for key in dict
字典的遍历，拿到的是key

字典里面的内置函数items（） keys() values()
'''
# 打印份数大于90的学生
dictionary = {'张三':99, '李四':88, '王五':97}
print(dictionary.items())
for key,values in dictionary.items():
    #print(key,values)
    if values >=90:
        print(key)


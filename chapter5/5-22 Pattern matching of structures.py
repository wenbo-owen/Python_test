"""
结构的模式匹配
Pattern matching of structures

"""

data = eval(input('请输入要匹配的数据: '))

match data:
    case {'name':'wenbo','age':20}:
        print('字典')
    case [10,20,30]:
        print('列表')
    case(10,20,30):
        print('元组')
    case _:
        print('相当于多重if中的else')
"""
同步迭代

"""

fruits ={'apple', 'banana', 'cherry','pear'}  #集合是无序的
fruits1 =['apple', 'banana', 'cherry','pear']  #集合是无序的

counts = [10,3,4,5]

for f,c in zip(fruits1,counts):
    match f,c:
        case 'apple',10:
            print('10个苹果')
        case 'banana', 3:
            print('3个香蕉')
        case 'cherry', 4:
            print('4个樱桃')
        case 'pear', 5:
            print('5个梨')

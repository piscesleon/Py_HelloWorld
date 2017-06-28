import copy
spam=['A','B','C','D']
cheese=copy.copy(spam)
cheese[1]=42
print(spam)
print(cheese)


# 在字典中添加 键-值
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
print(birthdays)
birthdays['Additional']='Added Date'
print(birthdays)
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

# 获取嵌套字典中，二级字典的键列表
def getAllItems(guests):
    AllItemList=[]
    for v in guests.values():
        for k in v.keys():
            if k not in AllItemList:
                AllItemList.append(k)
            else:
                True
    return AllItemList

AllItemList=getAllItems(allGuests)
print(AllItemList)

# 对每个二级字典的键列表的值，取得对应的数量
def getTotalBrought(guest, item):
    numBrought=0
    for k, v in guest.items():
        numBrought=numBrought+v.get(item,0)
    return numBrought

# 打印物品名+数量
for i in AllItemList:
    print(i + ' ' + str(getTotalBrought(allGuests, i)))
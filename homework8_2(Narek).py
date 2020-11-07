list_1 = [9,5,8,5,20,1,2,-3,-2,-1,0]
list_1.sort()
list_1.reverse()
list_2 = list_1[0:3]
list_3 = list_1[len(list_1)-2:len(list_1)]
list_3_count=1
for el in list_3:
    list_3_count *= el
list_3_count *=list_1[0]
list_2_count = 1
for elem in list_2:
    list_2_count*=elem
if list_3_count > list_2_count:
    print(list_3_count)
else:
    print(list_2_count)

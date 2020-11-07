list_1 = [9,5,8,5,20,1,2,-3,-2,-1,0]
list_1.sort()
list_1.reverse()
list_2 = list_1[0:3]
count = 1
for el in list_2:
    count *= el
print(count)
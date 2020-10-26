list_1 = [1,5,20,30]
d = list_1[-1]-list_1[-2]
list_1.append(d)
list_1.sort()
new_list = []
for i in range(len(list_1)-1,0,-1):
    d=list_1[1]
    if list_1[i]-d == list_1[i-1] + d:
        new_list.append(list_1[i]-d)
for el in new_list:
    list_1.append(el)
list_1.sort()
if sum(list_1[1:]) % d == 0:
    print(True,list_1)
else:
    print(False)

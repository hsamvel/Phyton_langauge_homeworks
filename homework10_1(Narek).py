list_1 = [5,9,2,12,5,8]
count = 0
for i in range(0,len(list_1)-1,1):
    if abs(list_1[i]-list_1[i+1]) > count:
        count = abs(list_1[i]-list_1[i+1])
print(count)

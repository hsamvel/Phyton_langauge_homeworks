list_1 = [4,8,12]
n = input().split(',')
for el in n:
    list_1.append(int(el))
list_1.sort()
i = 2
d = list_1[2] - list_1[1]
while i < len(list_1) and list_1[i] - list_1[i-1] == d:
    i += 1
if i == len(list_1):
    print(True, list_1)
else:
    print(False)
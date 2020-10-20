list_1 = [1,1,1]
def b(list_1):
    count = 0
    for i in range(len(list_1)-1):
        j = i +1
        while list_1[j] <= list_1[i]:
            list_1[j] += 1
            count += 1
    return count
print(b(list_1))
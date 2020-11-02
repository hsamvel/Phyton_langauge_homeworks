def sorted_list(list_1):
    new_list = []
    count = 0
    for i in range(len(list_1)):
        if list_1[i] == -1:
            new_list.append(i)
            count += 1
    list_1.sort()
    list_2 = list_1[count:]
    for i in range(len(new_list)):
        list_2.insert(new_list[i],-1)
    return list_2


s_list =[2,-1,1,5,4,-1,3]
print(sorted_list(s_list))


list_1 = [5,4,6,9,3]
def a(list_1):
    new_list = []
    for i in range(1,len(list_1),1):
        if list_1[i] > list_1[i-1]:
            continue
        else:
            new_list.append(list_1[i])
    if len(new_list) == 1:
        print(True)
    else:
        print(False)
a(list_1)    
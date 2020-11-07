def non_decreasing_sequence(*nums):
    list_1 = [*nums]
    new_list = []
    for i in range(len(list_1)-1):
        if list_1[i]<abs(list_1[i+1]) and list_1[i]>list_1[i+1]:
            list_1[i+1]= abs(list_1[i+1])
        if list_1[i]>=abs(list_1[i+1]):
            list_1[i]= -(list_1[i])
    count = 0 
    for i in range(len(list_1)-1):
        if list_1[i] <= list_1[i+1]:
            count += 1
    if len(list_1)-count == 1:
        print('Yes',list_1)
    else:
        print('no')
            

non_decreasing_sequence(1,1,0)
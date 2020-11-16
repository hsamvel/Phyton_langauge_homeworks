list_1 =[5,2,2,5,3]


def sum_of_pairs(list_1,number):
    for i in range(len(list_1)):
        if number - list_1[i] in list_1:
            return number-list_1[i],list_1[i]
    return '' 


print(sum_of_pairs(list_1,8))

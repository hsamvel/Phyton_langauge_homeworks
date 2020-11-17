list_1 =[4, 2, 2, 5, 3]


def sum_of_pairs(list_1,number):
    for i in range(len(list_1)):
        if number - list_1[i] in list_1:
            if number - list_1[i] == list_1[i] and list_1.count(list_1[i]) != 1:
                return number - list_1[i] , list_1[i]
            if number - list_1[i] != list_1[i]:
                return number - list_1[i],list_1[i]
    return '' 


print(sum_of_pairs(list_1,8))

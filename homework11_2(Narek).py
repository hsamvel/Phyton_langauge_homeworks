list_1 =[1,4,4,5,2]


def sum_of_pairs(list_,number):
    for i in range(len(list_)-1):
        if list_[i]+list_[i+1] == number:
            return list_[i],list_[i+1]
    return ''


print(sum_of_pairs(list_1,8))
list_1 = [1,4,6,5,7,10]
def swap_list_elements(list_1):
    kent = [] 
    zuyg=[]
    for el in list_1:
        if el % 2 == 0:
            zuyg.append(el)
        else:
            kent.append(el)
    new_list = []
    i = 0
    while i < len(kent):
        new_list.append(zuyg[i])
        new_list.append(kent[i])
        i+=1
    return new_list


print(swap_list_elements(list_1))
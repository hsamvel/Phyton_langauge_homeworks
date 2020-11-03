dict_1 = {'A' : (0,0),'B' : (0,4),'C':(2,0),'D':(2,4),'E':(0,-4),'F':(2,-4)}
new_list = []
list_2 = []
for elem in dict_1:
    new_list.append(sum(dict_1[elem]))
    list_2.append(elem)
print(new_list)
dict_2= {}
for i in range(0,len(new_list),1):
    for j in range(1,len(new_list),1):
        if list_2[i] != list_2[j]:
            dict_2[list_2[i]+list_2[j]]= abs(new_list[j]-new_list[i])
print(dict_2)

    
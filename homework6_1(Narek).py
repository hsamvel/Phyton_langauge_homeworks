a=list('A1')
b=list('B5')
list1 = [int(el) for el in a if el.isdigit()]
list2 = [int(elem) for elem in b if elem.isdigit()]
if list1[0] % 2  ==  list2[0] % 2:
    print(False)
else:
    print(True)
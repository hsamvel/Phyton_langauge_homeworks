list_1 = [2,2,2,2,2,2,1,2]
count = 0
def weighing_machine(list_1,a=0):
    global count
    if count == 3:
        if list_1[-1] % 2 != 0:
            return len(list_1)-1
        else:
            return len(list_1)-2
    if sum(list_1[a:a+2]) % 2 != 0:
        if list_1[a] % 2 ==1:
            return a 
        return a + 1
    else:
        count += 1
        return weighing_machine(list_1,a=a+2)

print(weighing_machine(list_1))
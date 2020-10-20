n = int(input())
names = []
grades = []
for i in range(n):
    names.append(input())
    grades.append(float(input()))
list_1 = [names,grades]
minn = 500
for el in list_1[1]:
    if el < minn and el > min(list_1[1]):
        minn = el
print(list_1[0][list_1[1].index(minn)])



    

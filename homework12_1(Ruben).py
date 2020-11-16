a = [[10,9,6,3,7],
     [6,10,2,9,7],
     [7,6,3,8,2],
     [8,9,7,9,9],
     [6,8,6,8,2]]
i = -1 
j = 0 
new_a = []
def rotateImage(a):
    global i,j,new_a
    if j >= len(a):
        return new_a
    row = []
    while abs(i) <= len(a):
        row.append(a[i][j])
        i -= 1 
    new_a.append(row)
    j += 1
    i = -1 
    return rotateImage(a)
print(rotateImage(a))

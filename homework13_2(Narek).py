def search_(matrix,value):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == value:
                return i,j
    return -1

matrix = [[10, 20, 30, 40],
          [15, 25, 35, 45],
          [27, 28, 37, 48],
          [32, 33, 29, 50]]
print(search_(matrix,29))

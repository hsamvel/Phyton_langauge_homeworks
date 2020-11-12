number = int(input())
count = 0
for i in range(1,number+1):
    for el in str(i):
        if '2' in el:
            count += 1
print(count)

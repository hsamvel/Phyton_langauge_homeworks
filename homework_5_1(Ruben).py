n = input().split(', ')
m = [input().split(', ') for i in range(len(n))]
our_vars = []
names = input().split(', ')
new_list = []
for i in range(len(m)):
    for elem in names:
        if elem not in m[i]:
            our_vars.append(elem)
for j in range(len(m)):
    if our_vars[0] in m[j]:
        new_list+=m[j]
for c in range(len(n)):
    if len(new_list)== int(n[c][-1]):
        print(our_vars[0],n[c][0:-2],sep=':')
            

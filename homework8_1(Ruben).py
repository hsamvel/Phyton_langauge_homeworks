def answer_queries(k,*query_counts):
    list_1 = [*query_counts]
    a = 0
    count = 0
    if len(list_1) == 1:
        count = (list_1[0]+k) // k
        return count
    else:
        for el in list_1:
            count += 1
            if el >= k:
                a+= abs(el-k)
            if el < k and a!=0:
                a = a-(k-el)
            elif el < k and a==0:
                return count 
        
    
print(answer_queries(5,10,5,5,3,2,1))
            
            
    
    
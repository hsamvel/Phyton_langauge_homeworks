def str_vs_str(str1,str2):
    count = 0
    for el in str1:
        if el in str2:
            if list(str1).count(el) == list(str2).count(el):
                count += 1
    if count == len(str2):
        return True
    return False


print(str_vs_str( 'abcde','ceafb'))
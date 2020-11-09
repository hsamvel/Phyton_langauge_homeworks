string_1 = input()
def buildPalindrome(string_1):
    if string_1 == string_1[-1::-1]:
        return string_1
    if string_1[-1] != string_1[0] and string_1[-1] != string_1[1]:
        string_1 += string_1[1]
    elif string_1[-1] == string_1[0]:
        string_1 += string_1[1]
    else:
        string_1 += string_1[0]
    return buildPalindrome(string_1)


print(buildPalindrome(string_1))

#abcdc
#ababab
#abba
#abaa
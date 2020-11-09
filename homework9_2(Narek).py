string_1 = '(bar)'


def reverse_string(string_1):
    string_1 = string_1.replace(string_1[string_1.rfind('('):string_1.find(')')+1],string_1[string_1.find(')')-1:string_1.rfind('('):-1])
    if string_1.count(')') == 1:
        return reverse_string(string_1)
    return string_1

print(reverse_string(string_1))

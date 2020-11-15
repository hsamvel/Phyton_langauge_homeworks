count = 0


def count_elements_of_number(number):
    global count
    if number < 10:
        count += 1
    else:
        count += 1
        return count_elements_of_number(number // 10)
    return count


print(count_elements_of_number(999))
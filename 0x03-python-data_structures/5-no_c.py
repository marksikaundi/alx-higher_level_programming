#!/usr/bin/python3
def no_c(my_string):
    strlen = len(my_string)

    k = 0

    new_str = my_string[:]

    for j in range(strlen):
        if (my_string[j] == 'c' or my_string[j] == 'C'):
            new_str = new_str[:(j - k)] + my_string[(j + 1):]
            k += 1

    return (new_str)

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numm = 0
    try:
        for j in my_list[:x]:
            print("{}".format(j), end="")
            numm += 1
        print()
        return numm
    except IndexError:
        print()
        return numm

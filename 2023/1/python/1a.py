


import re


# first and last digit
first = "^.*?([\d])"
last = ".*(\d).*$"
call = 0
with open("../input.txt") as fp:
    for line in fp:
        s_first = int(re.search(first, line).group(1))
        s_last  = int(re.search(last, line).group(1))
        print(s_first, s_last)
        call += s_first * 10
        call += s_last
        print(call)
    # print("total",total)



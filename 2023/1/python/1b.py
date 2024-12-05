


import re


# first and last digit
first = "^.*?(\d|one|two|three|four|five|six|seven|eight|nine)"
last = ".*(\d|one|two|three|four|five|six|seven|eight|nine).*$"

s2i = {
        'one': 1,
        '1': 1,
        'two': 2,
        '2': 2,
        'three':3,
        '3':3,
        'four':4,
        '4':4,
        '5':5,
        'five':5,
        'six':6,
        '6':6,
        'seven':7,
        '7':7,
        'eight':8,
        '8':8,
        'nine':9,
        '9':9,
        '0':0,
        'zero':0
        }
call = 0
with open("../input.txt") as fp:
    for line in fp:
        s_first = s2i[re.search(first, line).group(1)]
        s_last  = s2i[re.search(last, line).group(1)]
        print(s_first, s_last)
        call += s_first * 10
        call += s_last
        print(call)
    # print("total",total)



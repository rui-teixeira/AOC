import functools
import time

def update(w1):
    w2 = []
    for s in w1:
        for d in blink(s):
            # print(d)
            w2.append(d)
    return w2


@functools.cache
def mul(d):
    return d * 2024

@functools.cache
def blink(d):
    # print(d)
    if d == 0:
        return([1])

    s = str(d)
    l = len(s)
    if l % 2 == 0:
        i = l // 2
        d1, d2 = int(s[:i]), int(s[i:])
        return([d1, d2])
    else:
       return [mul(d)]

def w2s(w):
    return " ".join([str(d) for d in w])



file_name = '../test.txt'
file_name = '../input.txt'
for line in open(file_name):
    w = [int(s) for s in line.strip().split(" ")]

    # print("Initial arrangement:")
    # print(w2s(w))

    for i in range(1,75+1):
        w = update(w)
        print(f"After {i} blink{'s' if i > 1 else''}: {len(w)}")
        # print(w2s(w))
        # print()
    print(len(w))




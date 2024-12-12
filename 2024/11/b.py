import functools
import time



@functools.cache
def mul(d):
    return d * 2024

# @functools.cache
def blink():
    global w
    global i
    d = w[i]

   #  if d == 0:
   #      w[i] = 1
   #      i += 1

   # #  s = str(d)
   #  l = len(s)
   #  if l % 2 == 0:
   #      i = l // 2
   #      d1, d2 = int(s[:i]), int(s[i:])
   #      w[i] = d1
   #      i += 1
   #      w.insert(i, d2)
   #      i += 1
   #  else:
   #      w[i] = mul(d)
   #      i += 1

def w2s():
    global w
    return " ".join([str(d) for d in w])

file_name = '../test.txt'
file_name = '../input.txt'
file_name = '../test.txt'
w = []
i = 0
i_max = 0
for line in open(file_name):
    w = [int(s) for s in line.strip().split(" ")]

    # print("Initial arrangement:")
    # print(w2s(w))
    for j in range(1,25+1):
        i_max = len(w)
        while i < i_max:
            blink():

        print(f"After {j} blink{'s' if j > 1 else''}: {len(w)}")
        # print(w2s())
        # print()
    print(len(w))




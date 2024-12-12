from collections import Counter
import functools

def mul(s):
    return str(int(s) * 2024)

def split(stone) -> (str, str):
    i = len(stone) // 2
    return str(int(stone[:i])), str(int(stone[i:]))

def blink(counter) -> Counter:
    new_counter = Counter()
    for stone, c in counter.items():
        # print(stone, c)
        if stone == '0':
            new_counter['1'] += c
            continue
        if len(stone) % 2 == 0:
            s1, s2 = split(stone) 
            new_counter[s1] += c 
            if s2 == '':
                new_counter['0'] += c 
            else:
                new_counter[s2] += c 
            continue
        else:
            new_counter[mul(stone)] += c
    return new_counter


file_name = '../test.txt'
file_name = '../input.txt'
for line in open(file_name):
    counter = Counter()
    for stone in line.strip().split(" "):
        counter[stone] += 1 
    # print("Initial arrangement:")
    # print(counter)
    for j in range(1,75+1):
        counter = blink(counter)

        print(f"After {j} blink{'s' if j > 1 else''}: {counter.total()}")
       #  print(counter)
    print(counter.total())




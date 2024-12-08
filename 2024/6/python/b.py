from pprint import pprint
import logging
import traceback
from collections import defaultdict
import copy

g = ''
i = 0
j = 0

area = []
traps = {}
traps_set = set()
loops = []

i_max = 0
j_max = 0

file = '../test.txt'
file = "../input.txt"
rot = {
        '^' : '>',
        '>' : 'v',
        'v' : '<',
        '<' : '^'
        }

rot_r = {
        '^': '<',
        '>': '^',
        'v': '>',
        '<': 'v',
        }
area = []
corners = []

def add_trap(g,j,i):
    print("add_trap", g, j, i)
    traps_set.add((g,j,i))
    traps_set.add(('_',j,i))

def check_trap(g,j,i):
    # print("check_trap", g,j,i)
    return (g,j,i) in traps_set

def print_area(show_traps=False):
    print()
    for l, line in enumerate(area):
        for c, char in enumerate(line):
            if show_traps and ('_',l,c) in traps_set:
                print("O", end='')
            else:
                print(char, end='')
        print()

# figure out all the 
def mark_traps(g,j,i):
    global area
    global traps
    gr = rot_r[g]
    # | #
    # |O^
    if g == '^':
        if i == 0 or j == j_max:
            return
        k = i - 1
        for l in range(j+1,j_max):
            if area[l][i] == '#':
                break
            if area[l][k] == '#':
                continue
            add_trap(gr,l,k)

    #  --
    #  O
    #  >#
    if g == '>':
        if j == 0 or i == 0:
            return
        l = j - 1
        for k in range(i, -1, -1):
            # look for the line end
            if area[j][k] == '#':
                break
            # no point placing if objs already exist
            if area[l][k] == '#':
                continue
            add_trap(rot_r[g],l,k)
    #  
    #  vO| 
    #  # |
    if g == 'v':
        if j == 0 or i == i_max:
            return
        k = i + 1
        for l in range(j, -1, -1):
            # look for the line end
            if area[j][k] == '#':
                break
            # no point placing if objs already exist
            if area[l][k] == '#':
                continue
            add_trap(rot_r[g],l,k)
    #  
    #  #<
    #   O 
    #  --
    if g == '<':
        if j == j_max or i == i_max:
            return
        l = j + 1
        for k in range(j, -1, -1):
            # look for the line end
            if area[j][k] == '#':
                break
            # no point placing if objs already exist
            if area[l][k] == '#':
                continue
            add_trap(rot_r[g],l,k)


def step(check):
    global g,i,i_max, j, j_max
    global area
    global corners
    global traps
    global loops
    try:
        # print('g',g)
        # print("at:",j,i)

        # where are you going?
        if g == '^':
            j2, i2 = j-1, i
        if g == '>':
            j2, i2 = j, i+1
        if g == 'v':
            j2, i2 = j+1, i
        if g == '<':
            j2, i2 = j, i-1

        n = area[j2][i2]
        # print('going',j2,i2)
        # print('n',n)
        # bounds check
        if j2 < 0 or j2 >= j_max or i2 < 0 or i2 >= i_max:
            area[j][i] = 'X'
            return "gone!"

        if n == '#':
            # found obstacle
            if not check:
                mark_traps(g,j,i)
            g = rot[g]
            area[j][i] = g
            corners.append((j,i))
            return "turning.."

        if n == '.' or n == 'X':
            if check:
                if check_trap(g,j2,i2):
                    print('loop', g, j2, i2)
                    loops.append((g,j2,i2))
            # clear
            area[j][i] = 'X'
            area[j2][i2] = g
            i,j = i2,j2
            return 'walking..'

        return "gone"
    except Exception as e:
        logging.error(traceback.format_exc())
        # out of bounds
        area[j][i] = 'X'
        return "gone"


        
def guard():
    for j, l in enumerate(area):
        for i, s in enumerate(l):
            if s in '^>V<':
                return [s, j, i]

#  find the traps
with open(file) as fp:
    for line in fp:
        area.append([s for s in line.strip()])

    i_max = len(area[0])
    j_max = len(area)

    [g, j, i] = guard()

    while True:
        print_area(show_traps=True)
        a = step(False)
        print(a)
        if a[0] == 'g':
            break

    print_area()

# PART2    
with open(file) as fp:
    print("##################PART2!!!")
    area = []
    print(traps)
    for line in fp:
        area.append([s for s in line.strip()])

    [g, j, i] = guard()
    print(g,j,i)

    while True:
        for l in range(len(area)):
            for k in range(len(area[l])):
                if (g,l,k) in traps_set:
                    print('O', end="")
                else:
                    print(area[l][k], end="")
            print()
        a = step(True)
        print(a)
        if a[0] == 'g':
            break

    print('loops',loops)
    print(len(loops))

    print_area(show_traps=False)

    print_area(show_traps=True) 

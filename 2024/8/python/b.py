import math

class World:
    antenas = {}
    anodes = {} 
    raw = []
    j_max = 0
    i_max = 0

    def read(this, buff):
        for j, line in enumerate(buff):
            this.raw.append([])
            for i, c in enumerate(line.strip()):
                this.raw[j].append(c)
                if c != '.':
                    if c in this.antenas:
                        this.antenas[c].append((j,i))
                    else:
                        this.antenas[c] = [(j,i)]
        this.j_max = len(this.raw)
        this.i_max = len(this.raw[0])
                

    def show(this, grid=False, anodes=False):
        if anodes:
            for t in this.anodes:
                for p in this.anodes[t]:
                    print(p)
                    this.raw[p[0]][p[1]] = '#'
                
        for line in this.raw:
            for c in line:
                print(c, end='')
            print()

    def add_anode(this, t, p, check=True):
        try:
            this.anodes[t].append(p)
        except:
            this.anodes[t] = [p]

    def count_anodes(this):
        count = 0
        for line in this.raw:
            for c in line:
                if c != '.':
                    count += 1
        return count


def bounds(j, j_max, i, i_max):
    return i >=0 and i < i_max and j >= 0 and j < j_max

def calc(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])
#
#     0123456
#     |||||||
# 0 - #...... 
# 1 - .......
# 2 - ..a....
# 3 - .......
# 4 - ....b..
# 5 - .......
# 6 - ......#
#
#
#     0123456
#     |||||||
# 0 - ......# 
# 1 - .......
# 2 - ....a..
# 3 - .......
# 4 - ..b....
# 5 - .......
# 6 - #......
#
def calc2(a, b):
    d0 = abs(a[0] - b[0])
    d1 = abs(a[1] - b[1])
    a2_0 = 0
    a2_1 = 0
    b2_0 = 0
    b2_1 = 0
    if a[0] > b[0]:
        a2_0 = a[0] + d0
        b2_0 = b[0] - d0
    else:
        a2_0 = a[0] - d0
        b2_0 = b[0] + d0
    if a[1] > b[1]:
        a2_1 = a[1] + d1
        b2_1 = b[1] - d1
    else:
        a2_1 = a[1] - d1
        b2_1 = b[1] + d1
    return (a2_0, a2_1), (b2_0,b2_1)

def calc3(a,b, j_max, i_max):
    aj = a[0]
    ai = a[1]
    bj = b[0]
    bi = b[1]
    dj = abs(aj - b[0])
    di = abs(a[1] - b[1])
    gcd = math.gcd(dj,di)
    dj = dj / gcd
    di = di / gcd
    ps = []
    # find quadrant 

    if aj < b[0] and a[1] < b[1]:
        # even quadrant
        # going 'back' from a
        c = 1
        while True:
            pj = int(aj - dj * c)
            pi = int(ai - di * c)
            if bounds(pj, j_max, pi, i_max):
                ps.append((pj,pi))
            else:
                break
            c += 1
        # going 'forward' from a
        c = 1
        while True:
            pj = int(aj + dj * c)
            pi = int(ai + di * c)
            if bounds(pj, j_max, pi, i_max):
                ps.append((pj,pi))
            else:
                break
            c += 1
    else:
        # odd or ortho quadrant
        # going 'back' from a
        c = 1
        while True:
            pj = int(aj - dj * c)
            pi = int(ai + di * c)
            if bounds(pj, j_max, pi, i_max):
                ps.append((pj,pi))
            else:
                break
            c += 1
        # going 'forward' from a
        c = 1
        while True:
            pj = int(aj + dj * c)
            pi = int(ai - di * c)
            if bounds(pj, j_max, pi, i_max):
                ps.append((pj,pi))
            else:
                break
            c += 1
    return ps





debug = False
# with open("../test.txt") as fp:
with open("../input.txt") as fp:
    w = World()
    w.read(fp)
    if debug: w.show()
    if debug: print(w.antenas)
    for t in w.antenas:
        if debug: print("calc anodes for",t)
        i = 0
        j = 1
        num_of_t = len(w.antenas[t])
        if debug: print("\tFound",num_of_t, "antenas")
        for i in range(i, num_of_t):
            a1 = w.antenas[t][i]
            if debug: print("\tcalc for antena",i, t, a1)
            for j in range(i+1, num_of_t):
                a2 = w.antenas[t][j]
                if debug: print("\t\twith antena",j, t, a2)
                anodes = calc3(a1, a2, w.j_max, w.i_max)
                for p in anodes:
                    w.add_anode(t,p)
        if debug: print("anodes", t, len(w.anodes[t]), w.anodes[t])
    w.show(anodes=True)
    print("num of anode locs", w.count_anodes())

    




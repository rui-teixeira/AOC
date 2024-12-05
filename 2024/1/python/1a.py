with open("../input.txt") as fp:
    a = []
    b = []
    for line in fp:
        ai, bi = line.split("   ")
        a.append(int(ai))
        b.append(int(bi))
    a.sort()
    b.sort()
    total = sum([abs(i-j) for i, j in zip(a,b)])
    print("total",total)



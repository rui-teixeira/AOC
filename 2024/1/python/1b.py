with open("../input.txt") as fp:
    a = []
    b = []
    for line in fp:
        ai, bi = line.split("   ")
        a.append(int(ai))
        b.append(int(bi))
    a.sort()
    b.sort()
    simi = 0
    j = 0
    for i, u in enumerate(a):
        print(i,u)
        c = 0 # how many times i appears in b
        while True:
            try:
                if u == b[j]:
                    c += 1
                    j += 1
                elif b[j] >= u:
                    break
                else:
                    j += 1
            except: 
                break
        simi += u * c
        print(u, c)
    print("simi", simi)




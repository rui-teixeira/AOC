# with open("../test.txt") as fp:

def check(levels):
    safe = False
    dec = True
    if levels[0] == levels[1]:
        print("levels", levels)
        print("unsafe")
        safe = False
        return safe
    elif levels[0] > levels[1]:
        dec = True
    else: dec = False

    safe = False
    for i in range(len(levels)-1):
        if levels[i] == levels[i+1]:
            print("levels", levels)
            print("unsafe")
            safe = False
            break
        elif dec and levels[i] < levels[i+1]:
            print("levels", levels)
            print("unsafe")
            safe = False
            break
        elif not dec and levels[i] > levels[i+1]:
            print("levels", levels)
            print("unsafe")
            safe = False
            break
        if abs(levels[i]-levels[i+1]) > 3:
            print("levels", levels)
            print("unsafe")
            safe = False
            break
        safe = True
    return safe

with open("../input.txt") as fp:
    count = 0
    for line in fp:
        strikes = 0
        levels = [int(a) for a in line.split(" ")]

        if check(levels):
            count += 1
        else:
            for i in range(len(levels)):
                levels_n = levels[:]
                del levels_n[i]
                safe = check(levels_n)
                if safe:
                    count += 1
                    break
                else:
                    continue
    print("count",count)



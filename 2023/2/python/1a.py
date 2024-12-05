# with open("../test.txt") as fp:

def check(lvls):
    safe = False
    print("levels", levels)
    dec = True
    if levels[0] == levels[1]:
        print("unsafe")
        safe = False
        return safe
    elif levels[0] > levels[1]:
        dec = True
    else: dec = False

    safe = False
    for i in range(len(levels)-1):
        if levels[i] == levels[i+1]:
            print("unsafe")
            safe = False
            break
        elif dec and levels[i] < levels[i+1]:
            print("unsafe")
            safe = False
            break
        elif not dec and levels[i] > levels[i+1]:
            print("unsafe")
            safe = False
            break
        if abs(levels[i]-levels[i+1]) > 3:
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
        count += 1 if check(levels) else 0
    print("count",count)



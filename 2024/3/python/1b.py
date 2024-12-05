import re
mulr = r'mul\((\d+),(\d+)\)'
do = r'do\(\)'
dont = r'don\'t\(\)'

# with open("../example.txt") as fp:
with open("../input_concat.txt") as fp:
    total = 0
    for line in fp:
        dont_splits = re.split(dont, line)

        muls = re.findall(mulr, dont_splits[0])
        for mul in muls: 
            a, b = mul[0], mul[1]
            total += int(a) * int(b)

        del dont_splits[0] 

        for i in range(len(dont_splits)):
            do_splits = re.split(do, dont_splits[i])
            print(do_splits)
            del do_splits[0]
            for j in range(len(do_splits)):
                muls = re.findall(mulr, do_splits[j])
                for mul in muls: 
                    a, b = mul[0], mul[1]
                    total += int(a) * int(b)

    print(total)



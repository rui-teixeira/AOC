m = []
file_name = '../test.txt'
file_name = '../input.txt'
for line in open(file_name):
    i_max = len(line.strip())
    m.append([int(c) for c in line.strip()])
j_max = len(m)


def iob(j, i):
    if j < 0 or i < 0:
        return False
    if j >= j_max or i >= i_max:
        return False
    return True

def climb(j,i):
    c = m[j][i]
    print(f"{c} - {(j,i)}")
    if c == 9:
        print("reached top")
        return 1
    score = 0
    if iob(j-1, i):
        if m[j-1][i]-1 ==  c:
            score += climb(j-1, i)
    if iob(j+1, i):
        if m[j+1][i]-1 == c:
            score += climb(j+1, i)
    if iob(j, i-1):
        if m[j][i-1]-1 == c:
            score += climb(j, i-1)
    if iob(j, i+1):
        if m[j][i+1]-1 == c:
            score += climb(j, i+1)
    return score
        
th = []
for j, line in enumerate(m):
    for i, d in enumerate(line):
        if d == 0:
            print("found start, climb!", j,i)
            th.append(climb(j, i))

print('th', th)
print('sum', sum(th))


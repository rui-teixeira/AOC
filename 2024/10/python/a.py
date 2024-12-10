m = []
i_max = 0
j_max = 0
file_name = '../test.txt'
file_name = '../input.txt'
for line in open(file_name):
    i_max = len(line.strip())
    m.append([int(c) for c in line.strip()])
j_max = len(m)

def iob(j, i):
    # print('j',j, 'j_max', j_max)
    # print('i',i, 'i_max', i_max)
    if j < 0 or i < 0:
        return False
    if j >= j_max or i >= i_max:
        return False
    return True

def climb(j,i, visited, tops):
    c = m[j][i]
    print(f"{c} - {(j,i)}")
    if (j, i) in visited:
        print("already visited", (j,i))
        return None
    else:
        visited.add((j,i))

    if c == 9:
        print("reached top")
        tops.add((j,i))
        return
    if iob(j-1, i):
        if m[j-1][i]-1 ==  c:
            climb(j-1, i, visited, tops)
    if iob(j+1, i):
        if m[j+1][i]-1 == c:
            climb(j+1, i, visited, tops)
    if iob(j, i-1):
        if m[j][i-1]-1 == c:
            climb(j, i-1, visited, tops)
    if iob(j, i+1):
        if m[j][i+1]-1 == c:
            climb(j, i+1, visited, tops)
        
th = []
for j, line in enumerate(m):
    for i, d in enumerate(line):
        if d == 0:
            print("found start, climb!", j,i)
            visited = set()
            tops = set()
            climb(j, i, visited, tops)
            th.append(len(tops))

print('th', th)
print('sum', sum(th))


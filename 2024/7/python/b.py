import math

def pipe(a,b):
    d = int(math.log10(b)) + 1
    return 10**d * a + b

def solve(arr,i,acc,op,target, last_i):
    if op == '+':
        new_acc = acc + arr[i]
    elif op == '*':
        new_acc = acc * arr[i]
    elif op == '|':
        new_acc = pipe(acc, arr[i])
    else:
        # just starting
        return solve(arr, i+1, arr[0], '+', target, last_i) or solve(arr, i+1, arr[0], '*', target, last_i) or solve(arr, i+1, arr[0], '|', target, last_i)

    if new_acc == target and i == last_i:
        return True
    if new_acc > target:
        return False
    if i == last_i:
        return False
    return solve(arr, i+1, new_acc, '+', target, last_i) or solve(arr, i+1, new_acc, '*', target, last_i) or solve(arr, i+1, new_acc, '|', target, last_i)

# with open("../input.txt") as fp:
with open("../input.txt") as fp:
# with open("../test.txt") as fp:
    total = 0
    for line in fp:
        [score, rest] = line.split(':')
        score = int(score)
        vals = [int(i) for i in rest.strip().split(' ')]
        print("solve",score, vals)
        total += score if solve(vals, 0, 0, 'start', score, len(vals)-1) else 0
    print(total)
        



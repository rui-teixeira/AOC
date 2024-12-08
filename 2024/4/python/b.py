

g = []
key = 'XMAS'
key_i = [1,2,3] # skip the 1st one
count = 0

def check_h(j,i):
    try:
        if (
                (g[j][i+1] == key[1]) and 
                (g[j][i+2] == key[2]) and 
                (g[j][i+3] == key[3])
                ):
            print("Found h")
            return True 
    except:
        return False

def check_h_r(j,i):
    if i < 3 :
        return False # Negative bounds check 
    try:
        if g[j][i-1] == key[1] and g[j][i-2] == key[2] and g[j][i-3] == key[3]:
           return True 
    except:
        return False

def check_v(j,i):
    try:
        if g[j+1][i] == key[1] and g[j+2][i] == key[2] and g[j+3][i] == key[3]: return True 
    except:
        return False

def check_v_r(j,i):
    if j < 3 :
        return False # Negative bounds check 
    try:
        if g[j-1][i] == key[1] and g[j-2][i] == key[2] and g[j-3][i] == key[3]: return True 
    except:
        return False
def check_x_1(j,i):
    try:
        if g[j+1][i+1] == key[1] and g[j+2][i+2] == key[2] and g[j+3][i+3] == key[3]: return True 
    except:
        return False
def check_x_2(j,i):
    if j < 3 :
        return False # Negative bounds check 
    try:
        if g[j-1][i+1] == key[1] and g[j-2][i+2] == key[2] and g[j-3][i+3] == key[3]: return True 
    except:
        return False
def check_x_3(j,i):
    if i < 3 :
        return False # Negative bounds check 
    try:
        if g[j+1][i-1] == key[1] and g[j+2][i-2] == key[2] and g[j+3][i-3] == key[3]: return True 
    except:
        return False
def check_x_4(j,i):
    if i < 3 or j < 3:
        return False # Negative bounds check 
    try:
        if g[j-1][i-1] == key[1] and g[j-2][i-2] == key[2] and g[j-3][i-3] == key[3]: return True 
    except:
        return False

# a.b
# .A.
# c.d
def check_corners(j, i, a, b, c, d):
    if i < 1 or j < 1:
        return False # Negative bounds check 
    try:
        if (
            g[j-1][i-1] == a and g[j-1][i+1] == b and 
            g[j+1][i-1] == c and g[j+1][i+1] == d 
                ): return True 
    except:
        return False

# with open("../example.txt") as fp:
with open("../input.txt") as fp:
    for line in fp:
        g.append(line)
    for j in range(len(g)):
        for i in range(len(line)):
            if g[j][i] == 'A':
                # M.M
                # .A.
                # S.S
                count += 1 if check_corners(j,i,'M','M','S','S') else 0
                # S.M
                # .A.
                # S.M
                count += 1 if check_corners(j,i,'S','M','S','M') else 0
                # S.S
                # .A.
                # M.M
                count += 1 if check_corners(j,i,'S','S','M','M') else 0
                # M.S
                # .A.
                # M.S
                count += 1 if check_corners(j,i,'M','S','M','S') else 0

    print(count)



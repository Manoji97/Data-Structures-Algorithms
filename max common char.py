s1 = 'aggtab'
s2 = 'gxtxayb'
d = {}
def fun(x,y):               #recursive implementation
    print(x,y)
    if len(x) <= 0 or len(y) <= 0:
        d[(x,y)] = 0
        return 0
    if (x,y) in d:
        return d[(x,y)]
    if x[-1] == y[-1]:
        a = fun(x[:-1],y[:-1])
        d[(x,y)] = a
        return 1 + a
    else:
        b = max(fun(x[:-1],y) , fun(x,y[:-1]))
        d[(x,y)] = b
        return b
    
fun(s1,s2)

import numpy as np       #dynamic programming
ss1 = len(s1)
ss2 = len(s2)

t = np.zeros((ss1+1,ss2+1))

for i in range(ss1+1):
    for j in range(ss2 +1):
        if i == 0 or j == 0:
            t[i,j] = 0
        else:
            if s1[i-1] == s2[j-1]:
                t[i,j] = 1 + t[i-1,j-1]
                
            else:
                t[i,j] = max(t[i-1,j],t[i,j-1])
print(t[ss1,ss2])

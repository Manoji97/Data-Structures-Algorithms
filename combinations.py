#  this function is for combinations of position
def fn(ls,a):
    ans = []
    for i in ls:
        for j in a:
            if i not in j:
                if sorted([i] + j) not in [sorted(f) for f in ans]:
                    ans.append([i] + j)
    return ans


# main list of combination of the input
def main_fn(l):
    ans = []
    ls = list(range(1,len(l)+1))
    a1 = [[i] for i in ls]
    for i in range(len(l)):
        for k in a1:
            ans.append([l[p-1] for p in k])
        a1 = fn(ls,a1)
    return ans 


l = [1,'a',3,4,5]

comb = main_fn(l)






























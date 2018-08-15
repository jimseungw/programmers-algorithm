import math
def solution(n,a,b):
    a, b = min(a,b), max(a,b)
    for k in range(1, int(math.log2(n)+1)):
        if a%2 != 0 and a+1 == b:
            return k
        else:
            n, a, b = n/2, math.ceil(a/2), math.ceil(b/2) ###

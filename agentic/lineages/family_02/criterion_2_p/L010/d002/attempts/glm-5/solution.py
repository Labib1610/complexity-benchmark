import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    N = 2 * n
    E = 2 * m
    
    # parse literals into node ids
    # node for literal v: 2|v|-1 if v>0 else 2|v|-2
    vals = data[2:2 + 2*m]
    # A[j], B[j] node ids
    # count degrees
    deg = [0] * N
    A = [0] * m
    B = [0] * m
    idx = 0
    for j in range(m):
        a = int(vals[idx]); b = int(vals[idx+1]); idx += 2
        if a > 0:
            na = a + a - 1
        else:
            na = -a - a - 2
        if b > 0:
            nb = b + b - 1
        else:
            nb = -b - b - 2
        A[j] = na; B[j] = nb
        deg[na ^ 1] += 1
        deg[nb ^ 1] += 1
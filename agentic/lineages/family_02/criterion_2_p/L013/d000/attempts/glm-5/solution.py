import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    N = 2 * n
    # literal encoding: for value l: idx = 2*(|l|-1) + (l<0)
    # edges: for clause (a,b): (neg(a) -> b), (neg(b) -> a)
    E = 2 * m
    eu = [0]*E
    ev = [0]*E
    pos = 2
    # We'll compute literal indices directly.
    # For clause (a, b): u = lit(-a), v = lit(b); and u2 = lit(-b), v2 = lit(a).
    # lit(x): if x>0: 2*(x-1); if x<0: 2*(-x-1)+1. neg(lit) = lit ^ 1.
    # So lit(-a) = lit(a) ^ 1.
    deg = [0]*(N+1)  # for CSR of G (out-edges)
    rdeg = [0]*(N+1) # for CSR of G^T
    for i in range(m):
        a = int(data[pos]); b = int(data[pos+1]); pos += 2
        # lit(a):
        if a > 0:
            la = 2*(a-1)
        else:
            la = 2*(-a-1)+1
        if b > 0:
            lb = 2*(b-1)
        else:
            lb = 2*(-b-1)+1
        # edges: (la^1 -> lb), (lb^1 -> la)
        u1 = la ^ 1; v1 = lb
        u2 = lb ^ 1; v2 = la
        j = 2*i
        eu[j] = u1; ev[j] = v1
        eu[j+1] = u2; ev[j+1] = v2
        deg[u1+1] += 1; deg[u2+1] += 1
        rdeg[v1+1] += 1; rdeg[v2+1] += 1
    ...
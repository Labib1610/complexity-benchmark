import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    idx = 2
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    for a in range(1, n + 1):
        la = adj[a]
        # candidates b > a that conflict with a
        # we want lexicographically smallest (a,b,c)
        for b in sorted(la):
            if b <= a:
                continue
            lb = adj[b]
            # find smallest c > b that is in both la and lb
            common = la & lb
            for c in sorted(common):
                if c > b:
                    print(a, b, c)
                    return

solve()
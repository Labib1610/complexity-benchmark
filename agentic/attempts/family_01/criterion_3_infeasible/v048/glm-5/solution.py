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
        u = int(data[idx]); v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
    
    # Find lexicographically smallest triangle
    for a in range(1, n + 1):
        la = adj[a]
        if len(la) < 2:
            continue
        # candidates b > a with b in la
        for b in la:
            if b <= a:
                continue
            lb = adj[b]
            # candidates c > b with c in la and c in lb
            # iterate over smaller set
            if len(la) <= len(lb):
                for c in la:
                    if c > b and c in lb:
                        print(a, b, c)
                        return
            else:
                for c in lb:
                    if c > b and c in la:
                        print(a, b, c)
                        return

solve()
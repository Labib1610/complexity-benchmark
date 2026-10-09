import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    if k == 1:
        print("YES")
        print(1)
        return
    
    # complement graph adjacency
    comp = [0] * n
    for i in range(n):
        comp[i] = ((1 << n) - 1) ^ (1 << i) ^ adj[i]
    
    # If k is large, search for independent set of size k in original graph.
    # Otherwise search for clique of size k in complement graph.
    if k > n // 2:
        target = k
        found = None
        
        def expand(R, P, size):
            nonlocal found
            if found is not None:
                return
            if size == target:
                found = R
                return
            if P == 0:
                return
            # bound: can we reach target?
            if size + bin(P).count('1') < target:
                return
            # pick pivot to reduce branching
            # simple: iterate vertices in P
            p = P
            while p:
                v = (p & -p).bit_length() - 1
                p &= p - 1
                if found is not None:
                    return
                expand(R | (1 << v), P & comp[v], size + 1)
                P &= ~(1 << v)
        
        expand(0, (1 << n) - 1, 0)
        if found is not None:
            verts = [i+1 for i in range(n) if found & (1 << i)]
            print("YES")
            print(' '.join(map(str, verts)))
        else:
            print("NO")
    else:
        target = k
        found = None
        
        def expand(R, P, size):
            nonlocal found
            if found is not None:
                return
            if size == target:
                found = R
                return
            if P == 0:
                return
            if size + bin(P).count('1') < target:
                return
            p = P
            while p:
                v = (p & -p).bit_length() - 1
                p &= p - 1
                if found is not None:
                    return
                expand(R | (1 << v), P & adj[v], size + 1)
                P &= ~(1 << v)
        
        expand(0, (1 << n) - 1, 0)
        if found is not None:
            verts = [i+1 for i in range(n) if found & (1 << i)]
            print("YES")
            print(' '.join(map(str, verts)))
        else:
            print("NO")

solve()
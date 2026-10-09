import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    full = (1 << n) - 1
    # Precompute independent sets via DP
    indep = [False] * (1 << n)
    indep[0] = True
    for mask in range(1, 1 << n):
        v = (mask & -mask).bit_length() - 1
        rest = mask ^ (1 << v)
        if indep[rest] and (adj[v] & rest) == 0:
            indep[mask] = True
    
    # Find all maximal independent sets
    maximal = []
    seen = [False] * (1 << n)
    for mask in range(1 << n):
        if indep[mask]:
            is_maximal = True
            for v in range(n):
                if not (mask & (1 << v)):
                    if (adj[v] & mask) == 0:
                        is_maximal = False
                        break
            if is_maximal:
                maximal.append(mask)
    
    # Check if three maximal independent sets cover all vertices
    L = len(maximal)
    for i in range(L):
        mi = maximal[i]
        for j in range(i, L):
            mj = maximal[j]
            if (mi & mj) == 0:
                complement = full & ~(mi | mj)
                if indep[complement]:
                    # Build assignment
                    assign = [0] * n
                    for v in range(n):
                        if mi & (1 << v):
                            assign[v] = 1
                        elif mj & (1 << v):
                            assign[v] = 2
                        else:
                            assign[v] = 3
                    print("YES")
                    print(' '.join(map(str, assign)))
                    return
    print("NO")

solve()
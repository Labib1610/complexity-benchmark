import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # complement adjacency: comp[i] = set of vertices non-adjacent to i (and i != j)
    comp = [0] * (n + 1)
    for i in range(1, n + 1):
        comp[i] = ((1 << (n + 1)) - 1) & ~adj[i] & ~1
    
    # memo: (R, k) -> clique or None
    memo = {}
    
    def find_clique(R, kk):
        if kk == 0:
            return 0
        if R == 0:
            return None
        if bin(R).count('1') < kk:
            return None
        key = (R, kk)
        if key in memo:
            return memo[key]
        
        # pick pivot: vertex in R with max degree into R
        best_p = -1
        best_deg = -1
        R_list = []
        r = R
        while r:
            b = r & -r
            v = b.bit_length() - 1
            R_list.append(v)
            r ^= b
        
        for v in R_list:
            d = bin(comp[v] & R).count('1')
            if d > best_deg:
                best_deg = d
                best_p = v
        
        # branch: include best_p, or exclude best_p
        # include best_p
        newR = R & comp[best_p]
        res = find_clique(newR, kk - 1)
        if res is not None:
            result = res | (1 << best_p)
            memo[key] = result
            return result
        
        # exclude best_p
        res = find_clique(R ^ (1 << best_p), kk)
        memo[key] = res
        return res
    
    R = 0
    for i in range(1, n + 1):
        R |= 1 << i
    
    result = find_clique(R, k)
    if result is None:
        print("NO")
    else:
        print("YES")
        vertices = []
        for i in range(1, n + 1):
            if result & (1 << i):
                vertices.append(str(i))
        print(' '.join(vertices))

solve()
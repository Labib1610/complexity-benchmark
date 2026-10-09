import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
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
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))
    
    # Greedy selection: pick vertex with minimum degree in remaining graph
    result = []
    available = (1 << n) - 1
    
    while available and len(result) < k:
        # Find vertex with minimum degree among available
        best_v = -1
        best_deg = n + 1
        av = available
        while av:
            v = (av & -av).bit_length()
            av &= av - 1
            deg = bin(adj[v] & available).count('1')
            if deg < best_deg:
                best_deg = deg
                best_v = v
        
        if best_v == -1:
            break
        
        result.append(best_v)
        # Remove best_v and its neighbors from available
        available &= ~adj[best_v]
        available &= ~(1 << (best_v - 1))
    
    if len(result) >= k:
        print("YES")
        print(' '.join(map(str, result[:k])))
        return
    
    # Backtracking search
    result = []
    found = False
    
    def backtrack(start, available_mask):
        nonlocal found, result
        if found:
            return
        need = k - len(result)
        if need == 0:
            found = True
            return
        # Count available vertices
        cnt = bin(available_mask).count('1')
        if cnt < need:
            return
        
        # Pruning: if remaining vertices can't satisfy need
        if cnt < need:
            return
        
        # Try vertices starting from 'start'
        for i in range(start, n + 1):
            if found:
                return
            bit = 1 << (i - 1)
            if available_mask & bit:
                result.append(i)
                new_available = available_mask & ~adj[i] & ~bit
                backtrack(i + 1, new_available)
                if found:
                    return
                result.pop()
    
    backtrack(1, (1 << n) - 1)
    
    if found:
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

solve()
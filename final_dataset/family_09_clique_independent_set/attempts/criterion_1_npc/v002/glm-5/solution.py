import sys
from itertools import combinations

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Greedy heuristic to find a large independent set
    def greedy_is():
        remaining = set(range(n))
        result = []
        while remaining:
            # Pick vertex with minimum degree in the remaining graph
            u = min(remaining, key=lambda x: len(adj[x] & remaining))
            result.append(u)
            remaining.discard(u)
            remaining -= adj[u]
        return result
    
    best = greedy_is()
    
    # If greedy already finds k, output it
    if len(best) >= k:
        print("YES")
        print(' '.join(str(x + 1) for x in best[:k]))
        return
    
    # Otherwise, use meet-in-the-middle for exact search
    # Split vertices into two halves
    mid = n // 2
    left = list(range(mid))
    right = list(range(mid, n))
    
    # Precompute compatibility within each half
    def get_compat(vertices):
        compat = {}
        for i, u in enumerate(vertices):
            mask = 0
            for j, v in enumerate(vertices):
                if v not in adj[u]:
                    mask |= (1 << j)
            compat[u] = mask
        return compat
    
    left_compat = get_compat(left)
    right_compat = get_compat(right)
    
    # Enumerate all independent sets in left half
    left_sets = []
    L = len(left)
    for mask in range(1 << L):
        ok = True
        for i in range(L):
            if mask & (1 << i):
                u = left[i]
                # Check if u conflicts with any other selected vertex
                if (mask & left_compat[u]) != mask:
                    ok = False
                    break
        if ok:
            left_sets.append(mask)
    
    # Enumerate all independent sets in right half
    right_sets = []
    R = len(right)
    for mask in range(1 << R):
        ok = True
        for i in range(R):
            if mask & (1 << i):
                u = right[i]
                if (mask & right_compat[u]) != mask:
                    ok = False
                    break
        if ok:
            right_sets.append(mask)
    
    # Precompute which left vertices are compatible with which right vertices
    cross_compat = [0] * n
    for i, u in enumerate(left):
        mask = 0
        for j, v in enumerate(right):
            if v not in adj[u]:
                mask |= (1 << j)
        cross_compat[u] = mask
    
    # Group left sets by size
    left_by_size = {}
    for mask in left_sets:
        sz = bin(mask).count('1')
        if sz not in left_by_size:
            left_by_size[sz] = []
        left_by_size[sz].append(mask)
    
    # Group right sets by size
    right_by_size = {}
    for mask in right_sets:
        sz = bin(mask).count('1')
        if sz not in right_by_size:
            right_by_size[sz] = []
        right_by_size[sz].append(mask)
    
    # Try to find a combination
    for ls in range(k + 1):
        rs = k - ls
        if ls not in left_by_size or rs not in right_by_size:
            continue
        for lm in left_by_size[ls]:
            # Compute which right vertices are compatible with this left set
            compat_mask = (1 << R) - 1
            for i in range(L):
                if lm & (1 << i):
                    u = left[i]
                    compat_mask &= cross_compat[u]
            for rm in right_by_size[rs]:
                if (rm & compat_mask) == rm:
                    # Found a valid combination
                    result = []
                    for i in range(L):
                        if lm & (1 << i):
                            result.append(left[i] + 1)
                    for i in range(R):
                        if rm & (1 << i):
                            result.append(right[i] + 1)
                    print("YES")
                    print(' '.join(map(str, result)))
                    return
    
    print("NO")

if __name__ == "__main__":
    solve()
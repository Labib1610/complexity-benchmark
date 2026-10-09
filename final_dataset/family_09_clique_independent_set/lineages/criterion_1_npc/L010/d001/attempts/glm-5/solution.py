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
    
    if k == 1:
        print("YES")
        print(1)
        return
    
    # Find a maximal independent set greedily
    chosen = []
    forbidden = 0
    for v in range(1, n + 1):
        if not (forbidden & (1 << v)):
            chosen.append(v)
            forbidden |= adj[v] | (1 << v)
            if len(chosen) == k:
                print("YES")
                print(' '.join(map(str, chosen)))
                return
    
    if len(chosen) >= k:
        print("YES")
        print(' '.join(map(str, chosen[:k])))
        return
    
    # Split into two halves for meet-in-the-middle
    half = n // 2
    left = list(range(1, half + 1))
    right = list(range(half + 1, n + 1))
    
    def get_independent_sets(vertices):
        results = []
        size = len(vertices)
        for mask in range(1 << size):
            ok = True
            for i in range(size):
                if mask & (1 << i):
                    vi = vertices[i]
                    for j in range(i + 1, size):
                        if mask & (1 << j):
                            vj = vertices[j]
                            if adj[vi] & (1 << vj):
                                ok = False
                                break
                    if not ok:
                        break
            if ok:
                results.append(mask)
        return results
    
    left_sets = get_independent_sets(left)
    right_sets = get_independent_sets(right)
    
    # Group right sets by size
    right_by_size = {}
    for rmask in right_sets:
        cnt = bin(rmask).count('1')
        right_by_size.setdefault(cnt, []).append(rmask)
    
    # Precompute cross-conflict masks
    left_cross = [0] * len(left_sets)
    for idx, lmask in enumerate(left_sets):
        cross = 0
        for i in range(len(left)):
            if lmask & (1 << i):
                cross |= adj[left[i]]
        left_cross[idx] = cross
    
    # Precompute right internal conflict masks
    right_internal = [0] * len(right_sets)
    for idx, rmask in enumerate(right_sets):
        internal = 0
        for j in range(len(right)):
            if rmask & (1 << j):
                internal |= (1 << right[j])
        right_internal[idx] = internal
    
    # Precompute right cross masks (conflicts from right to left)
    right_cross = [0] * len(right_sets)
    for idx, rmask in enumerate(right_sets):
        cross = 0
        for j in range(len(right)):
            if rmask & (1 << j):
                cross |= adj[right[j]]
        right_cross[idx] = cross
    
    # Precompute left internal masks
    left_internal = [0] * len(left_sets)
    for idx, lmask in enumerate(left_sets):
        internal = 0
        for i in range(len(left)):
            if lmask & (1 << i):
                internal |= (1 << left[i])
        left_internal[idx] = internal
    
    # Try all combinations
    for lidx, lmask in enumerate(left_sets):
        lsize = bin(lmask).count('1')
        if lsize > k:
            continue
        need = k - lsize
        if need in right_by_size:
            l_cross = left_cross[lidx]
            l_internal = left_internal[lidx]
            for ridx in right_by_size[need]:
                rmask = right_sets[ridx]
                r_cross = right_cross[ridx]
                r_internal = right_internal[ridx]
                # Check no cross conflicts
                if (l_cross & r_internal) or (r_cross & l_internal):
                    continue
                # Found valid pair
                result = []
                for i in range(len(left)):
                    if lmask & (1 << i):
                        result.append(left[i])
                for j in range(len(right)):
                    if rmask & (1 << j):
                        result.append(right[j])
                print("YES")
                print(' '.join(map(str, result)))
                return
    
    print("NO")

solve()
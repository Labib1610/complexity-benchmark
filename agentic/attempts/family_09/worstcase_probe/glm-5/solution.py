import sys

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
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
    
    # Greedy heuristic: try vertices in order of increasing degree
    order = list(range(1, n + 1))
    order.sort(key=lambda x: bin(adj[x]).count('1'))
    
    best = []
    for start in order:
        if len(best) == k:
            break
        current = []
        used_mask = 0
        for v in order:
            idx = v - 1
            bit = 1 << idx
            if (used_mask & adj[v]) == 0:
                current.append(v)
                used_mask |= bit
                if len(current) == k:
                    break
        if len(current) > len(best):
            best = current
            if len(best) == k:
                break
    
    if len(best) == k:
        print("YES")
        print(' '.join(map(str, best)))
        return
    
    # Meet-in-the-middle approach
    half = n // 2
    left_size = half
    right_size = n - half
    
    # Precompute adjacency masks for each half
    left_adj = [0] * left_size
    for i in range(left_size):
        v = i + 1
        mask = 0
        for j in range(left_size):
            if adj[v] & (1 << j):
                mask |= 1 << j
        left_adj[i] = mask
    
    right_adj = [0] * right_size
    for i in range(right_size):
        v = half + i + 1
        mask = 0
        for j in range(right_size):
            if adj[v] & (1 << (half + j)):
                mask |= 1 << j
        right_adj[i] = mask
    
    # Cross edges: for each left vertex, which right vertices are forbidden
    cross = [0] * left_size
    for i in range(left_size):
        v = i + 1
        mask = 0
        for j in range(right_size):
            if adj[v] & (1 << (half + j)):
                mask |= 1 << j
        cross[i] = mask
    
    # Enumerate all independent sets in left half
    left_sets = [[] for _ in range(left_size + 1)]
    left_sets[0].append((0, 0))
    
    for i in range(1, left_size + 1):
        bit = 1 << (i - 1)
        prev_sets = left_sets[i - 1]
        curr_sets = []
        for mask, sz in prev_sets:
            curr_sets.append((mask, sz))
        for mask, sz in prev_sets:
            if (mask & left_adj[i - 1]) == 0:
                new_mask = mask | bit
                curr_sets.append((new_mask, sz + 1))
        # Prune: keep only best size for each mask
        best_for_mask = {}
        for mask, sz in curr_sets:
            if mask not in best_for_mask or sz > best_for_mask[mask]:
                best_for_mask[mask] = sz
        left_sets[i] = [(mask, sz) for mask, sz in best_for_mask.items()]
    
    # Collect all left independent sets
    all_left = {}
    for mask, sz in left_sets[left_size]:
        if sz not in all_left:
            all_left[sz] = []
        all_left[sz].append(mask)
    
    # Enumerate all independent sets in right half
    right_sets = [[] for _ in range(right_size + 1)]
    right_sets[0].append((0, 0))
    
    for i in range(1, right_size + 1):
        bit = 1 << (i - 1)
        prev_sets = right_sets[i - 1]
        curr_sets = []
        for mask, sz in prev_sets:
            curr_sets.append((mask, sz))
        for mask, sz in prev_sets:
            if (mask & right_adj[i - 1]) == 0:
                new_mask = mask | bit
                curr_sets.append((new_mask, sz + 1))
        best_for_mask = {}
        for mask, sz in curr_sets:
            if mask not in best_for_mask or sz > best_for_mask[mask]:
                best_for_mask[mask] = sz
        right_sets[i] = [(mask, sz) for mask, sz in best_for_mask.items()]
    
    # For each right mask, compute forbidden left vertices
    right_forbidden = {}
    for mask, sz in right_sets[right_size]:
        forbidden = 0
        for i in range(right_size):
            if mask & (1 << i):
                forbidden |= cross[i]
        right_forbidden[mask] = (sz, forbidden)
    
    # Try to find combination
    for left_sz in range(min(k, left_size), -1, -1):
        right_sz = k - left_sz
        if right_sz < 0 or right_sz > right_size:
            continue
        if left_sz not in all_left:
            continue
        
        for left_mask in all_left[left_sz]:
            for right_mask, (rsz, forbidden) in right_forbidden.items():
                if rsz != right_sz:
                    continue
                if (left_mask & forbidden) == 0:
                    # Found solution
                    result = []
                    for i in range(left_size):
                        if left_mask & (1 << i):
                            result.append(i + 1)
                    for i in range(right_size):
                        if right_mask & (1 << i):
                            result.append(half + i + 1)
                    print("YES")
                    print(' '.join(map(str, result)))
                    return
    
    print("NO")

if __name__ == "__main__":
    solve()
import sys

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
    
    # Greedy approach: repeatedly pick vertex with maximum degree in remaining graph
    # This is a standard heuristic for finding large independent sets
    remaining = set(range(n))
    result = []
    
    while remaining and len(result) < k:
        # Find vertex with maximum degree in remaining graph
        best_v = -1
        best_deg = -1
        for v in remaining:
            deg = len(adj[v] & remaining)
            if deg > best_deg:
                best_deg = deg
                best_v = v
        
        # Add best_v to independent set
        result.append(best_v)
        remaining.discard(best_v)
        
        # Remove best_v and all its neighbors from remaining
        neighbors = adj[best_v] & remaining
        remaining -= neighbors
    
    if len(result) >= k:
        print("YES")
        print(' '.join(str(x + 1) for x in result[:k]))
        return
    
    # If greedy didn't find enough, try meet-in-the-middle
    half = n // 2
    
    # Generate all independent sets for first half
    left_sets = []
    for mask in range(1 << half):
        valid = True
        for i in range(half):
            if mask & (1 << i):
                for j in range(i + 1, half):
                    if mask & (1 << j):
                        if j in adj[i]:
                            valid = False
                            break
                if not valid:
                    break
        if valid:
            left_sets.append((mask, bin(mask).count('1')))
    
    # Generate all independent sets for second half
    right_sets = []
    for mask in range(1 << (n - half)):
        valid = True
        for i in range(n - half):
            if mask & (1 << i):
                for j in range(i + 1, n - half):
                    if mask & (1 << j):
                        if (half + j) in adj[half + i]:
                            valid = False
                            break
                if not valid:
                    break
        if valid:
            right_sets.append((mask, bin(mask).count('1')))
    
    # Group right sets by size
    right_by_size = {}
    for mask, size in right_sets:
        if size not in right_by_size:
            right_by_size[size] = []
        right_by_size[size].append(mask)
    
    # For each left set, find compatible right set
    for left_mask, left_size in left_sets:
        need = k - left_size
        if need < 0:
            continue
        if need not in right_by_size:
            continue
        
        # Build forbidden mask for right side
        forbidden = 0
        for i in range(half):
            if left_mask & (1 << i):
                for j in range(n - half):
                    if (half + j) in adj[i]:
                        forbidden |= (1 << j)
        
        for right_mask in right_by_size[need]:
            if (right_mask & forbidden) == 0:
                # Found valid combination
                result = []
                for i in range(half):
                    if left_mask & (1 << i):
                        result.append(i + 1)
                for i in range(n - half):
                    if right_mask & (1 << i):
                        result.append(half + i + 1)
                print("YES")
                print(' '.join(map(str, result)))
                return
    
    print("NO")

if __name__ == "__main__":
    solve()
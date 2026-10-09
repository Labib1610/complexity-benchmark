import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    
    # color: 0 = unassigned, 1/2/3 = periods
    color = [0] * (n + 1)
    
    # Precompute list of nodes for convenience
    nodes = list(range(1, n + 1))
    
    # We'll use a recursive backtracking with bitset pruning.
    # For efficiency, order nodes by degree descending.
    nodes.sort(key=lambda x: bin(adj[x]).count('1'), reverse=True)
    
    # forbidden[i] = bitmask of colors (1<<1, 1<<2, 1<<3) forbidden for node i
    # We'll track dynamically.
    
    # Precompute neighbors as list
    neighbors = [ [] for _ in range(n+1) ]
    for i in range(1, n+1):
        nb = adj[i]
        while nb:
            b = nb & -nb
            j = b.bit_length() - 1
            neighbors[i].append(j)
            nb ^= b
    
    # Use iterative or recursive DFS with pruning.
    # Since n <= 40, 3^40 is too large, but graph coloring with 3 colors
    # can be solved with backtracking + pruning for n=40 in practice if graph is not too dense.
    # However worst case could be hard. Let's implement a smarter approach:
    # Use the fact that 3-coloring can be reduced: pick a node, try 3 colors.
    # Use forward checking: maintain available colors for each unassigned node.
    
    # available[i] = bitmask of available colors (bits 1,2,3)
    available = [0b1110] * (n + 1)  # bits 1,2,3 set (bit 0 unused)
    
    # We'll assign nodes in order of most constrained.
    # Use recursion with forward checking.
    
    assigned = [0] * (n + 1)
    
    # Count of unassigned neighbors for each node (dynamic)
    # Not strictly needed; we'll use available masks.
    
    # Precompute static degree
    degree = [bin(adj[i]).count('1') for i in range(n+1)]
    
    # For choosing next node, pick unassigned node with fewest available colors,
    # tie-break by highest degree.
    
    # We'll implement recursive function.
    # To speed up, use arrays and avoid function call overhead by using stack.
    
    # Let's implement recursive with sys.setrecursionlimit
    sys.setrecursionlimit(10000)
    
    # We need to restore state on backtrack.
    # We'll record changes to available masks.
    
    # Let's implement a simple recursive backtracking with forward checking.
    
    unassigned = set(range(1, n+1))
    
    # For performance, represent unassigned as a bitmask too.
    unassigned_mask = (1 << (n+1)) - 2  # bits 1..n set
    
    # Precompute bit positions
    # We'll iterate over set bits of unassigned_mask.
    
    def popcount(x):
        return bin(x).count('1')
    
    # Precompute bit lengths
    # We'll use x.bit_length()
    
    # Let's define recursive function
    def dfs(count):
        if count == n:
            return True
        # Choose unassigned node with fewest available colors
        best = -1
        best_avail = 4
        best_deg = -1
        um = unassigned_mask
        while um:
            b = um & -um
            i = b.bit_length() - 1
            um ^= b
            av = available[i]
            cnt = 0
            if av & 2: cnt += 1
            if av & 4: cnt += 1
            if av & 8: cnt += 1
            if cnt == 0:
                return False
            if cnt < best_avail or (cnt == best_avail and degree[i] > best_deg):
                best_avail = cnt
                best = i
                best_deg = degree[i]
                if cnt == 1:
                    break
        
        i = best
        av = available[i]
        # Try each color
        for c in (1, 2, 3):
            bit = 1 << c
            if not (av & bit):
                continue
            # Assign color c to i
            assigned[i] = c
            unassigned_mask ^= (1 << i)
            # Record changes to available
            changes = []
            ok = True
            for j in neighbors[i]:
                if assigned[j] == 0 and (available[j] & bit):
                    available[j] &= ~bit
                    changes.append(j)
                    if available[j] == 0:
                        ok = False
                        break
            if ok:
                if dfs(count + 1):
                    return True
            # Undo
            for j in changes:
                available[j] |= bit
            assigned[i] = 0
            unassigned_mask |= (1 << i)
        return False
    
    if dfs(0):
        out = ['YES']
        out.append(' '.join(str(assigned[i]) for i in range(1, n+1)))
        sys.stdout.write('\n'.join(out))
    else:
        sys.stdout.write('NO')

solve()
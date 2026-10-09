import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Precompute valid pairs
    # Interaction value: 2*(d^4) - 10*(d^2) + 4
    # We need sum = -4m, so each edge must contribute -4.
    # Valid pairs (f_u, f_v) such that value is -4.
    valid_pairs = set()
    for i in range(1, 4):
        for j in range(1, 4):
            d = i - j
            val = 2 * (d**4) - 10 * (d**2) + 4
            if val == -4:
                valid_pairs.add((i, j))
    
    # Determine allowed values for each node
    # Initially all values {1, 2, 3} are possible
    allowed = [set([1, 2, 3]) for _ in range(n)]
    
    # AC-3 algorithm for arc consistency
    queue = []
    for u in range(n):
        for v in adj[u]:
            queue.append((u, v))
    
    possible = True
    while queue and possible:
        u, v = queue.pop(0)
        # Revise: remove values from allowed[u] that have no support in allowed[v]
        to_remove = set()
        for x in allowed[u]:
            has_support = False
            for y in allowed[v]:
                if (x, y) in valid_pairs:
                    has_support = True
                    break
            if not has_support:
                to_remove.add(x)
        
        if to_remove:
            allowed[u] -= to_remove
            if not allowed[u]:
                possible = False
                break
            # Propagate constraints to neighbors
            for w in adj[u]:
                if w != v:
                    queue.append((w, u))
    
    if not possible:
        print("NO")
        return
    
    # Check if any node has empty domain
    for u in range(n):
        if not allowed[u]:
            print("NO")
            return
    
    # Backtracking search with lexicographically smallest preference
    assignment = [0] * n
    
    # Precompute neighbors for efficiency
    neighbors = adj
    
    def backtrack(idx):
        if idx == n:
            return True
        
        u = idx
        # Try values in ascending order for lexicographically smallest solution
        for val in sorted(allowed[u]):
            # Check consistency with already assigned neighbors
            consistent = True
            for v in neighbors[u]:
                if v < u:  # neighbor already assigned
                    if (val, assignment[v]) not in valid_pairs:
                        consistent = False
                        break
            
            if consistent:
                assignment[u] = val
                if backtrack(idx + 1):
                    return True
                assignment[u] = 0
        
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
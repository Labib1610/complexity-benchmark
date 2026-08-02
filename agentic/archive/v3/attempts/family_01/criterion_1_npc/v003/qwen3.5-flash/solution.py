import sys

# Increase recursion depth to handle N=40 comfortably
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Precompute neighbors_less and neighbors_greater to optimize the DFS
    # neighbors_less[u]: neighbors v such that v < u
    # neighbors_greater[u]: neighbors v such that v > u
    neighbors_less = [[] for _ in range(n + 1)]
    neighbors_greater = [[] for _ in range(n + 1)]
    
    for u in range(1, n + 1):
        for v in adj[u]:
            if v < u:
                neighbors_less[u].append(v)
            else:
                neighbors_greater[u].append(v)
    
    # colors[i] stores the assigned color for person i (0 if unassigned)
    colors = [0] * (n + 1)
    # domains[i] stores a bitmask of available colors for person i
    # 1 (bit 0) -> color 1, 2 (bit 1) -> color 2, 4 (bit 2) -> color 3
    # Initially all colors are available for all unassigned nodes
    domains = [7] * (n + 1) 
    
    def dfs(u):
        # Base case: all personnel assigned
        if u > n:
            return True
        
        # Try assigning colors 1, 2, 3 in order to ensure lexicographically smallest solution
        for c in range(1, 4):
            # Check conflict with already assigned neighbors (v < u)
            conflict = False
            for v in neighbors_less[u]:
                if colors[v] == c:
                    conflict = True
                    break
            if conflict:
                continue
            
            # Forward checking: update domains of unassigned neighbors (v > u)
            # We need to record changes to restore them if this path fails
            changed = []
            possible = True
            mask_c = 1 << (c - 1)
            
            for v in neighbors_greater[u]:
                # If color c was not available for v, assigning c to u doesn't affect v's domain
                # But we still need to check if v has any colors left.
                # However, domains[v] is guaranteed to be non-zero before this step due to invariant.
                # We only remove c if it was available.
                if (domains[v] & mask_c):
                    domains[v] &= ~mask_c
                    changed.append(v)
                    # If v has no colors left, this assignment leads to a dead end
                    if domains[v] == 0:
                        possible = False
                        break
            
            if possible:
                colors[u] = c
                if dfs(u + 1):
                    return True
                colors[u] = 0
            
            # Restore domains for unassigned neighbors
            for v in changed:
                domains[v] |= mask_c
                
        return False

    if dfs(1):
        print("YES")
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()
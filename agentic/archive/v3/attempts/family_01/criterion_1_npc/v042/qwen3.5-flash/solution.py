import sys

# Increase recursion depth to accommodate deep recursion trees if necessary
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break

    # Precompute neighbors < u and > u to optimize DFS
    # adj_lt[u] stores neighbors v where v < u
    # adj_gt[u] stores neighbors v where v > u
    adj_lt = [[] for _ in range(n + 1)]
    adj_gt = [[] for _ in range(n + 1)]
    
    for u in range(1, n + 1):
        for v in adj[u]:
            if v < u:
                adj_lt[u].append(v)
            else:
                adj_gt[u].append(v)

    # colors[i] stores the vault assigned to artifact i (0 if unassigned)
    # 1, 2, 3 are valid vault numbers
    colors = [0] * (n + 1)
    
    # available[i] is a bitmask of available colors for artifact i
    # 1 -> bit 0 (val 1), 2 -> bit 1 (val 2), 3 -> bit 2 (val 4)
    # Initially all 1, 2, 3 available -> mask 7
    available = [7] * (n + 1)
    
    # DFS function to find lexicographically smallest assignment
    def dfs(u):
        # Base case: all artifacts assigned
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to ensure lexicographically smallest sequence
        for c in range(1, 4):
            # 1. Check compatibility with already assigned neighbors (v < u)
            conflict = False
            for v in adj_lt[u]:
                if colors[v] == c:
                    conflict = True
                    break
            if conflict:
                continue
            
            # 2. Check consistency with future neighbors (v > u) - Forward Checking
            # We check if assigning c to u would leave any neighbor v > u with no valid colors
            future_conflict = False
            for v in adj_gt[u]:
                # If c is the only remaining color for v, assigning c to u will make v uncolorable
                # available[v] == (1 << (c - 1)) checks if exactly color c is available
                if available[v] == (1 << (c - 1)):
                    future_conflict = True
                    break
            
            if future_conflict:
                continue
            
            # If valid, proceed with assignment
            # Update available colors for future neighbors
            for v in adj_gt[u]:
                available[v] &= ~(1 << (c - 1))
            
            colors[u] = c
            
            if dfs(u + 1):
                return True
            
            # Backtrack
            colors[u] = 0
            for v in adj_gt[u]:
                available[v] |= (1 << (c - 1))
        
        return False

    if dfs(1):
        print("YES")
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()
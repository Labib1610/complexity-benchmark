import sys

# Increase recursion depth to handle N=40 safely
sys.setrecursionlimit(2000)

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

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Remove duplicate edges if any for efficiency
    for i in range(1, n + 1):
        adj[i] = list(set(adj[i]))

    colors = [0] * (n + 1)
    domains = [0] * (n + 1)
    history = []  # Stack to track domain changes for backtracking
    
    # Find connected components
    visited = [False] * (n + 1)
    components = []
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            comp.sort()
            components.append(comp)

    # Solve each component independently
    # Since components are disjoint, we can solve them one by one.
    # The lexicographical requirement is satisfied by solving nodes in index order.
    for comp in components:
        # Initialize domains for the nodes in this component
        for u in comp:
            domains[u] = 7  # 111 in binary, representing {1, 2, 3} available
        
        # DFS function to find the lexicographically smallest coloring
        def dfs(idx):
            if idx == len(comp):
                return True
            
            u = comp[idx]
            
            # Try colors 1, 2, 3 in increasing order to ensure lexicographical smallest
            for c in range(1, 4):
                # Check consistency with already assigned neighbors
                valid = True
                for v in adj[u]:
                    if colors[v] != 0 and colors[v] == c:
                        valid = False
                        break
                
                if not valid:
                    continue
                
                # Forward Checking: Update domains of unassigned neighbors
                changes_start = len(history)
                possible = True
                
                for v in adj[u]:
                    if colors[v] == 0:  # Unassigned neighbor
                        old_mask = domains[v]
                        domains[v] &= ~(1 << (c - 1))
                        if domains[v] == 0:
                            possible = False
                            # Don't break immediately to ensure we capture the state,
                            # but logically we can stop checking neighbors.
                            # However, we must ensure we don't add more to history if we fail.
                            # But we added to history before check.
                            # So we need to restore history if we break.
                            # We'll handle restoration after the loop.
                            break
                        history.append((v, old_mask))
                
                if possible:
                    colors[u] = c
                    if dfs(idx + 1):
                        # Solution found for this component.
                        # We need to clear history because it contains changes from this path.
                        # We don't need to restore domains because we are done with this component
                        # and will reset domains for the next component (or just leave them).
                        # But history must be empty for the next component's DFS to work correctly.
                        while history:
                            history.pop()
                        return True
                    
                    # Backtrack: Reset color
                    colors[u] = 0
                
                # Restore domains if this branch failed or was pruned
                while len(history) > changes_start:
                    v, old = history.pop()
                    domains[v] = old
            
            return False

        if not dfs(0):
            print("NO")
            return

    # Output result
    print("YES")
    print(*(colors[1:]))

if __name__ == '__main__':
    solve()
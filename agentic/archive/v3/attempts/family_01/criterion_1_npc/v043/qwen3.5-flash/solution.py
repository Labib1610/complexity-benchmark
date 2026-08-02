import sys

# Increase recursion depth to handle deep recursion for N=40
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

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
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
    
    ans = [0] * (n + 1)
    
    # Process each component independently
    # Since components are disjoint, we can solve them independently to find
    # the lexicographically smallest assignment for each component.
    # The global lexicographically smallest sequence is formed by combining
    # the optimal assignments for each component.
    for comp in components:
        # Initialize domains for nodes in this component
        # domains[i] is a bitmask of allowed colors (1, 2, 4)
        # We use size n + 1 for simplicity
        domains = [7] * (n + 1)
        
        # Precompute positions in the component for quick lookup
        # This helps to determine if a neighbor is unassigned
        pos = {u: i for i, u in enumerate(comp)}
        
        # Recursive DFS with forward checking
        def dfs(idx):
            if idx == len(comp):
                return True
            
            u = comp[idx]
            
            # Try colors 1, 2, 3 in order for lexicographically smallest
            for c in (1, 2, 3):
                # Check if color c is allowed for u based on already assigned neighbors
                # domains[u] has been updated by neighbors with pos < idx
                if domains[u] & (1 << (c - 1)):
                    # Valid color choice
                    changes = []
                    conflict = False
                    
                    # Propagate constraints to unassigned neighbors
                    for v in adj[u]:
                        # v is in the same component, check if unassigned
                        # Since adj[u] only contains neighbors in the component
                        if pos[v] > idx:
                            old = domains[v]
                            new = old & ~(1 << (c - 1))
                            domains[v] = new
                            changes.append((v, old))
                            if new == 0:
                                conflict = True
                                break
                    
                    if not conflict:
                        ans[u] = c
                        if dfs(idx + 1):
                            return True
                    
                    # Backtrack: restore domains
                    for v, old in changes:
                        domains[v] = old
            
            return False

        if not dfs(0):
            print("NO")
            return
            
    print("YES")
    print(*(ans[1:]))

if __name__ == '__main__':
    solve()
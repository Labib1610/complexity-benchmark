import sys

# Increase recursion depth to handle deep recursion if necessary
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

    visited = [False] * (n + 1)
    components = []
    
    # Identify connected components
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            q = [i]
            visited[i] = True
            comp.append(i)
            idx = 0
            while idx < len(q):
                u = q[idx]
                idx += 1
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
                        comp.append(v)
            # Sort vertices in the component to process them in lexicographical order of indices
            comp.sort()
            components.append(comp)

    ans = [0] * (n + 1)
    
    # Process each component independently
    for comp in components:
        k = len(comp)
        # Map vertex index to position in the component list
        local_pos = {v: i for i, v in enumerate(comp)}
        
        # Build local adjacency list using indices within the component
        local_adj = [[] for _ in range(k)]
        for i, u in enumerate(comp):
            for v in adj[u]:
                if v in local_pos:
                    local_adj[i].append(local_pos[v])
        
        comp_colors = [0] * k
        forbidden = [0] * k
        
        # Depth First Search with Forward Checking
        def dfs(idx):
            if idx == k:
                return True
            
            # If all 3 colors are forbidden for the current vertex, this path is invalid
            if forbidden[idx] == 7:
                return False

            # Try colors 0, 1, 2 (corresponding to shifts 1, 2, 3)
            for c in range(3):
                # Check if color c is allowed
                if not ((forbidden[idx] >> c) & 1):
                    comp_colors[idx] = c
                    
                    changes = []
                    possible = True
                    
                    # Forward checking: update forbidden colors for unassigned neighbors
                    for v_idx in local_adj[idx]:
                        if v_idx > idx:
                            old_mask = forbidden[v_idx]
                            new_mask = old_mask | (1 << c)
                            forbidden[v_idx] = new_mask
                            changes.append((v_idx, old_mask))
                            # If a neighbor becomes impossible to color, prune this branch
                            if new_mask == 7:
                                possible = False
                                break
                    
                    if possible:
                        if dfs(idx + 1):
                            return True
                    
                    # Backtrack: restore forbidden colors
                    for v_idx, old_mask in changes:
                        forbidden[v_idx] = old_mask
                    
                    comp_colors[idx] = 0
            
            return False

        if not dfs(0):
            print("NO")
            return
        
        # Store the result for the component
        for i, v in enumerate(comp):
            ans[v] = comp_colors[i] + 1
            
    print("YES")
    print(*(ans[1:]))

if __name__ == '__main__':
    solve()
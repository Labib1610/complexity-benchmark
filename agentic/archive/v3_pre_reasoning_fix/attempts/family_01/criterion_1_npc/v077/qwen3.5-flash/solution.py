import sys

# Increase recursion depth to accommodate N=40 safely
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
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
    
    # Find connected components
    # This allows us to solve the problem for smaller subgraphs independently.
    # Since the graph is defined by incompatibilities, constraints only exist within components.
    # To find the lexicographically smallest global assignment (s_1, ..., s_n),
    # we can find the lexicographically smallest assignment for each component's nodes
    # (sorted by ID) and combine them.
    
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
            components.append(comp)
    
    # Global assignment array
    assignment = [0] * (n + 1)
    
    # Process each component
    for comp in components:
        # Sort nodes in the component to ensure we assign shifts in increasing order of ID.
        # This is crucial for finding the lexicographically smallest assignment for the component.
        comp.sort()
        k = len(comp)
        
        # Map node ID to index 0..k-1 for local processing
        node_to_idx = {node: i for i, node in enumerate(comp)}
        
        # Build local adjacency list for the subgraph
        sub_adj = [[] for _ in range(k)]
        for u in comp:
            u_idx = node_to_idx[u]
            for v in adj[u]:
                # Since we are in a component, all neighbors must be in the component
                if v in node_to_idx:
                    v_idx = node_to_idx[v]
                    sub_adj[u_idx].append(v_idx)
        
        # Backtracking solver
        # We want to find the lexicographically smallest assignment for this component.
        # We try colors 1, 2, 3 for each node in order.
        
        comp_assignment = [0] * k
        forbidden = [0] * k  # bitmasks for forbidden colors (1<<0, 1<<1, 1<<2 for colors 1, 2, 3)
        
        def backtrack(idx):
            if idx == k:
                return True
            
            # Check available colors for current node (idx)
            # forbidden[idx] contains bits for colors forbidden by already assigned neighbors
            f = forbidden[idx]
            
            # Try colors 1, 2, 3 in order to ensure lexicographically smallest
            for c in range(1, 4):
                # Check if color c is allowed (bit is 0)
                if not ((f >> (c - 1)) & 1):
                    comp_assignment[idx] = c
                    
                    # Update constraints for neighbors
                    # We only update neighbors with index > idx (unassigned neighbors)
                    # Neighbors < idx are already assigned and their constraints are satisfied.
                    changes = []
                    possible = True
                    
                    for v_idx in sub_adj[idx]:
                        if v_idx > idx:
                            old_val = forbidden[v_idx]
                            forbidden[v_idx] |= (1 << (c - 1))
                            # If all 3 colors are forbidden for a neighbor, this path is invalid
                            if forbidden[v_idx] == 7:
                                possible = False
                                break
                            changes.append((v_idx, old_val))
                    
                    if possible:
                        if backtrack(idx + 1):
                            return True
                    
                    # Backtrack: restore forbidden values
                    for v_idx, old_val in changes:
                        forbidden[v_idx] = old_val
            
            return False
        
        if backtrack(0):
            # Fill the global assignment array
            for i in range(k):
                assignment[comp[i]] = comp_assignment[i]
        else:
            print("NO")
            return
    
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()
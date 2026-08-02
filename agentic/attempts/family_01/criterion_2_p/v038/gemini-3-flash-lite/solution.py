import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(500000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
        
    color = [0] * (n + 1)
    
    # To get the lexicographically smallest sequence, we iterate 1 to n.
    # If a node is uncolored, we try assigning it 1.
    # This is a standard 2-coloring (bipartite check) problem.
    # The requirement for lexicographically smallest means we prefer 1 over 2
    # whenever we have a choice in a new connected component.
    
    res = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS/DFS for this component
            stack = [(i, 1)]
            color[i] = 1
            component = []
            
            # Using iterative DFS to collect component and check bipartiteness
            dfs_stack = [i]
            component = [i]
            color[i] = 1
            
            idx_comp = 0
            while idx_comp < len(component):
                u = component[idx_comp]
                idx_comp += 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        component.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
            
            # We have a valid 2-coloring. Now ensure lexicographical smallest.
            # Within each component, the relative coloring is fixed.
            # If we have a choice for the root, we pick the one that makes
            # the smallest index in the component have the smallest value.
            # Actually, simply picking color[root] = 1 is always optimal
            # because 1 < 2.
            pass
            
    print("YES")
    print(*(color[i] for i in range(1, n + 1)))

solve()
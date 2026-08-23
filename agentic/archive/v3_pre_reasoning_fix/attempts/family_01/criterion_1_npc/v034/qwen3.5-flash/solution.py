import sys

# Increase recursion depth to handle deep recursion trees
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
            # Sort component to ensure we process vertices in increasing index order
            # This is crucial for the lexicographical requirement
            comp.sort()
            components.append(comp)

    colors = [0] * (n + 1)
    available = [0] * (n + 1) # bitmasks: 1, 2, 3 -> bits 0, 1, 2
    
    # Helper for bipartite check
    def is_bipartite(comp):
        # Check if the subgraph induced by comp is bipartite
        # Since comp is connected, one BFS/DFS is enough
        colors_map = {}
        stack = [comp[0]]
        colors_map[comp[0]] = 1
        
        while stack:
            u = stack.pop()
            c = colors_map[u]
            next_c = 3 - c # 1 -> 2, 2 -> 1
            
            for v in adj[u]:
                if v not in colors_map:
                    colors_map[v] = next_c
                    stack.append(v)
                else:
                    if colors_map[v] == c:
                        return False
        return True

    comp_allowed = []
    for comp in components:
        if is_bipartite(comp):
            comp_allowed.append([1, 2])
        else:
            comp_allowed.append([1, 2, 3])
            
    # Define DFS function
    def dfs(comp, allowed_colors, idx):
        if idx == len(comp):
            return True
        
        u = comp[idx]
        
        for c in allowed_colors:
            # Check conflict with assigned neighbors
            conflict = False
            for v in adj[u]:
                if colors[v] == c:
                    conflict = True
                    break
            
            if conflict:
                continue
            
            # Forward check
            modified = []
            possible = True
            
            for v in adj[u]:
                if colors[v] == 0:
                    mask = 1 << (c - 1)
                    # Only update if the color was available
                    if available[v] & mask:
                        available[v] &= ~mask
                        modified.append(v)
                    
                    # Check if available[v] became 0
                    if available[v] == 0:
                        possible = False
                        break
            
            if not possible:
                # Backtrack available
                for v in modified:
                    available[v] |= (1 << (c - 1))
                continue
            
            # Assign
            colors[u] = c
            
            if dfs(comp, allowed_colors, idx + 1):
                return True
            
            # Backtrack
            colors[u] = 0
            for v in modified:
                available[v] |= (1 << (c - 1))
        
        return False

    for i, comp in enumerate(components):
        # Initialize available for this component
        for v in comp:
            available[v] = 7
        
        if not dfs(comp, comp_allowed[i], 0):
            print("NO")
            return

    print("YES")
    # Output colors
    print(" ".join(map(str, colors[1:])))

if __name__ == '__main__':
    solve()
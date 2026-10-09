def solve():
    import sys
    from collections import defaultdict, deque
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    graph = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    # Try to 3-color the graph
    color = [-1] * n  # -1 means uncolored, 0,1,2 are the three colors
    
    # Check if graph is 3-colorable
    def is_safe(node, c):
        for neighbor in graph[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def dfs(node):
        for c in [0, 1, 2]:
            if is_safe(node, c):
                color[node] = c
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        if not dfs(neighbor):
                            color[node] = -1
                            return False
                return True
        return False
    
    # Try coloring all components
    for i in range(n):
        if color[i] == -1:
            # Try to start coloring with color 0
            color[i] = 0
            for neighbor in graph[i]:
                if color[neighbor] == -1:
                    if not dfs(neighbor):
                        print("NO")
                        return
            # Check if current component is valid
            # We need to verify no two adjacent nodes have same color
            for u, v in edges:
                if color[u] == color[v]:
                    print("NO")
                    return
    
    # Verify the coloring is valid
    for u, v in edges:
        if color[u] == color[v]:
            print("NO")
            return
            
    print("YES")
    print(" ".join(str(c+1) for c in color))

solve()
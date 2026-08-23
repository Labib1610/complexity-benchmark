def solve():
    import sys
    from collections import defaultdict, deque
    
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Color the graph with 3 colors using backtracking (DFS)
    # 0: unassigned, 1,2,3: assigned colors
    color = [0] * (n+1)
    
    # Check if we can color node with c without conflict
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    # DFS with backtracking to find lexicographically smallest valid coloring
    def dfs(node):
        if node > n:
            return True
            
        for c in range(1, 4):
            if is_safe(node, c):
                color[node] = c
                if dfs(node + 1):
                    return True
                color[node] = 0  # backtrack
        return False
    
    # Try to color all nodes starting from 1
    if dfs(1):
        print("YES")
        print(' '.join(map(str, color[1:])))
    else:
        print("NO")

solve()
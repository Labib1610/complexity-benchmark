def solve():
    import sys
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().split()
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    
    visited = [False] * n
    components = []
    
    for start in range(n):
        if not visited[start]:
            component = []
            stack = [start]
            while stack:
                v = stack.pop()
                if visited[v]:
                    continue
                visited[v] = True
                component.append(v)
                for neighbor in adj[v]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
            components.append(sorted(component))
    
    colors = [0] * n
    
    def backtrack(component, idx):
        if idx == len(component):
            return True
        v = component[idx]
        for c in range(1, 4):
            valid = True
            for neighbor in adj[v]:
                if colors[neighbor] == c:
                    valid = False
                    break
            if valid:
                colors[v] = c
                if backtrack(component, idx + 1):
                    return True
                colors[v] = 0
        return False
    
    for component in components:
        if not backtrack(component, 0):
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, colors)))

solve()
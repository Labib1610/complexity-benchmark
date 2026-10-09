import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * n
    
    # Check bipartiteness of the incompatibility graph
    for start in range(n):
        if color[start] == 0:
            color[start] = 1
            stack = [start]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # Graph is bipartite, so 3-coloring is possible
    # Use the bipartition: color 1 -> vault 1, color 2 -> vault 2, isolated vertices -> vault 3
    result = []
    for i in range(n):
        if color[i] == 1:
            result.append(1)
        elif color[i] == 2:
            result.append(2)
        else:
            result.append(3)
    
    print("YES")
    print(' '.join(map(str, result)))

solve()
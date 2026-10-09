import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    edges = []
    for i in range(m):
        u = int(input_data[2 + 2*i])
        v = int(input_data[2 + 2*i + 1])
        edges.append((u, v))
    
    adj = [[] for _ in range(n + 1)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    color = [0] * m
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if not visited[start]:
            stack = [(start, 0, -1, -1)]
            while stack:
                u, cu, pe, pu = stack.pop()
                if visited[u]:
                    continue
                visited[u] = True
                for v, e in adj[u]:
                    if e == pe:
                        continue
                    if visited[v]:
                        if color[e] == 0:
                            color[e] = 6 - cu - 1
                    else:
                        cv = 3 - cu
                        color[e] = cv
                        stack.append((v, cv, e, u))
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)) + "\n")

solve()
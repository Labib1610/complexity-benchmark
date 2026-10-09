import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, B = map(int, input().split())
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Compute subtree sizes
    parent = [-1] * n
    order = [0]
    for u in order:
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)
    
    size = [1] * n
    for u in reversed(order):
        for v in adj[u]:
            if v != parent[u]:
                size[u] += size[v]
    
    min_cost = 0
    for u, v in edges:
        if parent[v] == u:
            s = size[v]
        else:
            s = size[u]
        min_cost += s * (n - s)
    
    if min_cost > B:
        print("NO")
        return
    
    # Build a valid arrangement: DFS order
    pos = [0] * n
    idx = 0
    stack = [0]
    visited = [False] * n
    visited[0] = True
    while stack:
        u = stack.pop()
        pos[u] = idx + 1
        idx += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    print("YES")
    print(" ".join(map(str, pos)))

if __name__ == "__main__":
    solve()
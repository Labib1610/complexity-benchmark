import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, B = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    parent = [-1]*n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in g[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
    
    size = [1]*n
    for u in reversed(order):
        for v in g[u]:
            if parent[v] == u:
                size[u] += size[v]
    
    min_cost = 0
    for u in range(1, n):
        s = size[u]
        min_cost += min(s, n - s)
    
    if min_cost > B:
        print("NO")
        return
    
    # Assign by DFS preorder
    assign = [0]*n
    idx = 1
    stack = [0]
    visited = [False]*n
    visited[0] = True
    while stack:
        u = stack.pop()
        assign[u] = idx
        idx += 1
        for v in g[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    
    print("YES")
    print(" ".join(map(str, assign)))

if __name__ == "__main__":
    solve()
import sys
sys.setrecursionlimit(300000)

def solve():
    n, m, B = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    pos = [0] * n
    visited = [False] * n
    order = []
    
    def dfs(u):
        visited[u] = True
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
    
    dfs(0)
    
    # Assign positions 1..n in DFS order
    for idx, node in enumerate(order):
        pos[node] = idx + 1
    
    # Compute cost
    cost = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                cost += abs(pos[u] - pos[v])
    
    if cost <= B:
        print("YES")
        print(" ".join(map(str, pos)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
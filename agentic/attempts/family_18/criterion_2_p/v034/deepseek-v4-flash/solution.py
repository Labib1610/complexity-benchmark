import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, B = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    pos = [0] * n
    order = []
    visited = [False] * n
    
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
    
    # Compute total wire length
    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u] - pos[v])
    
    if total <= B:
        print("YES")
        print(" ".join(str(pos[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
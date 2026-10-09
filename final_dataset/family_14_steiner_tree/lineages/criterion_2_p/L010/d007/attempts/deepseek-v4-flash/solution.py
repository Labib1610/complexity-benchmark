import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    visited = [False] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        has_critical = u in critical
        total_cost = 0
        for v, w in adj[u]:
            if not visited[v]:
                child_has, child_cost = dfs(v)
                if child_has:
                    total_cost += child_cost + w
                    has_critical = True
        return has_critical, total_cost
    
    # Start from any critical node
    start = next(iter(critical))
    _, ans = dfs(start)
    print(ans)

if __name__ == "__main__":
    solve()
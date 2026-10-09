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
    
    def dfs(u, parent):
        visited[u] = True
        has_critical = u in critical
        total = 0
        for v, w in adj[u]:
            if v == parent:
                continue
            if not visited[v]:
                sub_has, sub_cost = dfs(v, u)
                if sub_has:
                    total += sub_cost + w
                    has_critical = True
        return has_critical, total
    
    # start from any critical node
    start = next(iter(critical))
    _, ans = dfs(start, -1)
    print(ans)

if __name__ == "__main__":
    solve()
import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    visited = [False] * (n+1)
    total_cost = 0
    
    def dfs(u, parent):
        nonlocal total_cost
        visited[u] = True
        has_critical = u in critical
        for v, w in adj[u]:
            if v != parent and not visited[v]:
                child_has = dfs(v, u)
                if child_has:
                    total_cost += w
                    has_critical = True
        return has_critical
    
    # start from any critical node
    start = next(iter(critical))
    dfs(start, -1)
    print(total_cost)

if __name__ == "__main__":
    solve()
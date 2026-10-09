import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    N, E, F = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(N+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    visited = [False] * (N+1)
    
    def dfs(u, parent):
        visited[u] = True
        has_critical = u in critical
        total_cost = 0
        for v, w in adj[u]:
            if v == parent:
                continue
            if not visited[v]:
                sub_cost, sub_has = dfs(v, u)
                if sub_has:
                    total_cost += w + sub_cost
                    has_critical = True
        return total_cost, has_critical
    
    # Start from any critical node
    start = next(iter(critical))
    cost, _ = dfs(start, -1)
    print(cost)

if __name__ == "__main__":
    solve()
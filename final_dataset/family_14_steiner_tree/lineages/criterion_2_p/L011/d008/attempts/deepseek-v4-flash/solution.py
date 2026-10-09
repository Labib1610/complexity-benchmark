import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    visited = [False] * (n + 1)
    
    def dfs(u, parent):
        visited[u] = True
        has_target = u in targets
        total_cost = 0
        for v, w in adj[u]:
            if v == parent:
                continue
            if not visited[v]:
                sub_cost, sub_has_target = dfs(v, u)
                if sub_has_target:
                    total_cost += sub_cost + w
                    has_target = True
        return total_cost, has_target
    
    # Start from any target node
    start = next(iter(targets))
    cost, _ = dfs(start, -1)
    print(cost)

if __name__ == "__main__":
    solve()
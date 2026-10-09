import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    required = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    visited = [False] * (n + 1)
    total_cost = 0
    
    def dfs(u):
        nonlocal total_cost
        visited[u] = True
        has_required = u in required
        for v, w in adj[u]:
            if not visited[v]:
                child_has = dfs(v)
                if child_has:
                    total_cost += w
                    has_required = True
        return has_required
    
    # Start from any required node
    start = next(iter(required))
    dfs(start)
    
    print(total_cost)

if __name__ == "__main__":
    solve()
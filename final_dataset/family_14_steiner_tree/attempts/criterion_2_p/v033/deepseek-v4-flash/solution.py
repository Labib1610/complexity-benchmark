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
    
    # Root at any required node
    root = next(iter(required))
    
    visited = [False] * (n + 1)
    total_cost = 0
    
    def dfs(u):
        visited[u] = True
        has_required = u in required
        for v, w in adj[u]:
            if not visited[v]:
                child_has = dfs(v)
                if child_has:
                    total_cost += w
                has_required = has_required or child_has
        return has_required
    
    dfs(root)
    print(total_cost)

if __name__ == "__main__":
    solve()
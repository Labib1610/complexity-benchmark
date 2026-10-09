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
    
    def dfs(u, parent):
        visited[u] = True
        has_required = u in required
        total_weight = 0
        for v, w in adj[u]:
            if v == parent:
                continue
            if not visited[v]:
                child_has_required, child_weight = dfs(v, u)
                if child_has_required:
                    total_weight += child_weight + w
                    has_required = True
        return has_required, total_weight
    
    # Start from any required node
    start = next(iter(required))
    _, ans = dfs(start, -1)
    print(ans)

if __name__ == "__main__":
    solve()
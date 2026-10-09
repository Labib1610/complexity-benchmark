import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    primaries = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # DFS to find edges that are part of the minimal subtree
    visited = [False] * (n + 1)
    
    def dfs(u, parent):
        visited[u] = True
        has_primary = u in primaries
        total_cost = 0
        for v, w in adj[u]:
            if v == parent:
                continue
            child_cost, child_has_primary = dfs(v, u)
            if child_has_primary:
                total_cost += child_cost + w
                has_primary = True
        return total_cost, has_primary
    
    # Start from any primary node
    start = next(iter(primaries))
    total_cost, _ = dfs(start, -1)
    print(total_cost)

if __name__ == "__main__":
    solve()
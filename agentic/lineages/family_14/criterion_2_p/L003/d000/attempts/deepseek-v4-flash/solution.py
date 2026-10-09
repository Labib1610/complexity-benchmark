import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    priority = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    # Root at any priority node
    root = next(iter(priority)) - 1
    visited = [False] * n
    total_cost = 0
    
    def dfs(u):
        nonlocal total_cost
        visited[u] = True
        has_priority = (u + 1) in priority
        for v, w in adj[u]:
            if not visited[v]:
                child_has_priority = dfs(v)
                if child_has_priority:
                    total_cost += w
                has_priority = has_priority or child_has_priority
        return has_priority
    
    dfs(root)
    print(total_cost)

if __name__ == "__main__":
    solve()
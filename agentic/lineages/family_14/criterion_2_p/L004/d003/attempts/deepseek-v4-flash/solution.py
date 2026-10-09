import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to count critical nodes in subtree
    visited = [False] * (n + 1)
    critical_count = [0] * (n + 1)
    
    def dfs(u):
        visited[u] = True
        cnt = 1 if u in critical else 0
        for v, w in adj[u]:
            if not visited[v]:
                cnt += dfs(v)
        critical_count[u] = cnt
        return cnt
    
    # Start from any critical node
    start = next(iter(critical))
    dfs(start)
    
    total_cost = 0
    for u, v, w in edges:
        # Edge is needed if one side has at least one critical and the other side also has at least one
        if critical_count[u] > 0 and critical_count[u] < t:
            total_cost += w
        elif critical_count[v] > 0 and critical_count[v] < t:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()
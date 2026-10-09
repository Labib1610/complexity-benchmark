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
    
    # DFS to find minimal subtree containing all critical nodes
    visited = [False] * (n+1)
    
    def dfs(u, parent):
        visited[u] = True
        need = u in critical
        total_cost = 0
        for v, w in adj[u]:
            if v == parent:
                continue
            if not visited[v]:
                child_need, child_cost = dfs(v, u)
                if child_need:
                    need = True
                    total_cost += child_cost + w
        return need, total_cost
    
    # Start from any critical node
    start = next(iter(critical))
    _, cost = dfs(start, -1)
    print(cost)

if __name__ == "__main__":
    solve()
import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # Find a critical node to start DFS
    start = next(iter(critical))
    
    visited = [False] * n
    cost = 0
    
    def dfs(u):
        visited[u] = True
        has_critical = u in critical
        for v, w in adj[u]:
            if not visited[v]:
                child_has = dfs(v)
                if child_has:
                    cost_holder[0] += w
                has_critical = has_critical or child_has
        return has_critical
    
    cost_holder = [0]
    dfs(start)
    print(cost_holder[0])

if __name__ == "__main__":
    solve()
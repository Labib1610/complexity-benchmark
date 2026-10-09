import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    mandatory = set(map(int, input().split()))
    
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
    
    visited = [False] * (n + 1)
    total_cost = 0
    
    def dfs(u, parent):
        nonlocal total_cost
        visited[u] = True
        has_mandatory = u in mandatory
        for v, w in g[u]:
            if v == parent:
                continue
            if not visited[v]:
                child_has = dfs(v, u)
                if child_has:
                    total_cost += w
                has_mandatory = has_mandatory or child_has
        return has_mandatory
    
    # Start from any mandatory node
    start = next(iter(mandatory))
    dfs(start, -1)
    
    print(total_cost)

if __name__ == "__main__":
    solve()
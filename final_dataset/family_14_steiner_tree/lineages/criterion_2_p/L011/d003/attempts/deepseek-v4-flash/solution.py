import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = set(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t == 1:
        print(0)
        return
    
    # DFS to find edges that are part of minimal subtree connecting terminals
    visited = [False] * (n+1)
    total_cost = 0
    
    def dfs(u, parent):
        nonlocal total_cost
        visited[u] = True
        has_terminal = u in terminals
        for v, w in adj[u]:
            if v == parent:
                continue
            if not visited[v]:
                child_has_terminal = dfs(v, u)
                if child_has_terminal:
                    total_cost += w
                has_terminal = has_terminal or child_has_terminal
        return has_terminal
    
    # Start from any terminal
    start = next(iter(terminals))
    dfs(start, -1)
    
    print(total_cost)

if __name__ == "__main__":
    solve()
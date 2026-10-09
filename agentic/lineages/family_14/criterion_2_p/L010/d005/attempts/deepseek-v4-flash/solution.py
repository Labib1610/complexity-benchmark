import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    terminals = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to mark which edges are needed
    visited = [False] * (n + 1)
    needed = [False] * (n + 1)  # needed[i] means edge to parent is needed
    
    def dfs(u, parent, parent_edge_weight):
        visited[u] = True
        has_terminal = u in terminals
        for v, w in adj[u]:
            if v == parent:
                continue
            if not visited[v]:
                child_has = dfs(v, u, w)
                if child_has:
                    needed[v] = True
                    has_terminal = True
        return has_terminal
    
    # Start from any terminal
    start = next(iter(terminals))
    dfs(start, -1, 0)
    
    total = 0
    for u, v, w in edges:
        if needed[u] or needed[v]:
            total += w
    
    print(total)

if __name__ == "__main__":
    solve()
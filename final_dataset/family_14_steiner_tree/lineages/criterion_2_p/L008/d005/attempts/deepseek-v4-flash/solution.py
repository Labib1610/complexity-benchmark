import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    R, S, P = map(int, input().split())
    injected = set(map(int, input().split()))
    
    adj = [[] for _ in range(R + 1)]
    edges = []
    for _ in range(S):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        edges.append((u, v, w))
    
    # DFS to find which edges are needed
    visited = [False] * (R + 1)
    needed = [False] * (R + 1)  # for edges, we'll store by index
    
    # We'll store edge index for each adjacency
    adj_idx = [[] for _ in range(R + 1)]
    for idx, (u, v, w) in enumerate(edges):
        adj_idx[u].append((v, w, idx))
        adj_idx[v].append((u, w, idx))
    
    def dfs(u):
        visited[u] = True
        has_injected = u in injected
        for v, w, idx in adj_idx[u]:
            if not visited[v]:
                child_has = dfs(v)
                if child_has:
                    needed[idx] = True
                has_injected |= child_has
        return has_injected
    
    # Start from any injected node
    start = next(iter(injected))
    dfs(start)
    
    total_cost = 0
    for idx, (u, v, w) in enumerate(edges):
        if needed[idx]:
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    solve()
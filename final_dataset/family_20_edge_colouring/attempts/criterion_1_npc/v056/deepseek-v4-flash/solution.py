import sys
sys.setrecursionlimit(1000000)

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    # Find bridges
    tin = [-1]*n
    low = [-1]*n
    timer = [0]
    visited = [False]*n
    
    def dfs(v, p_edge):
        visited[v] = True
        tin[v] = low[v] = timer[0]
        timer[0] += 1
        for to, eidx in adj[v]:
            if eidx == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eidx)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    # bridge
                    bridges.append(eidx)
    
    bridges = []
    for i in range(n):
        if not visited[i]:
            dfs(i, -1)
    if bridges:
        print("NO")
        return
    
    # Assign colors
    color = [-1]*m
    used_at = [[False]*3 for _ in range(n)]
    
    # order edges: by degree constraint
    # We'll backtrack
    def backtrack(edge_idx):
        if edge_idx == m:
            return True
        u, v = edges[edge_idx]
        for c in range(3):
            if not used_at[u][c] and not used_at[v][c]:
                color[edge_idx] = c
                used_at[u][c] = True
                used_at[v][c] = True
                if backtrack(edge_idx + 1):
                    return True
                used_at[u][c] = False
                used_at[v][c] = False
                color[edge_idx] = -1
        return False
    
    # However, naive order might cause early bad choices.
    # We can sort edges by degree of endpoints? Simple approach may work since cubic small.
    if backtrack(0):
        print("YES")
        print(" ".join(str(c+1) for c in color))
    else:
        # Should not happen if no bridges, but just in case
        print("NO")

if __name__ == "__main__":
    main()
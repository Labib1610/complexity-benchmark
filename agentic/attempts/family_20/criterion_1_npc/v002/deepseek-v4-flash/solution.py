import sys
sys.setrecursionlimit(1000000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))
    
    color = [0] * m  # 0 = uncolored, 1..3 = colors

    # For each vertex, keep list of (edge_index, neighbor)
    # We want to color edges so that at each vertex, the three incident edges have distinct colors.

    # Backtracking with propagation
    # At any step, pick an uncolored edge, try colors 1..3
    
    # Pre-check to speed: if vertex already has 3 distinct colored edges, no choice.
    
    def vertex_possible(v):
        cols = [color[e] for (u, e) in adj[v] if color[e] != 0]
        # Must be all distinct
        return len(cols) == len(set(cols))
    
    def dfs(edge_idx):
        if edge_idx == m:
            return True
        if color[edge_idx] != 0:
            return dfs(edge_idx + 1)
        u, v = edges[edge_idx]
        # Get used colors at u and v
        used_u = [color[e] for (x, e) in adj[u] if color[e] != 0]
        used_v = [color[e] for (x, e) in adj[v] if color[e] != 0]
        used = set(used_u + used_v)
        for c in (1, 2, 3):
            if c not in used:
                color[edge_idx] = c
                # Check both endpoints still valid
                if vertex_possible(u) and vertex_possible(v):
                    if dfs(edge_idx + 1):
                        return True
                color[edge_idx] = 0
        return False

    if dfs(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
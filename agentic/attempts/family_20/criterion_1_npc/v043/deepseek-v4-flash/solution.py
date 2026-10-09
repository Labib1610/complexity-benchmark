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
    
    color = [-1] * m
    
    # Check if graph is bridgeless
    # Find bridges using DFS
    tin = [-1] * n
    low = [-1] * n
    timer = [0]
    visited = [False] * n
    
    def dfs_bridge(v, p_edge):
        visited[v] = True
        tin[v] = low[v] = timer[0]
        timer[0] += 1
        for to, eid in adj[v]:
            if eid == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs_bridge(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    # bridge found
                    return False
        return True
    
    # Graph is connected? Not guaranteed, but we can check all components
    for i in range(n):
        if not visited[i]:
            if not dfs_bridge(i, -1):
                print("NO")
                return
    
    # Now try to 3-edge-color using backtracking
    # We'll use a recursive function that colors edges in order
    # At each step, pick an uncolored edge and try colors 1,2,3
    
    # To speed up, we can order edges by degree of endpoints (most constrained first)
    # But simple order is fine for n=2000
    
    # We'll store used colors at each vertex
    used = [0] * n  # bitmask of used colors (bits 0,1,2 for colors 1,2,3)
    
    def backtrack(idx):
        if idx == m:
            return True
        u, v = edges[idx]
        # Try colors 1,2,3
        for c in range(3):
            if not (used[u] & (1 << c)) and not (used[v] & (1 << c)):
                color[idx] = c
                used[u] |= (1 << c)
                used[v] |= (1 << c)
                if backtrack(idx + 1):
                    return True
                used[u] ^= (1 << c)
                used[v] ^= (1 << c)
                color[idx] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
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
    
    K = 2 * m // n  # should be 3 for this problem
    
    # Check if graph is bridgeless
    # Find bridges using DFS
    disc = [-1] * n
    low = [0] * n
    time = 0
    bridges = set()
    
    def dfs(u, parent_edge):
        nonlocal time
        disc[u] = low[u] = time
        time += 1
        for v, eid in adj[u]:
            if eid == parent_edge:
                continue
            if disc[v] == -1:
                dfs(v, eid)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.add(eid)
            else:
                low[u] = min(low[u], disc[v])
    
    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
    
    if bridges:
        print("NO")
        return
    
    # Now find a proper 3-edge-coloring using backtracking
    color = [-1] * m
    # For each vertex, which colors are used
    used_at_vertex = [set() for _ in range(n)]
    
    # Sort edges by degree of endpoints to improve backtracking
    edge_order = list(range(m))
    edge_order.sort(key=lambda e: len(adj[edges[e][0]]) + len(adj[edges[e][1]]), reverse=True)
    
    def backtrack(eidx):
        if eidx == m:
            return True
        e = edge_order[eidx]
        u, v = edges[e]
        # Try colors 1..K
        for c in range(1, K+1):
            if c not in used_at_vertex[u] and c not in used_at_vertex[v]:
                color[e] = c
                used_at_vertex[u].add(c)
                used_at_vertex[v].add(c)
                if backtrack(eidx + 1):
                    return True
                used_at_vertex[u].remove(c)
                used_at_vertex[v].remove(c)
                color[e] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(m)))
    else:
        print("NO")

if __name__ == "__main__":
    main()
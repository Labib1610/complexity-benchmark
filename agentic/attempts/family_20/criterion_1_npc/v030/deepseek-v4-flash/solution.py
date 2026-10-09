import sys
sys.setrecursionlimit(1000000)

def solve():
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
    
    # Check if graph is 3-regular
    for i in range(n):
        if len(adj[i]) != 3:
            print("NO")
            return
    
    color = [-1] * m
    # For each vertex, track used colors
    used_at_vertex = [set() for _ in range(n)]
    
    # Order edges by degree of endpoints (most constrained first)
    edge_order = list(range(m))
    edge_order.sort(key=lambda e: len(adj[edges[e][0]]) + len(adj[edges[e][1]]), reverse=True)
    
    def backtrack(idx):
        if idx == m:
            return True
        e = edge_order[idx]
        u, v = edges[e]
        # Try colors 1,2,3
        for c in range(1, 4):
            if c not in used_at_vertex[u] and c not in used_at_vertex[v]:
                color[e] = c
                used_at_vertex[u].add(c)
                used_at_vertex[v].add(c)
                if backtrack(idx + 1):
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
    solve()
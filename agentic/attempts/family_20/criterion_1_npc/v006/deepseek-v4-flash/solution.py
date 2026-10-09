import sys
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for idx in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    
    color = [-1] * m
    # For each vertex, track used colors
    used_at_vertex = [set() for _ in range(n)]
    
    # Sort edges by degree of endpoints for better pruning
    order = list(range(m))
    order.sort(key=lambda e: len(adj[edges[e][0]]) + len(adj[edges[e][1]]), reverse=True)
    
    def backtrack(pos):
        if pos == m:
            return True
        e = order[pos]
        u, v = edges[e]
        # Try colors 1,2,3
        for c in (1,2,3):
            if c not in used_at_vertex[u] and c not in used_at_vertex[v]:
                color[e] = c
                used_at_vertex[u].add(c)
                used_at_vertex[v].add(c)
                if backtrack(pos + 1):
                    return True
                used_at_vertex[u].remove(c)
                used_at_vertex[v].remove(c)
                color[e] = -1
        return False
    
    if backtrack(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(color[i]) for i in range(m)) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == "__main__":
    solve()
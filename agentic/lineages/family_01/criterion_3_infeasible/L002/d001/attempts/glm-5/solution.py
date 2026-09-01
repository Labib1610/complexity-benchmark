import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
        deg[u] += 1
        deg[v] += 1
    
    # Sort vertices by degree
    vertices = list(range(1, n + 1))
    vertices.sort(key=lambda x: deg[x])
    
    # For each vertex, create sorted neighbor list
    neighbors = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if adj[u][v]:
                neighbors[u].append(v)
    
    found = None
    
    # Iterate vertices in order of increasing degree
    for u in vertices:
        # Get neighbors of u
        nu = neighbors[u]
        # For each pair of neighbors (v, w) with v < w
        for i in range(len(nu)):
            v = nu[i]
            for j in range(i + 1, len(nu)):
                w = nu[j]
                if adj[v][w]:
                    # Found triangle
                    a, b, c = sorted([u, v, w])
                    if found is None or (a, b, c) < found:
                        found = (a, b, c)
    
    print(found[0], found[1], found[2])

solve()
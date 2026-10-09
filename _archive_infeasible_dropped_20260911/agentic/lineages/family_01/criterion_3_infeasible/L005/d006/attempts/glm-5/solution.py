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
    
    # Iterate over vertices in sorted order to find the lexicographically smallest triangle
    # This works because the first triangle found in this order will have the smallest 'a',
    # and for the same 'a', the smallest 'b', etc.
    for u in vertices:
        # Collect neighbors of u that are greater than u
        neighbors = [v for v in range(u + 1, n + 1) if adj[u][v]]
        # Check all pairs of neighbors
        for i in range(len(neighbors)):
            v = neighbors[i]
            for j in range(i + 1, len(neighbors)):
                w = neighbors[j]
                if adj[v][w]:
                    print(u, v, w)
                    return

if __name__ == '__main__':
    solve()
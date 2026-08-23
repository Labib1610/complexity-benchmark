import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    deg = [0] * (n + 1)
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u][v] = True
        adj[v][u] = True
        deg[u] += 1
        deg[v] += 1
    
    # Sort vertices by degree
    vertices = list(range(1, n + 1))
    vertices.sort(key=lambda x: deg[x])
    
    # Iterate over vertices in order of non-decreasing degree
    for u in vertices:
        # Collect neighbors of u
        neighbors = []
        # Iterate neighbors efficiently
        # Since n <= 2000, O(n) check is acceptable
        for v in range(1, n + 1):
            if adj[u][v]:
                neighbors.append(v)
        
        # Check all pairs of neighbors
        k = len(neighbors)
        for i in range(k):
            for j in range(i + 1, k):
                v = neighbors[i]
                w = neighbors[j]
                if adj[v][w]:
                    # Found a triangle
                    # Sort to ensure a < b < c
                    trio = sorted([u, v, w])
                    print(trio[0], trio[1], trio[2])
                    return

if __name__ == '__main__':
    solve()
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
    
    # Iterate to find lexicographically smallest triangle
    for a in range(1, n - 1):
        # Collect neighbors of a that are > a
        neighbors_a = []
        # We can iterate b from a+1 to n, but collecting neighbors first might be faster
        # if degree is small. However, worst case is dense graph.
        # Iterating b and checking adj[a][b] is O(n) per a.
        for b in range(a + 1, n + 1):
            if adj[a][b]:
                neighbors_a.append(b)
        
        # For each pair of neighbors b, c of a, check if b and c are connected
        # neighbors_a is sorted because b loop was increasing
        # We need b < c
        limit = len(neighbors_a)
        for i in range(limit):
            b = neighbors_a[i]
            for j in range(i + 1, limit):
                c = neighbors_a[j]
                if adj[b][c]:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()
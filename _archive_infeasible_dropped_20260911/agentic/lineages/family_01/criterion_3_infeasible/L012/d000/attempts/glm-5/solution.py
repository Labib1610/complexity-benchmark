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
        # Find all neighbors of a that are > a
        neighbors_a = []
        for b in range(a + 1, n + 1):
            if adj[a][b]:
                neighbors_a.append(b)
        
        # Check pairs among neighbors_a
        # Since neighbors_a is sorted (due to iteration order), 
        # the first valid pair (b, c) found will be lexicographically smallest for this a
        len_na = len(neighbors_a)
        for i in range(len_na):
            b = neighbors_a[i]
            for j in range(i + 1, len_na):
                c = neighbors_a[j]
                if adj[b][c]:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()
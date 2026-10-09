import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u][v] = True
        adj[v][u] = True
    
    # Iterate through all triples to find the lexicographically smallest valid one
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if not adj[a][b]:
                continue
            for c in range(b + 1, n + 1):
                if adj[a][c] and adj[b][c]:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()
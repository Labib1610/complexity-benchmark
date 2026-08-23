import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
    
    best_a = n + 1
    best_b = n + 1
    best_c = n + 1
    
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if not adj[a][b]:
                continue
            for c in range(b + 1, n + 1):
                if adj[a][c] and adj[b][c]:
                    if a < best_a or (a == best_a and b < best_b) or (a == best_a and b == best_b and c < best_c):
                        best_a = a
                        best_b = b
                        best_c = c
    
    print(best_a, best_b, best_c)

if __name__ == "__main__":
    solve()
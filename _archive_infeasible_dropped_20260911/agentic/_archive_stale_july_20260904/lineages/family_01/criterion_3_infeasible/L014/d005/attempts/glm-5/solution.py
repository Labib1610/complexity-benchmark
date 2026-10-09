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
    
    # Iterate through all triples a < b < c to find the lexicographically smallest deadlock
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            for c in range(b + 1, n + 1):
                # Count prohibited pairs among (a, b, c)
                cnt = 0
                if adj[a][b]:
                    cnt += 1
                if adj[a][c]:
                    cnt += 1
                if adj[b][c]:
                    cnt += 1
                
                # Condition 1: At least one prohibited pair
                if cnt == 0:
                    continue
                
                # Condition 2: For any two materials, they have the same prohibition status
                # with respect to the third.
                # This is equivalent to cnt being 1 or 3.
                if cnt == 1 or cnt == 3:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
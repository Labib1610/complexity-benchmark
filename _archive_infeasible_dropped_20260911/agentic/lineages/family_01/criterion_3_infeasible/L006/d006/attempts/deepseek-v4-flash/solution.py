import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u][v] = True
        adj[v][u] = True
    
    # Try each possible b
    for b in range(1, n + 1):
        # Collect smaller neighbors and larger neighbors
        smaller = []
        larger = []
        for i in range(1, n + 1):
            if adj[b][i]:
                if i < b:
                    smaller.append(i)
                elif i > b:
                    larger.append(i)
        
        # Check all pairs (a from smaller, c from larger)
        for a in smaller:
            for c in larger:
                if adj[a][c]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    solve()
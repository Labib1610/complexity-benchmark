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
    
    # Iterate through all possible trios in lexicographical order
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if adj[i][j]:
                for k in range(j + 1, n + 1):
                    if adj[i][k] and adj[j][k]:
                        print(i, j, k)
                        return

if __name__ == '__main__':
    solve()
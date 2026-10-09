import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u][v] = True
        adj[v][u] = True
        edges.append((u, v))
    
    # Check for triangle (3-clique)
    for u, v in edges:
        for w in range(1, n + 1):
            if w != u and w != v and adj[u][w] and adj[v][w]:
                result = sorted([u, v, w])
                print(result[0], result[1], result[2])
                return
    
    # Check for independent set of size 3
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if adj[i][j]:
                continue
            for k in range(j + 1, n + 1):
                if adj[i][k] or adj[j][k]:
                    continue
                print(i, j, k)
                return
    
    # Check for P3 (path of length 2)
    for u in range(1, n + 1):
        for v in range(1, n + 1):
            if v == u or adj[u][v]:
                continue
            for w in range(1, n + 1):
                if w == u or w == v:
                    continue
                if adj[u][w] and adj[v][w]:
                    result = sorted([u, v, w])
                    print(result[0], result[1], result[2])
                    return

if __name__ == "__main__":
    solve()
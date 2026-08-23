import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[False] * n for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u][v] = True
        adj[v][u] = True
    
    # Greedy assignment: for each vertex, assign the smallest valid color
    colors = [0] * n
    for u in range(n):
        used = [False] * 4
        for v in range(n):
            if adj[u][v] and colors[v] != 0:
                used[colors[v]] = True
        for c in range(1, 4):
            if not used[c]:
                colors[u] = c
                break
        if colors[u] == 0:
            print("NO")
            return
    
    # Verify solution
    for u in range(n):
        for v in range(u + 1, n):
            if adj[u][v] and colors[u] == colors[v]:
                print("NO")
                return
    
    print("YES")
    print(' '.join(map(str, colors)))

if __name__ == "__main__":
    solve()
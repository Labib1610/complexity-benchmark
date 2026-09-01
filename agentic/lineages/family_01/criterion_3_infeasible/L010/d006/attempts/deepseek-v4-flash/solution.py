import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    mat = [[False] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        mat[u][v] = mat[v][u] = True
    
    for i in range(1, n + 1):
        adj[i].sort()
    
    # Find lexicographically smallest triangle
    for u in range(1, n + 1):
        for v in adj[u]:
            if v <= u:
                continue
            for w in adj[u]:
                if w <= v:
                    continue
                if mat[v][w]:
                    print(u, v, w)
                    return

if __name__ == "__main__":
    solve()
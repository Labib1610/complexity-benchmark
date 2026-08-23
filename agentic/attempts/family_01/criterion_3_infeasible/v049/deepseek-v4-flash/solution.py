import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
        if u > v:
            u, v = v, u
        edges.append((u, v))
    
    edges.sort()
    for u, v in edges:
        common = adj[u] & adj[v]
        if common:
            w = min(common)
            if w > v:
                print(u, v, w)
                return

if __name__ == "__main__":
    solve()
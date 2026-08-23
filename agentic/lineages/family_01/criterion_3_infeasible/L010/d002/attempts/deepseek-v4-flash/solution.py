import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = set()
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        edges.add((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    for u in range(1, n + 1):
        adj[u].sort()
    
    for u in range(1, n + 1):
        for v in adj[u]:
            if v <= u:
                continue
            for w in adj[v]:
                if w <= v:
                    continue
                if (u, w) in edges:
                    print(u, v, w)
                    return

if __name__ == "__main__":
    solve()
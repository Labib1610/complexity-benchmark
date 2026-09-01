import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n+1)]
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
        # find w > v such that (u,w) and (v,w) exist
        for w in adj[u]:
            if w > v and w in adj[v]:
                print(u, v, w)
                return

if __name__ == "__main__":
    solve()
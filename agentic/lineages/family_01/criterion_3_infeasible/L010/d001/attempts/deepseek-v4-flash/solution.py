import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    edges = []
    edge_set = set()

    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        edges.append((u, v))
        edge_set.add((u, v))
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1, n + 1):
        adj[i].sort()

    # Iterate edges in sorted order
    edges.sort()
    for u, v in edges:
        for w in adj[u]:
            if w > v and (v, w) in edge_set:
                print(u, v, w)
                return

if __name__ == "__main__":
    solve()
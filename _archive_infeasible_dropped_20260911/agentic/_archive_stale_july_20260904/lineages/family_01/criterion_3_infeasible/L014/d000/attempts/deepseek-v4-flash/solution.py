import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    edges.sort()
    
    for u, v in edges:
        # Find common neighbors w > v
        common = adj[u] & adj[v]
        for w in sorted(common):
            if w > v:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()
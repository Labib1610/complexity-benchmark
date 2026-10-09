import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = set()
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        edges.add((u, v))
        edges.add((v, u))
        adj[u].append(v)
        adj[v].append(u)
    
    for a in range(1, n + 1):
        adj[a].sort()
        for i in range(len(adj[a])):
            b = adj[a][i]
            if b <= a:
                continue
            for j in range(i + 1, len(adj[a])):
                c = adj[a][j]
                if c <= b:
                    continue
                if (b, c) in edges:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()
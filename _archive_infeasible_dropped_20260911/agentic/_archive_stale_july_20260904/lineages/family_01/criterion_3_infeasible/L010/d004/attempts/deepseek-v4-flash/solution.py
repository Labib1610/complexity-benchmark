import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    edge_set = set()
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edge_set.add((u, v))
        edge_set.add((v, u))
    
    for a in range(1, n + 1):
        for b in adj[a]:
            if b <= a:
                continue
            for c in adj[a]:
                if c <= b:
                    continue
                if (b, c) in edge_set:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()
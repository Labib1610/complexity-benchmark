import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges by u then v for lexicographical ordering
    edges.sort()
    
    for u, v in edges:
        # Find smallest common neighbor w > v
        common = adj[u].intersection(adj[v])
        if common:
            w = min(common)
            if v < w:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()
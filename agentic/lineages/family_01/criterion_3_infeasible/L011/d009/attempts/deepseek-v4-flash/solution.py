import sys

def main():
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
    
    # Sort edges by u then v
    edges.sort()
    
    for u, v in edges:
        # Find common neighbor w > v
        # Iterate over neighbors of u that are > v
        for w in adj[u]:
            if w > v and w in adj[v]:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()
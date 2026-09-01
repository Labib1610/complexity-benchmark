import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = set()
    adj = [set() for _ in range(n + 1)]
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        if u > v:
            u, v = v, u
        edges.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We need to find a triangle in the complement graph
    # That is, three nodes u<v<w such that none of (u,v), (u,w), (v,w) are in the edge list
    
    for u in range(1, n - 1):
        for v in range(u + 1, n):
            if (u, v) in edges:
                continue
            for w in range(v + 1, n + 1):
                if (u, w) in edges or (v, w) in edges:
                    continue
                # Found a triangle in complement: u-v-w with no edges between them
                print(u, v, w)
                return

if __name__ == "__main__":
    main()
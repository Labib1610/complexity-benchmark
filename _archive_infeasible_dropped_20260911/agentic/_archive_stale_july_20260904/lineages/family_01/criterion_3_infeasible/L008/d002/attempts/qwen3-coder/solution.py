import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    graph = defaultdict(set)
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        graph[u].add(v)
        graph[v].add(u)
    
    # Sort edges to help with ordering
    edges.sort()
    
    # For each edge (u,v), look for a common neighbor w
    # such that u < v < w and (u,w) and (v,w) are also edges
    for u, v in edges:
        if u >= v:
            continue
        # Find common neighbors of u and v that are > v
        for w in graph[u]:
            if w > v and w in graph[v]:
                print(u, v, w)
                return

if __name__ == "__main__":
    main()
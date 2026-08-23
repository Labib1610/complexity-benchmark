import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort edges to process in order
    edges.sort()
    
    # For each edge (u,v), look for a common neighbor w
    min_score = float('inf')
    result = None
    
    for u, v in edges:
        if u >= n:
            continue
        # Get neighbors of u and v
        neighbors_u = adj[u]
        neighbors_v = adj[v]
        
        # Find common neighbors
        common = neighbors_u & neighbors_v
        for w in common:
            if u < v < w:
                score = u * 100000000 + v * 10000 + w
                if score < min_score:
                    min_score = score
                    result = (u, v, w)
    
    if result:
        print(result[0], result[1], result[2])

if __name__ == "__main__":
    main()
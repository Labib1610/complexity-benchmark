import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = set()
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        edges.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert adjacency sets to sorted lists for deterministic iteration
    for node in adj:
        adj[node] = sorted(adj[node])
    
    # Iterate through all nodes in increasing order
    for a in range(1, n+1):
        if a not in adj:
            continue
        neighbors_a = adj[a]
        # For each pair of neighbors of 'a'
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            for j in range(i+1, len(neighbors_a)):
                c = neighbors_a[j]
                if c <= b:
                    continue
                # Check if b and c are connected
                if (b, c) in edges:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()
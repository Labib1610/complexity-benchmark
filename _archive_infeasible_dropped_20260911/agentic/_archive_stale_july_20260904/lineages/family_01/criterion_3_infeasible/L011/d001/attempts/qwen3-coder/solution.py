import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    edge_set = set()
    adj = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        edge_set.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Generate all triangles by checking each combination of 3 nodes
    min_triangle = None
    
    # We'll iterate through all combinations of 3 nodes
    for a, b, c in combinations(range(1, n+1), 3):
        # Check if all three edges exist
        if (a,b) in edge_set and (a,c) in edge_set and (b,c) in edge_set:
            if min_triangle is None or (a,b,c) < min_triangle:
                min_triangle = (a,b,c)
    
    print(min_triangle[0], min_triangle[1], min_triangle[2])

if __name__ == "__main__":
    main()
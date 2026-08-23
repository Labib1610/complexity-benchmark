import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    edge_set = set()
    adj = defaultdict(set)
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        edge_set.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert sets to lists for faster iteration
    adj_list = {k: list(v) for k, v in adj.items()}
    
    # We want the lexicographically smallest (a,b,c) with a<b<c such that 
    # all three pairs (a,b), (b,c), (a,c) exist
    
    # Try all possible a, then b, then c in order
    for a in range(1, n+1):
        if a not in adj_list:
            continue
        neighbors_a = adj_list[a]
        # Sort neighbors of a to ensure we process b in increasing order
        neighbors_a.sort()
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            if b not in adj_list:
                continue
            neighbors_b = adj_list[b]
            # To find common neighbor c > b, we can intersect neighbors of a and b,
            # but we need c > b and also (a,c) and (b,c) exist
            # Let's iterate through neighbors of b
            for c in neighbors_b:
                if c <= b:
                    continue
                # Check if (a,c) exists
                if (a < c and (a, c) in edge_set) or (c < a and (c, a) in edge_set):
                    # All three edges (a,b), (b,c), (a,c) exist
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()
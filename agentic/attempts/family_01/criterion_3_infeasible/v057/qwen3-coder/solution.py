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
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to list for ordered iteration
    nodes = list(range(1, n+1))
    
    # For each node a, check its neighbors b
    # For each pair (a,b), check neighbors of b (c) that are also neighbors of a
    # That forms a triangle a-b-c
    
    # We want the lexicographically smallest triangle
    # So we iterate a from 1 to n
    # For each a, iterate b from neighbors of a that are > a
    # For each b, iterate c from neighbors of b that are > b
    # Check if c is also a neighbor of a
    # If so, we found a triangle a < b < c
    
    for a in nodes:
        neighbors_a = adj[a]
        # Only consider neighbors greater than a to maintain a < b < c
        candidates_b = [x for x in neighbors_a if x > a]
        candidates_b.sort()
        for b in candidates_b:
            # Now look for c such that c > b, c connected to both a and b
            neighbors_b = adj[b]
            candidates_c = [x for x in neighbors_b if x > b]
            candidates_c.sort()
            for c in candidates_c:
                if c in neighbors_a:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()
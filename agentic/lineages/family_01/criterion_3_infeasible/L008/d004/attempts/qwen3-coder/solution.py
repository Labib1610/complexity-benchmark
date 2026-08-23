import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    edges = []
    adj = [set() for _ in range(n+1)]
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # For each node, we'll store its neighbors
    # We want to find a triangle (clique of size 3) in the graph
    
    # To minimize the hazard score a*1e8 + b*1e4 + c, with a<b<c,
    # we should iterate through possible (a,b,c) in lexicographical order.
    # That means iterate a from 1 to n,
    #   for each a, iterate b from a+1 to n,
    #     for each b, iterate c from b+1 to n,
    #       and check if (a,b), (b,c), (a,c) are all edges.
    
    # However, checking all triplets would be too slow (O(n^3)).
    # Instead, for each edge (u,v), we look for a third node w such that
    # (u,w) and (v,w) are also edges. This makes it O(m*n) in worst case,
    # but much faster in practice since m << n^2.
    
    # Let's build a better adjacency structure
    # We'll go through each edge and see if we can form a triangle
    
    # To ensure we get the minimal in terms of hazard score,
    # we should process edges in a way that ensures we check smaller
    # indices first.
    
    # Sort the edges so that we process them in a consistent order
    sorted_edges = []
    for u, v in edges:
        if u > v:
            u, v = v, u
        sorted_edges.append((u, v))
    sorted_edges.sort()
    
    # For each edge (u,v), we look for a node w such that
    # w is connected to both u and v, and u < v < w to maintain order
    
    best = None
    min_score = float('inf')
    
    for u, v in sorted_edges:
        if u >= v:
            continue
        # Get common neighbors of u and v that are > v
        for w in adj[u]:
            if w > v and w in adj[v]:
                # Found a triangle u < v < w
                score = u * (10**8) + v * (10**4) + w
                if score < min_score:
                    min_score = score
                    best = (u, v, w)
    
    if best:
        print(best[0], best[1], best[2])
    else:
        # Fallback - shouldn't happen per problem statement
        # But let's try another approach just in case
        # Brute force with early termination might work given constraints
        found = False
        for a in range(1, n+1):
            if found:
                break
            for b in range(a+1, n+1):
                if found:
                    break
                # Check if a and b are connected
                if b not in adj[a]:
                    continue
                for c in range(b+1, n+1):
                    # Check if (a,c) and (b,c) exist
                    if c in adj[a] and c in adj[b]:
                        print(a, b, c)
                        found = True
                        break

if __name__ == "__main__":
    main()
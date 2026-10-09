import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # For each node, create a sorted list of its neighbors
    neighbors = [None] * (n + 1)
    for i in range(1, n + 1):
        neighbors[i] = sorted(adj[i])
    
    # We want the lexicographically smallest triangle
    # So we iterate through all edges and for each edge (u,v) with u<v,
    # we look for a third node w such that w > v and (u,w) and (v,w) exist
    # Since we want the smallest such triple, we process edges in order
    
    for u in range(1, n + 1):
        # For each neighbor v of u where v > u
        for i in range(len(neighbors[u])):
            v = neighbors[u][i]
            if v <= u:
                continue
            # Now we look for w in neighbors of both u and v, with w > v
            # To do this efficiently, we intersect neighbors[u][i+1:] and neighbors[v]
            # But since both lists are sorted, we can do a two-pointer approach
            
            nu_list = neighbors[u][i+1:]  # Neighbors of u that are > v
            nv_list = neighbors[v]        # All neighbors of v
            
            p1 = 0
            p2 = 0
            while p1 < len(nu_list) and p2 < len(nv_list):
                w1 = nu_list[p1]
                w2 = nv_list[p2]
                if w1 == w2:
                    # Found a triangle: u < v < w1
                    print(u, v, w1)
                    return
                elif w1 < w2:
                    p1 += 1
                else:
                    p2 += 1
    # The problem guarantees a solution exists, so we will always return before here

if __name__ == "__main__":
    main()
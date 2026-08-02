import sys

def find_lexicographically_smallest_triplet():
    n, m = map(int, input().split())
    
    # Create an adjacency list for the graph of interfering pairs
    interference_graph = {i: set() for i in range(1, n+1)}
    
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        interference_graph[u].add(v)
    
    # Iterate over all possible triplets (a, b, c) with a < b < c
    for a in range(1, n + 1):
        for b in interference_graph[a]:
            if b > a:
                for c in interference_graph[a]:
                    if c > b and c in interference_graph[b]:
                        print(a, b, c)
                        return

# Read input and solve the problem
find_lexicographically_smallest_triplet()
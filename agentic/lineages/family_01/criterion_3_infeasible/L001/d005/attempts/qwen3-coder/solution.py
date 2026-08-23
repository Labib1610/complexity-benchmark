import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    index = 2
    inert_pairs = set()
    adj = defaultdict(set)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        index += 2
        if u > v:
            u, v = v, u
        inert_pairs.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert adjacency lists to sorted lists for consistent iteration
    for u in adj:
        adj[u] = sorted(adj[u])
    
    # Iterate through all combinations (a,b,c) with a < b < c
    # Since we want lexicographically smallest, we iterate a from 1 to n,
    # for each a, b from neighbors of a and b > a,
    # for each such b, c from neighbors of both a and b, with c > b.
    
    for a in range(1, n+1):
        if a not in adj:
            continue
        for b in adj[a]:
            if b <= a:
                continue
            # Now find c such that (a,c) and (b,c) are both inert
            # c must be in both adj[a] and adj[b], and c > b
            common_neighbors = []
            # Use two pointers to find intersection of adj[a] and adj[b]
            i, j = 0, 0
            list_a = adj[a]
            list_b = adj[b]
            while i < len(list_a) and j < len(list_b):
                ca = list_a[i]
                cb = list_b[j]
                if ca == cb:
                    if ca > b:
                        print(a, b, ca)
                        return
                    i += 1
                    j += 1
                elif ca < cb:
                    i += 1
                else:
                    j += 1
    # As per problem statement, at least one solution exists, so we will find it

if __name__ == "__main__":
    main()
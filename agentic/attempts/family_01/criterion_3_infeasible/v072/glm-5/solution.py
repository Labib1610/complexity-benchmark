import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    
    adj = [[] for _ in range(n+1)]
    # Using a set for O(1) lookups
    edge_set = [set() for _ in range(n+1)]
    
    for _ in range(m):
        u = int(input[ptr])
        v = int(input[ptr+1])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
        edge_set[u].add(v)
        edge_set[v].add(u)
    
    # Sort adjacency lists for each node to process in order
    for i in range(1, n+1):
        adj[i].sort()
    
    # Iterate a from 1 to n
    for a in range(1, n+1):
        # Iterate b in adj[a] where b > a
        for b in adj[a]:
            if b <= a:
                continue
            # Now check for c in adj[b] where c > b and c is in adj[a]
            # Since adj[b] is sorted, we can iterate in order
            for c in adj[b]:
                if c <= b:
                    continue
                if c in edge_set[a]:
                    print(a, b, c)
                    return
    # Shouldn't reach here as per problem statement
    print(-1, -1, -1)

solve()
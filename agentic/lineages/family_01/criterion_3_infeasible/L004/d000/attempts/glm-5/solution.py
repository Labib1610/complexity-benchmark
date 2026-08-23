import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    n, m = map(int, input[ptr:ptr+2])
    ptr +=2
    
    adj = [set() for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input[ptr:ptr+2])
        ptr +=2
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate through each node a in order
    for a in range(1, n+1):
        neighbors = sorted(adj[a])
        # Check all pairs of neighbors b and c where b < c
        len_neighbors = len(neighbors)
        for i in range(len_neighbors):
            b = neighbors[i]
            if b < a:
                continue  # to ensure a < b < c, but since a is the smallest, we proceed
            for j in range(i+1, len_neighbors):
                c = neighbors[j]
                if c < a:
                    continue
                if b in adj[c]:
                    # Found the triangle a, b, c
                    # Ensure a < b < c
                    x, y, z = sorted([a, b, c])
                    print(x, y, z)
                    return
    # Shouldn't reach here as per problem statement
    print(-1, -1, -1)

solve()
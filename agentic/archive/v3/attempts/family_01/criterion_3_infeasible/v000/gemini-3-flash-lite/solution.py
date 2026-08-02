import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        if u > v:
            u, v = v, u
        adj[u].add(v)
        idx += 2
        
    # To find the lexicographically smallest triple (a, b, c)
    # where a < b < c and (a, b), (a, c), (b, c) are edges.
    # Iterate a from 1 to n-2
    for a in range(1, n - 1):
        neighbors_a = sorted(list(adj[a]))
        # Need at least two neighbors for a to form a triangle
        if len(neighbors_a) < 2:
            continue
            
        # Iterate b from the neighbors of a
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            
            # Now we need c > b such that c is in neighbors_a and c is in adj[b]
            # Since we want the lexicographically smallest, we check c in order
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

solve()
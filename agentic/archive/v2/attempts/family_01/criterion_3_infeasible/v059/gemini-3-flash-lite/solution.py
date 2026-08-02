import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        edges.append((u, v))
    
    # Sort edges to help find lexicographically smallest triple (a, b, c)
    # where a < b < c.
    # We want to iterate through 'a', then 'b', then check if 'c' exists.
    # Sorting edges by u then v is helpful.
    edges.sort()
    
    # To find the lexicographically smallest (a, b, c), we iterate through
    # every edge (a, b) and check if there exists a common neighbor c > b.
    # Since we want the smallest (a, b, c), we can iterate through possible 'a's
    # and for each 'a', iterate through neighbors 'b' in increasing order.
    
    # Pre-sort neighbors for each node to ensure we check 'c' in order
    for i in range(1, n + 1):
        adj[i] = sorted(list(adj[i]))
        
    # Iterate through each node 'a' as the smallest element
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        # Iterate through each neighbor 'b' of 'a'
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # We need a 'c' such that b < c and c is a neighbor of both a and b.
            # Since adj[a] is sorted, we check elements after 'b'.
            # To optimize, we check the intersection of neighbors_a and neighbors_b.
            
            # Optimization: only check neighbors of 'b' that are also in 'neighbors_a'
            # and are greater than 'b'.
            neighbors_b = adj[b]
            
            # Use two pointers or set intersection to find common neighbors
            ptr_a = i + 1
            ptr_b = 0
            while ptr_a < len(neighbors_a) and ptr_b < len(neighbors_b):
                val_a = neighbors_a[ptr_a]
                val_b = neighbors_b[ptr_b]
                
                if val_a == val_b:
                    print(f"{a} {b} {val_a}")
                    return
                elif val_a < val_b:
                    ptr_a += 1
                else:
                    ptr_b += 1

solve()
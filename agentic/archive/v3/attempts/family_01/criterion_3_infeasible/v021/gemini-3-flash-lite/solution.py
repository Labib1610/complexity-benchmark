import sys

def solve():
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
        v = int(input_data[idx + 1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        edges.append((u, v))
    
    # Sort edges to help find lexicographically smallest
    edges.sort()
    
    # Iterate through each edge (a, b) and check for a common neighbor c
    # To ensure lexicographical order, we iterate through edges (a, b)
    # and then through potential c > b.
    
    # Pre-sort neighbors for each node to check intersection efficiently
    adj_list = [sorted(list(s)) for s in adj]
    
    for a in range(1, n + 1):
        for b in adj_list[a]:
            # We have an edge (a, b) where a < b.
            # We look for c > b such that (a, c) and (b, c) exist.
            # This means c must be in adj[a] and adj[b].
            
            # Intersection of two sorted lists:
            list_a = adj_list[a]
            list_b = adj_list[b]
            
            # We only care about c > b.
            # Since both lists are sorted, find elements > b in both.
            ptr_a = 0
            while ptr_a < len(list_a) and list_a[ptr_a] <= b:
                ptr_a += 1
            
            ptr_b = 0
            while ptr_b < len(list_b) and list_b[ptr_b] <= b:
                ptr_b += 1
                
            # Now find the smallest common element
            while ptr_a < len(list_a) and ptr_b < len(list_b):
                if list_a[ptr_a] == list_b[ptr_b]:
                    print(f"{a} {b} {list_a[ptr_a]}")
                    return
                elif list_a[ptr_a] < list_b[ptr_b]:
                    ptr_a += 1
                else:
                    ptr_b += 1

solve()
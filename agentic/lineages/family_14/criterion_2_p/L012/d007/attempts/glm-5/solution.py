import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    t = int(next(it))
    
    primary = set()
    for _ in range(t):
        primary.add(int(next(it)))
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    primary_count = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i in primary:
            primary_count[i] = 1
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        primary_count[rx] += primary_count[ry]
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True
    
    total_cost = 0
    # Process edges in order of increasing weight
    for u, v, w in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            # Check if merging would connect all primary elements
            if primary_count[ru] + primary_count[rv] == t:
                total_cost += w
                # Merge all remaining edges to complete the MST
                # But we need to continue processing to merge other components
                # Actually, we should merge this edge and continue
                # The answer is the weight of this edge plus all previous edges
                # that were part of building up to this point
                # Wait, we need to reconsider the algorithm
                # The correct approach: when we first connect all primary elements,
                # the answer is the sum of all edges processed so far (including this one)
                # that form the MST up to this point
                # But we've been adding edges to total_cost only when they merge components
                # So total_cost already has the correct sum
                # We need to output total_cost and return
                print(total_cost)
                return
            else:
                # Merge the components
                union(u, v)
                total_cost += w
    
    # If we reach here, all primary elements are already connected
    # This shouldn't happen if t > 1 and graph is connected
    print(total_cost)

solve()
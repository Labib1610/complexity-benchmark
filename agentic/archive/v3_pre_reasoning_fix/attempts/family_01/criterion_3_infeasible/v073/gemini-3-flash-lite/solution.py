import sys

def solve():
    # Read n and m
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
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find the lexicographically smallest triple (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b from a+1 to n-1
    # Check if a and b are connected. If so, check for a common neighbor c > b.
    
    # Sort neighbors to ensure we find the smallest c efficiently
    adj_list = [sorted(list(s)) for s in adj]
    
    # Use bitsets or boolean arrays for O(1) adjacency checks
    is_connected = [[False] * (n + 1) for _ in range(n + 1)]
    for u in range(1, n + 1):
        for v in adj[u]:
            is_connected[u][v] = True
            
    for a in range(1, n - 1):
        # We only care about b that are connected to a
        neighbors_a = adj_list[a]
        for b in neighbors_a:
            if b <= a:
                continue
            
            # Now find the smallest c > b such that c is connected to a AND b
            # We intersect the neighbors of a and b
            # Since neighbors are sorted, we can iterate through them
            neighbors_b = adj[b]
            for c in neighbors_a:
                if c <= b:
                    continue
                if c in neighbors_b:
                    print(f"{a} {b} {c}")
                    return

solve()
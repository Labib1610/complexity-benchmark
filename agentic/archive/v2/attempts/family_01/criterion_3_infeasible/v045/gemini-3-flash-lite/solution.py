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
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    #   Iterate b from a+1 to n-1
    #     If b is connected to a:
    #       Check if there exists c > b such that c is in adj[a] and adj[b]
    
    # Pre-sort adjacency lists to make intersection faster or checking easier
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Only consider neighbors b > a
        neighbors_a = [x for x in sorted_adj[a] if x > a]
        for b in neighbors_a:
            # We need a c such that b < c and c is in adj[a] and adj[b]
            # Since we want the lexicographically smallest, we check if any
            # such c exists. If we find one, the first one we find is the smallest c.
            
            # Intersection of adj[a] and adj[b]
            # Using sets for O(1) lookup
            set_a = adj[a]
            set_b = adj[b]
            
            # Iterate through the smaller set to find common neighbors
            if len(set_a) < len(set_b):
                common = sorted([x for x in set_a if x > b and x in set_b])
            else:
                common = sorted([x for x in set_b if x > b and x in set_a])
            
            if common:
                print(f"{a} {b} {common[0]}")
                return

if __name__ == '__main__':
    solve()
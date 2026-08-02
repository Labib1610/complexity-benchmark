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
        
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    #   Iterate b from a+1 to n-1
    #     If a and b are connected:
    #       Check for common neighbors c > b
    
    # Sort neighbors to make intersection check efficient and ordered
    adj_list = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Only consider neighbors b > a
        neighbors_a = [x for x in adj_list[a] if x > a]
        for b in neighbors_a:
            # We need a c such that c > b, c is in adj[a] and c is in adj[b]
            # Since neighbors_a is sorted, we can intersect
            # To be efficient, convert adj[b] to a set for O(1) lookup
            # Actually, we can just iterate through sorted neighbors of a
            # that are > b
            
            # Using set for faster lookup of c in adj[b]
            adj_b_set = adj[b]
            
            for c in neighbors_a:
                if c > b:
                    if c in adj_b_set:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()
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
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b from a+1 to n-1
    # Check if a and b are connected.
    # If connected, check if there exists c > b such that c is in adj[a] and adj[b].
    
    # Pre-sort adjacency lists to make intersection faster
    adj_list = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Sort neighbors to ensure we check in order
        neighbors_a = adj_list[a]
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            if b <= a:
                continue
            
            # Now we have a < b. Find smallest c > b such that c in adj[a] and c in adj[b]
            # Use intersection of sorted lists
            neighbors_b = adj_list[b]
            
            idx_a = 0
            idx_b = 0
            len_a = len(neighbors_a)
            len_b = len(neighbors_b)
            
            while idx_a < len_a and idx_b < len_b:
                val_a = neighbors_a[idx_a]
                val_b = neighbors_b[idx_b]
                
                if val_a == val_b:
                    if val_a > b:
                        print(f"{a} {b} {val_a}")
                        return
                    idx_a += 1
                    idx_b += 1
                elif val_a < val_b:
                    idx_a += 1
                else:
                    idx_b += 1

solve()
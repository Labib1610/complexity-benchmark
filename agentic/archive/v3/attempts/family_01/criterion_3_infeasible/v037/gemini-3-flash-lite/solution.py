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
    #   Iterate b from a+1 to n-1
    #     If b is connected to a:
    #       Check if there exists c > b such that c is in adj[a] and adj[b]
    
    # Pre-sort adjacency lists to make intersection faster or use set lookup
    # Convert sets to sorted lists to iterate c efficiently
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Only consider b > a
        neighbors_a = [x for x in sorted_adj[a] if x > a]
        for b in neighbors_a:
            # We need c > b such that c is in adj[a] and adj[b]
            # Find intersection of neighbors_a (filtered > b) and neighbors_b (filtered > b)
            # Since sorted_adj is sorted, we can use two pointers
            neighbors_b = [x for x in sorted_adj[b] if x > b]
            
            ptr_a = 0
            ptr_b = 0
            while ptr_a < len(neighbors_a) and ptr_b < len(neighbors_b):
                val_a = neighbors_a[ptr_a]
                val_b = neighbors_b[ptr_b]
                
                if val_a <= b:
                    ptr_a += 1
                    continue
                if val_b <= b:
                    ptr_b += 1
                    continue
                    
                if val_a == val_b:
                    print(f"{a} {b} {val_a}")
                    return
                elif val_a < val_b:
                    ptr_a += 1
                else:
                    ptr_b += 1

if __name__ == '__main__':
    solve()
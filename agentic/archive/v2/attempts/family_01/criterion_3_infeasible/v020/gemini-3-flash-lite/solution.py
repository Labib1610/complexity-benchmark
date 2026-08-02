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
    # Check if b is in adj[a]
    # If yes, check if there exists c > b such that c is in both adj[a] and adj[b]
    
    # Pre-sort neighbors to speed up intersection
    adj_list = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Only consider neighbors b > a
        neighbors_a = [x for x in adj_list[a] if x > a]
        for b in neighbors_a:
            # Need to find smallest c > b such that c in adj[a] and c in adj[b]
            # Intersection of two sorted lists
            idx_a = 0
            idx_b = 0
            na = adj_list[a]
            nb = adj_list[b]
            
            # Binary search or two pointers to find intersection > b
            # Two pointers is efficient here
            while idx_a < len(na) and idx_b < len(nb):
                val_a = na[idx_a]
                val_b = nb[idx_b]
                
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

if __name__ == '__main__':
    solve()
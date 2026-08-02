import sys

def solve():
    # Use fast I/O
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
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
        
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b from a+1 to n-1
    # Check if there exists c > b such that c is in adj[a] and adj[b]
    
    # Sort adj lists to potentially optimize, though set intersection is O(min(deg))
    adj_list = [sorted(list(s)) for s in adj]
    
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        sorted_neighbors_a = sorted([x for x in neighbors_a if x > a])
        
        for b in sorted_neighbors_a:
            # We need to find c > b such that c is in both neighbors_a and neighbors_b
            # Since we want the smallest a, then smallest b, then smallest c,
            # we just need the first c that satisfies the condition.
            neighbors_b = adj[b]
            
            # Intersection of neighbors_a and neighbors_b
            # We can iterate through the smaller set
            if len(neighbors_a) < len(neighbors_b):
                candidates = neighbors_a
            else:
                candidates = neighbors_b
            
            best_c = float('inf')
            found = False
            for c in candidates:
                if c > b:
                    if c in neighbors_a and c in neighbors_b:
                        if c < best_c:
                            best_c = c
                            found = True
            
            if found:
                print(f"{a} {b} {best_c}")
                return

if __name__ == '__main__':
    solve()
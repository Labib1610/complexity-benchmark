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
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # Convert sets to sorted lists for faster intersection if needed,
    # but set intersection is generally efficient for this constraint.
    # We want to find the lexicographically smallest (a, b, c).
    # Iterate a from 1 to n, b from a+1 to n, c from b+1 to n.
    
    # Pre-sort adjacency lists to help iteration
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Candidates for b are neighbors of a
        neighbors_a = sorted_adj[a]
        for b in neighbors_a:
            if b <= a:
                continue
            
            # Candidates for c are neighbors of both a and b
            # We need c > b
            # Intersection of neighbors_a and neighbors_b
            # Since we want the smallest, we look for the smallest c > b
            
            # Use the fact that neighbors_a and neighbors_b are sorted
            # to find the smallest common neighbor c > b
            set_b = adj[b]
            for c in neighbors_a:
                if c > b and c in set_b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()
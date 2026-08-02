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
        
    # To find the lexicographically smallest (a, b, c),
    # we iterate a from 1 to n-2,
    # b from a+1 to n-1,
    # and check if there exists c > b such that c is in adj[a] and adj[b].
    
    # Sorting adjacency lists to potentially speed up finding c
    adj_sorted = [sorted(list(s)) for s in adj]
    
    for a in range(1, n - 1):
        # Only consider neighbors b > a
        neighbors_a = [x for x in adj_sorted[a] if x > a]
        for b in neighbors_a:
            # We need a c such that c > b, c in adj[a], and c in adj[b]
            # Since adj[a] is sorted, we can intersect efficiently
            # However, for n=2000, bitsets or simple set intersection are fast enough
            
            # Use set for O(1) lookup
            # We already have adj[a] as a set, let's use that
            # To optimize, iterate over the smaller adjacency list
            if len(adj[a]) < len(adj[b]):
                small = adj[a]
                large = adj[b]
            else:
                small = adj[b]
                large = adj[a]
                
            for c in small:
                if c > b and c in large:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()
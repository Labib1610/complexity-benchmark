import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # Convert sets to sorted lists to iterate in order
    adj_list = [sorted(list(adj[i])) for i in range(n + 1)]
    
    # We want the lexicographically smallest (a, b, c) with a < b < c
    # Iterate a from 1 to n
    for a in range(1, n + 1):
        # Candidates for b must be greater than a
        neighbors_a = [x for x in adj_list[a] if x > a]
        for b in neighbors_a:
            # Candidates for c must be greater than b
            # c must be in adj[a] and adj[b]
            # Since adj_list[a] and adj_list[b] are sorted, 
            # we can find intersection efficiently
            
            # Optimization: only check neighbors of b that are > b and also in adj[a]
            for c in adj_list[b]:
                if c > b:
                    if c in adj[a]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()
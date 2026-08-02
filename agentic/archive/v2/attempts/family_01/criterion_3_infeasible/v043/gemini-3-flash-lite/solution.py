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
        
    # To find the lexicographically smallest triple (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b from a+1 to n-1
    # Check if b is connected to a
    # Iterate c from b+1 to n
    # Check if c is connected to a and b
    
    # Optimization: Convert adj sets to sorted lists for faster iteration
    adj_list = [sorted(list(s)) for s in adj]
    
    for a in range(1, n - 1):
        # Candidates for b must be connected to a and b > a
        neighbors_a = [x for x in adj_list[a] if x > a]
        if not neighbors_a:
            continue
        
        for b in neighbors_a:
            # Candidates for c must be connected to a AND b, and c > b
            # We intersect the neighbors of a and b
            neighbors_b = set(adj[b])
            for c in adj_list[a]:
                if c > b and c in neighbors_b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()
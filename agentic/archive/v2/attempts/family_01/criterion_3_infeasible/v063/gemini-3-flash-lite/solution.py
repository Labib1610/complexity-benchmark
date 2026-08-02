import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency sets for O(1) lookups
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # Convert sets to sorted lists for efficient iteration
    adj_list = [sorted(list(adj[i])) for i in range(n + 1)]
    
    # We want the lexicographically smallest (a, b, c) with a < b < c.
    # Iterate a from 1 to n-2
    for a in range(1, n - 1):
        # Iterate b from a+1 to n-1
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # Now we need to find if there exists c > b such that c is in adj[a] and adj[b]
            # Since adj_list[a] is sorted, we can intersect efficiently
            # However, with n=2000, simply checking intersection is fine.
            # We want the smallest c, so we iterate through neighbors of a
            for c in adj_list[a]:
                if c <= b:
                    continue
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()
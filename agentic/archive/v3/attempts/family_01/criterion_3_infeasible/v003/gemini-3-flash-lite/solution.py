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
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n
    # Iterate b in sorted order of neighbors of a such that b > a
    # Iterate c in sorted order of neighbors of a and b such that c > b
    
    # Pre-sort neighbors for lexicographical order
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        neighbors_a = sorted_adj[a]
        # Filter neighbors > a
        b_candidates = [b for b in neighbors_a if b > a]
        for b in b_candidates:
            # We need c > b such that c is in adj[a] and c is in adj[b]
            # Since adj[a] and adj[b] are sorted, we can find intersection efficiently
            # However, with n=2000, set intersection is fast enough
            common = adj[a].intersection(adj[b])
            c_candidates = [c for c in common if c > b]
            if c_candidates:
                print(f"{a} {b} {min(c_candidates)}")
                return

if __name__ == '__main__':
    solve()
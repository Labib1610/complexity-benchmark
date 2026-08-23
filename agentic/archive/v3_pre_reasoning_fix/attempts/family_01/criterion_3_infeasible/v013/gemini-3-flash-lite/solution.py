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
        
    # To find lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b from a+1 to n-1
    # Check if there exists c > b such that c is in adj[a] and adj[b]
    
    # Pre-sort adjacency lists to make intersection faster or use set lookup
    # Since n is up to 2000, O(n^3) might be slow, but set intersection is fast.
    # Actually, iterate a, then b, then check if there is any c > b in (adj[a] & adj[b])
    
    for a in range(1, n - 1):
        adj_a = adj[a]
        # Candidates for b are neighbors of a such that b > a
        b_candidates = sorted([b for b in adj_a if b > a])
        for b in b_candidates:
            adj_b = adj[b]
            # We need smallest c > b such that c in adj_a and c in adj_b
            # Intersection of adj_a and adj_b
            common = adj_a.intersection(adj_b)
            # Find smallest c in common such that c > b
            best_c = float('inf')
            found = False
            for c in common:
                if c > b:
                    if c < best_c:
                        best_c = c
                        found = True
            
            if found:
                print(f"{a} {b} {best_c}")
                return

if __name__ == '__main__':
    solve()
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for lexicographic order processing
    adj_lists = [sorted(s) for s in adj]
    
    # Iterate to find the lexicographically smallest triangle
    for a in range(1, n + 1):
        neighbors_a = adj_lists[a]
        # Since we need a < b < c, we only consider neighbors b > a
        # Use binary search to find the start of valid neighbors
        # Manual pointer scan is efficient enough as lists are sorted
        start_index = 0
        len_na = len(neighbors_a)
        while start_index < len_na and neighbors_a[start_index] <= a:
            start_index += 1
        
        # Iterate through all valid b
        for i in range(start_index, len_na):
            b = neighbors_a[i]
            # For each b, iterate through valid c
            for j in range(i + 1, len_na):
                c = neighbors_a[j]
                # Check if edge (b, c) exists
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()
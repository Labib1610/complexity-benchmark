import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate to find lexicographically smallest triangle
    for a in range(1, n - 1):
        neighbors_a = adj[a]
        # We need b > a and c > b
        # Convert to list and sort to iterate in order
        # Optimization: only consider neighbors > a
        sorted_neighbors = sorted([x for x in neighbors_a if x > a])
        
        len_nb = len(sorted_neighbors)
        for i in range(len_nb):
            b = sorted_neighbors[i]
            # c must be > b and in neighbors of both a and b
            # Check remaining neighbors of a (which are > b due to sorting)
            for j in range(i + 1, len_nb):
                c_candidate = sorted_neighbors[j]
                if c_candidate in adj[b]:
                    print(a, b, c_candidate)
                    return

if __name__ == '__main__':
    solve()
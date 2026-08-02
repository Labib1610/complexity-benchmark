import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
        idx += 2
        
    # To find lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b from a+1 to n-1
    # Check if there exists c > b such that c is in adj[a] and adj[b]
    
    # Sort adj lists to potentially speed up intersection
    for i in range(1, n + 1):
        adj[i] = sorted(list(adj[i]))
    
    # Convert to sets for O(1) lookup
    adj_sets = [set(adj[i]) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Only check a if it has at least 2 neighbors
        if len(adj[a]) < 2:
            continue
            
        sorted_neighbors_a = adj[a]
        for i in range(len(sorted_neighbors_a)):
            b = sorted_neighbors_a[i]
            if b <= a:
                continue
            
            # Now we need smallest c > b such that c in adj[a] and c in adj[b]
            # Since sorted_neighbors_a is sorted, we can iterate through it
            # starting from index i+1
            for j in range(i + 1, len(sorted_neighbors_a)):
                c = sorted_neighbors_a[j]
                if c > b and c in adj_sets[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()
import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use an adjacency set or bitset for fast lookup
    # Since n <= 2000, an array of sets or a bitset is efficient.
    # Using adjacency lists and sorting them for iteration, 
    # combined with a boolean matrix for O(1) checking.
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    #   Iterate b in adj[a] where b > a
    #     Iterate c in adj[a] where c > b
    #       Check if c in adj[b]
    
    # Convert adjacency sets to sorted lists to help find smallest lexicographical triplet
    adj_sorted = [sorted(list(s)) for s in adj]
    
    for a in range(1, n - 1):
        neighbors_a = adj_sorted[a]
        # Filter neighbors > a
        nodes_a = [x for x in neighbors_a if x > a]
        
        for i in range(len(nodes_a)):
            b = nodes_a[i]
            # Optimization: if we already found a triplet with a smaller a or b,
            # we could stop, but here we just need the smallest.
            # Check neighbors of b that are also in nodes_a[i+1:]
            for j in range(i + 1, len(nodes_a)):
                c = nodes_a[j]
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()
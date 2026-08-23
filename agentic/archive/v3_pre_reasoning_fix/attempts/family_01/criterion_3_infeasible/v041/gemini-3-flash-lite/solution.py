import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use an adjacency list of sets for fast lookup or adjacency matrix if memory allows
    # Given n <= 2000, n*n adjacency matrix is 4 million entries, fits in memory.
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
    # Iterate b from a+1 to n-1
    # Check if b is in adj[a]
    # If so, check if there is any c > b such that c is in both adj[a] and adj[b]
    
    # Sort adjacency lists to potentially speed up intersection
    for i in range(1, n + 1):
        adj[i] = sorted(list(adj[i]))
    
    # Convert back to sets for O(1) average lookup
    adj_sets = [set(adj[i]) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Only consider b > a
        neighbors_a = [x for x in adj[a] if x > a]
        for b in neighbors_a:
            # We need c > b such that c in adj[a] and c in adj[b]
            # Since neighbors_a and neighbors_b are sorted, we can find intersection
            # or just iterate through smaller set
            neighbors_b = adj[b]
            for c in neighbors_b:
                if c > b:
                    if c in adj_sets[a]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == '__main__':
    solve()
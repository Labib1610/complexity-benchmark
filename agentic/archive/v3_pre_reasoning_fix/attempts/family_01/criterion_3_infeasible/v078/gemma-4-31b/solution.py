import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list to store neighbors
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix/set for O(1) lookup. 
    # Given n=2000, a bitset or a boolean matrix is feasible.
    # In Python, a list of sets or a list of lists (bitmask) could work.
    # Using a list of sets for clarity and efficiency.
    adj_set = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        adj_set[u].add(v)
        adj_set[v].add(u)
        
    # To find the lexicographically smallest triple (a, b, c) with a < b < c:
    # We iterate a from 1 to n.
    # For a fixed a, we look for pairs (b, c) such that a < b < c and both b, c are neighbors of a.
    # To find the smallest b, we iterate through neighbors of a that are > a in increasing order.
    
    for a in range(1, n + 1):
        # Get neighbors of a that are greater than a, sorted
        neighbors_a = sorted([v for v in adj[a] if v > a])
        
        # Check all pairs (b, c) from these neighbors
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                # Since neighbors_a is sorted, b < c is guaranteed.
                # We only need to check if b and c are connected.
                if c in adj_set[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
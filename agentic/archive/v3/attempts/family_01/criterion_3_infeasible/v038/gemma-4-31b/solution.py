import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list using sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    # Adjacency list using lists for iteration
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        adj_list[u].append(v)
        adj_list[v].append(u)

    # To find the lexicographically smallest triplet (a, b, c) with a < b < c:
    # We iterate a from 1 to n, b from a+1 to n, and check if there is a c > b
    # such that (a, c) and (b, c) are edges.
    
    # To optimize, we can iterate through all a from 1 to n.
    # For a fixed a, we only consider neighbors of a that are greater than a.
    # Let these neighbors be S_a = {v | v > a and (a, v) is an edge}.
    # We then look for two elements b, c in S_a such that b < c and (b, c) is an edge.
    # To get the lexicographically smallest, we sort S_a.
    
    for a in range(1, n + 1):
        # Get all neighbors of a that are > a, sorted ascending
        neighbors_a = sorted([v for v in adj_list[a] if v > a])
        
        # Now we need to find the smallest b in neighbors_a such that there is a c in neighbors_a
        # where c > b and (b, c) is an edge.
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Check all c in neighbors_a where c > b
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                # Check if b and c are connected
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
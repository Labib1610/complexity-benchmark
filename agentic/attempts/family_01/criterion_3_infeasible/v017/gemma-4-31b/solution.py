import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    # To optimize the search, we maintain adjacency lists as sorted lists
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        adj_list[u].append(v)
        adj_list[v].append(u)
        idx += 2
        
    for i in range(1, n + 1):
        adj_list[i].sort()

    # We need the lexicographically smallest triple (a, b, c) where a < b < c.
    # We iterate through potential 'a' from 1 to n.
    # For a fixed 'a', we look for 'b' and 'c' from its neighbors that are > a.
    for a in range(1, n + 1):
        # Neighbors of a that are greater than a
        neighbors_a = [v for v in adj_list[a] if v > a]
        
        # We want the smallest b, then smallest c.
        # Iterate through pairs (b, c) from neighbors_a.
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # We need c > b and c to be a neighbor of both a and b.
            # Since neighbors_a is sorted, we only check indices j > i.
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                # Check if b and c are connected
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
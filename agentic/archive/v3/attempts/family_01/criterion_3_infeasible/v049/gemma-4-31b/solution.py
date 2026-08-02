import sys

def solve():
    # Use fast I/O
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
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))

    # To find the lexicographically smallest (a, b, c) where a < b < c:
    # We iterate a from 1 to n.
    # For a fixed a, we look for b and c such that a < b < c and (a,b), (a,c), (b,c) are edges.
    # To minimize (a, b, c), we want the smallest a, then the smallest b, then the smallest c.
    
    # Pre-sort the adjacency lists to iterate in increasing order.
    # However, we only care about neighbors > current node.
    sorted_adj = [sorted([v for v in adj[u] if v > u]) for u in range(n + 1)]

    for a in range(1, n + 1):
        neighbors_of_a = sorted_adj[a]
        # We need to find two nodes b, c in neighbors_of_a such that b < c and (b, c) is an edge.
        # To minimize b, we iterate through neighbors_of_a.
        for i in range(len(neighbors_of_a)):
            b = neighbors_of_a[i]
            # To minimize c, we iterate through the rest of neighbors_of_a.
            for j in range(i + 1, len(neighbors_of_a)):
                c = neighbors_of_a[j]
                # Check if b and c are connected.
                # Since we only need to check if c is in adj[b], and adj[b] is a set, this is O(1).
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
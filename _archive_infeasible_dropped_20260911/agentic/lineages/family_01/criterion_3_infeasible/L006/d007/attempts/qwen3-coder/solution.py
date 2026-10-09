import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list for the graph
    adj = [set() for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].add(v)
        adj[v].add(u)
        index += 2

    # For each node, sort its neighbors for consistent processing
    for i in range(1, n + 1):
        adj[i] = sorted(adj[i])

    # Iterate through all combinations of a < b < c
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            # Check if a has access to b
            if b not in adj[a]:
                continue
            for c in range(b + 1, n + 1):
                # Check if a has access to c and b has access to c
                if c in adj[a] and c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    main()
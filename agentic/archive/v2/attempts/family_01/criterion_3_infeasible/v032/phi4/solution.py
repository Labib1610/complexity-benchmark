import sys

def find_smallest_triple(n, m, links):
    # Create adjacency list for graph representation
    adj = [set() for _ in range(n + 1)]
    
    # Populate the adjacency list with the given links
    for u, v in links:
        adj[u].add(v)
        adj[v].add(u)

    # Find the lexicographically smallest triangle
    for a in range(1, n + 1):
        neighbors_a = sorted(adj[a])
        for i, b in enumerate(neighbors_a):
            for c in neighbors_a[i + 1:]:
                if c in adj[b]:
                    return (a, b, c)

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    links = [(int(data[i]), int(data[i + 1])) for i in range(2, len(data), 2)]
    
    a, b, c = find_smallest_triple(n, m, links)
    print(a, b, c)
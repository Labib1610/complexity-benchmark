def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1
    
    # Initialize adjacency list with sets
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(input[idx])
        idx += 1
        v = int(input[idx])
        idx += 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Check each node's neighbors for a triangle
    for u in range(1, n + 1):
        sorted_neighbors = sorted(adj[u])
        len_neighbors = len(sorted_neighbors)
        for i in range(len_neighbors):
            for j in range(i + 1, len_neighbors):
                v = sorted_neighbors[i]
                w = sorted_neighbors[j]
                if w in adj[v]:
                    # Found a triangle, output sorted
                    res = sorted([u, v, w])
                    print(f"{res[0]} {res[1]} {res[2]}")
                    return

if __name__ == "__main__":
    main()
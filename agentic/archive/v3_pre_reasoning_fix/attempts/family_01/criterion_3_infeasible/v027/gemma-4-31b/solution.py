import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])HBS] = 2)
    
    # Adjacency list to store prohibited pairs
    # We only store neighbors with index > current index to simplify search
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix for O(1) lookup
    # Using a bitset/bytearray for memory efficiency and speed
    # n <= 2000, so n*n is 4 million, fits in memory
    matrix = [bytearray(n + 1) for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].append(v)
        matrix[u][v] = 1
        matrix[v][u] = 1

    # Sort adjacency lists to ensure we find the lexicographically smallest triple
    for i in range(1, n + 1):
        adj[i].sort()

    # We want the lexicographically smallest triple (a, b, c) with a < b < c.
    # We iterate through a from 1 to n, then b from adj[a], then c from adj[b].
    for a in range(1, n + 1):
        # Potential b's are neighbors of a that are greater than a
        neighbors_a = adj[a]
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Potential c's are neighbors of b that are greater than b
            # Since adj[b] is sorted, the first c we find that is also a neighbor of a
            # will give us the lexicographically smallest triple for this a and b.
            for c in adj[b]:
                if c > b:
                    if matrix[a][c]:
                        print(f"{a} {b} {c}")
                        return

if __name__ == "__main__":
    solve()
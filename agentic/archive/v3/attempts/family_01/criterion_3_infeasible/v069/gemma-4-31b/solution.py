import sys

def solve():
    # Read n and m from the first line
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency lists for graph representation
    adj = [[] for _ in range(n + 1)]
    # Use a set of tuples or a bitset-like structure for O(1) edge check
    # Given n=2000, a adjacency matrix (list of lists) is feasible and fast
    matrix = [[False] * (n + 1) for _ in range(n + 1)]
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
        matrix[u][v] = matrix[v][u] = True

    # Sort adjacency lists to ensure we check candidates in lexicographical order
    for i in range(1, n + 1):
        adj[i].sort()

    # To find the lexicographically smallest triple (a, b, c) with a < b < c:
    # We iterate a from 1 to n, then b from a+1 to n, then c from b+1 to n.
    # To optimize, we only iterate over actual neighbors.
    
    for a in range(1, n - 1):
        # Potential candidates for b and c must be neighbors of a and > a
        neighbors_a = [v for v in adj[a] if v > a]
        
        # We need to find the smallest b and c from neighbors_a such that matrix[b][c] is True
        # Since neighbors_a is sorted, we check pairs in lexicographical order
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                if matrix[b][c]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()
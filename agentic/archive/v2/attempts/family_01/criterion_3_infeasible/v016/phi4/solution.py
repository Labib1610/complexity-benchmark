import sys

def find_mutually_conflicting_triple():
    n, m = map(int, input().split())
    
    # Create an adjacency matrix for conflicts
    conflict_matrix = [[False] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        conflict_matrix[u][v] = True
        conflict_matrix[v][u] = True
    
    # Find the smallest lexicographical triple of mutually conflicting employees
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if not conflict_matrix[a][b]:
                continue
            for c in range(b + 1, n + 1):
                if conflict_matrix[a][c] and conflict_matrix[b][c]:
                    print(f"{a} {b} {c}")
                    return

find_mutually_conflicting_triple()
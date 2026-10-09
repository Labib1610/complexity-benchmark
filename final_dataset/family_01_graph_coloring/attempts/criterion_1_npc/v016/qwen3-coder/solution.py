import sys
from itertools import product

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, edges

def is_valid_coloring(n, edges, coloring):
    # Check that no two adjacent nodes have the same color
    for u, v in edges:
        if coloring[u] == coloring[v]:
            return False
    return True

def solve(n, edges):
    # Try all possible colorings with colors 1, 2, 3
    for coloring in product([1, 2, 3], repeat=n):
        if is_valid_coloring(n, edges, coloring):
            total = sum(coloring)
            if n <= total <= 3 * n:
                return True, list(coloring)
    return False, []

def main():
    n, edges = read_input()
    exists, coloring = solve(n, edges)
    if exists:
        print("YES")
        print(' '.join(map(str, coloring)))
    else:
        print("NO")

if __name__ == "__main__":
    main()
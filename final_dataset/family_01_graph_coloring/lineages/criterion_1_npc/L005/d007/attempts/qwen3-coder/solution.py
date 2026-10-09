import sys
from itertools import product

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, m, edges

def is_valid_coloring(n, edges, coloring):
    for u, v in edges:
        if coloring[u] == coloring[v]:
            return False
    return True

def solve(n, m, edges):
    # Try all possible 3-colorings
    for coloring in product([1, 2, 3], repeat=n):
        if is_valid_coloring(n, edges, coloring):
            return True, coloring
    return False, None

def main():
    n, m, edges = read_input()
    
    if m == 0:
        # No constraints, any valid coloring works
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    found, coloring = solve(n, m, edges)
    
    if found:
        print("YES")
        print(" ".join(map(str, coloring)))
    else:
        print("NO")

if __name__ == "__main__":
    main()
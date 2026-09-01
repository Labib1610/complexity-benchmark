import sys
from collections import defaultdict

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, edges

def is_valid_coloring(graph, n, coloring):
    for u, v in graph:
        if coloring[u] == coloring[v]:
            return False
    return True

def find_min_signature_coloring(n, edges):
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Try all possible colorings in lexicographic order
    # We want to minimize S = sum(f_i * 4^(n-i)) which means we want
    # the lexicographically smallest sequence when viewed from left to right
    
    def backtrack(index, coloring):
        if index == n:
            return coloring[:]
        
        # Try colors 1, 2, 3 in order
        for color in [1, 2, 3]:
            # Check if this color is valid with neighbors
            valid = True
            for neighbor in graph[index]:
                if neighbor < index and coloring[neighbor] == color:
                    valid = False
                    break
            
            if valid:
                coloring[index] = color
                result = backtrack(index + 1, coloring)
                if result is not None:
                    return result
        
        return None
    
    coloring = [0] * n
    return backtrack(0, coloring)

def main():
    n, edges = read_input()
    
    if n == 0:
        print("YES")
        return
    
    result = find_min_signature_coloring(n, edges)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
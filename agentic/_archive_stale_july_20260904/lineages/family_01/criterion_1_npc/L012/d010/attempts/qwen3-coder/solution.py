from collections import defaultdict
import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, m, edges

def is_valid_coloring(graph, n, coloring):
    for u in range(n):
        for v in graph[u]:
            if coloring[u] == coloring[v]:
                return False
    return True

def graph_coloring_possible(graph, n):
    # Check if the graph is 3-colorable using backtracking
    coloring = [-1] * n
    
    def is_safe(node, color):
        for neighbor in graph[node]:
            if coloring[neighbor] == color:
                return False
        return True
    
    def solve(node):
        if node == n:
            return True
        
        for color in [1, 2, 3]:
            if is_safe(node, color):
                coloring[node] = color
                if solve(node + 1):
                    return True
                coloring[node] = -1
        return False
    
    if solve(0):
        return True, coloring
    else:
        return False, []

def calculate_penalty(coloring, n):
    penalty = 0
    for i in range(n):
        penalty += coloring[i] * (4 ** (n - 1 - i))
    return penalty

def main():
    n, m, edges = read_input()
    
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Check if 3-coloring is possible
    possible, coloring = graph_coloring_possible(graph, n)
    
    if not possible:
        print("NO")
        return
    
    # Since we're using backtracking with colors in order [1,2,3], 
    # the first valid coloring we find will be lexicographically smallest,
    # which corresponds to the minimum penalty due to the weighting scheme.
    print("YES")
    print(' '.join(map(str, coloring)))

if __name__ == "__main__":
    main()
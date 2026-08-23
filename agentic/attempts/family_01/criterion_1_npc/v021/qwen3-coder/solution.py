import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # We model this as a 3-coloring problem on a graph
    # Each dial is a node, each crossbar is an edge
    # Adjacent nodes must have different colors (positions)
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Try all possible 3-colorings in lexicographical order
    # Colors are 1, 2, 3
    color = [0] * n  # 0 means unassigned
    
    def is_valid(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    # Use backtracking to find the lexicographically smallest valid coloring
    def backtrack(node):
        if node == n:
            return True
        for c in [1, 2, 3]:
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    main()
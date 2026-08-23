import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Build adjacency list
    adj = defaultdict(list)
    index = 2
    edges = []
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        index += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # We need to 3-color the graph such that no adjacent nodes have the same color
    # This is equivalent to checking if the graph is 3-colorable
    # Since n <= 40, and we might have a dense graph, we'll use backtracking with pruning
    
    # For small graphs, we can try all 3^n combinations, but that's too much for n=40
    # However, since it's a constraint satisfaction problem, we can use backtracking with early pruning
    
    # Let's model this as a graph coloring problem
    # We want to assign each node a color from {1,2,3} such that no edge connects two nodes of the same color
    
    colors = [0] * n  # 0 means unassigned
    
    def is_safe(node, color):
        for neighbor in adj[node]:
            if colors[neighbor] == color:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for color in [1, 2, 3]:
            if is_safe(node, color):
                colors[node] = color
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        return False
    
    # Optimization: if any connected component is not 3-colorable, the whole graph isn't
    # But let's just do simple backtracking with good variable ordering
    
    # To get lexicographically smallest, we try colors in order 1,2,3 for each node
    # and process nodes in order 0 to n-1
    
    if backtrack(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    main()
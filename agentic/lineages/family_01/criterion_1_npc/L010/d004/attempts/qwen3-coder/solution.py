from collections import defaultdict
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # We need to color the graph with 3 colors such that no adjacent nodes have the same color
    # This is equivalent to checking if the graph is 3-colorable
    # We'll try all possible colorings in lexicographical order using backtracking
    
    color = [0] * n  # 0 means uncolored
    
    def is_safe(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        
        for c in [1, 2, 3]:
            if is_safe(node, c):
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
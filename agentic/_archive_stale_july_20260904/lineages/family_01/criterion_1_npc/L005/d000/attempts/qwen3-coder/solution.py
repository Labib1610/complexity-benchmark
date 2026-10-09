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
    idx = 2
    edges = []
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-indexed
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # If no edges, assign all to 1
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Try all 3^n assignments, but since n<=40, we need a smarter approach
    # This is actually a graph coloring problem with 3 colors, and we want the lex smallest coloring
    
    # Since n <= 40, and it's a graph coloring problem, let's try backtracking with pruning
    # But even that might be too slow. Let's think differently.
    
    # Actually, let's model this as a 3-coloring problem and use backtracking with constraint propagation
    # We'll search in lexicographical order
    
    color = [-1] * n  # -1 means unassigned
    
    def is_valid(node, c):
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(pos):
        if pos == n:
            return True
        
        for c in [1, 2, 3]:
            if is_valid(pos, c):
                color[pos] = c
                if backtrack(pos + 1):
                    return True
                color[pos] = -1
        return False
    
    # Check if graph is 3-colorable
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    main()
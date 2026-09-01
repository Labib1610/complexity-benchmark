from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Try all possible assignments in lexicographical order
    # We can use backtracking with constraint propagation
    # But since n <= 40 and we have 3 colors, it's manageable
    
    # However, we can do better with graph coloring approach
    # We want the lexicographically smallest valid coloring
    
    # Let's use a greedy approach with backtracking
    # Try to assign colors 1,2,3 to each node in order 1 to n
    # and backtrack when we find a conflict
    
    color = [0] * (n + 1)  # color[i] is the color of node i, 0 means unassigned
    
    def is_valid(node, c):
        # Check if assigning color c to node is valid
        for neighbor in adj[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def backtrack(node):
        if node > n:
            return True  # All nodes colored
        
        for c in range(1, 4):  # Try colors 1, 2, 3 in order
            if is_valid(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = 0  # Backtrack
        
        return False
    
    if backtrack(1):
        print("YES")
        print(" ".join(map(str, color[1:])))
    else:
        print("NO")

solve()
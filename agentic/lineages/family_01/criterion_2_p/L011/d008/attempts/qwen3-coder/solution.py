import sys
from collections import defaultdict, deque

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    return n, m, edges

def solve():
    n, m, edges = read_input()
    
    if m == 0:
        # No edges, any assignment works. Lexicographically smallest is all 1s.
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # For each edge (u,v), the resonance is det(M) = x_u * x_v - (-1) = x_u * x_v + 1
    # We want the product of all resonances to be 3^m
    # So we want ∏(x_u * x_v + 1) = 3^m
    
    # Since x_u, x_v ∈ {1,2}, the possible values of (x_u * x_v + 1) are:
    # 1*1+1=2, 1*2+1=3, 2*1+1=3, 2*2+1=5
    # So we want ∏(x_u * x_v + 1) = 3^m
    # This means we want as many factors of 3 as possible, and other factors should multiply to give exactly 3^m
    
    # Actually, let's think differently.
    # x_u * x_v + 1 can be 2, 3, or 5.
    # We want the product to be 3^m.
    # This means we need every factor to be 3, because 2 and 5 are not multiples of 3.
    # So we need x_u * x_v + 1 = 3 for every edge, which means x_u * x_v = 2.
    # The only way to get x_u * x_v = 2 with x_u, x_v ∈ {1,2} is x_u=1, x_v=2 or x_u=2, x_v=1.
    
    # This is equivalent to a 2-coloring problem where adjacent nodes have different values.
    # But we also need the product to be exactly 3^m.
    # Let's reconsider...
    
    # Wait, let's recheck the math:
    # M = [x_u  1]
    #     [-1   x_v]
    # det(M) = x_u * x_v - (1 * -1) = x_u * x_v + 1
    # 
    # x_u=1,x_v=1: det = 1*1+1 = 2
    # x_u=1,x_v=2: det = 1*2+1 = 3
    # x_u=2,x_v=1: det = 2*1+1 = 3
    # x_u=2,x_v=2: det = 2*2+1 = 5
    #
    # Product should be 3^m.
    # This means we want every edge to contribute a factor of 3.
    # That means for every edge (u,v), we want x_u * x_v = 2.
    # Which means one of x_u,x_v is 1 and the other is 2.
    # This is a bipartite graph coloring problem!
    
    # Check if the graph is bipartite
    color = [-1] * n  # -1: unvisited, 0: color 0, 1: color 1
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False  # Not bipartite
        return True
    
    # Check if all components are bipartite
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
    
    # Graph is bipartite. Now assign tiers to make it perfectly balanced.
    # In a bipartite graph, we can assign:
    # Color 0 -> tier 1
    # Color 1 -> tier 2
    # This ensures x_u * x_v = 1*2 = 2 for every edge, so det = 3 for every edge.
    # Product = 3^m. Perfect!
    
    # To get lexicographically smallest assignment, we might need to decide which color gets which tier.
    # Try both assignments and pick the lexicographically smaller one.
    
    # Assignment 1: color 0 -> 1, color 1 -> 2
    assignment1 = [1 if color[i] == 0 else 2 for i in range(n)]
    
    # Assignment 2: color 0 -> 2, color 1 -> 1
    assignment2 = [2 if color[i] == 0 else 1 for i in range(n)]
    
    # Find lexicographically smaller
    if assignment1 <= assignment2:
        result = assignment1
    else:
        result = assignment2
    
    print("YES")
    print(" ".join(map(str, result)))

solve()
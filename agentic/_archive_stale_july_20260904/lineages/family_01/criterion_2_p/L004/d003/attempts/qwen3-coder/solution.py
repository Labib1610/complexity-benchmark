import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # The constraint is x^3 + y^3 = 9 where x,y in {1,2}
    # 1^3 = 1, 2^3 = 8
    # So 1^3 + 2^3 = 9 and 2^3 + 1^3 = 9
    # This means connected nodes must have different assignments
    
    # This is a bipartite graph check
    color = {}
    
    # Check each component
    nodes = set(adj.keys())
    all_nodes = set(range(1, n+1))
    
    for start in all_nodes:
        if start not in color:
            # BFS to check bipartiteness and assign colors
            queue = deque()
            queue.append(start)
            color[start] = 1
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 2 if current_color == 1 else 1
                
                for v in adj[u]:
                    if v not in color:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] != next_color:
                        print("NO")
                        return
    
    # If we reach here, it's bipartite
    # We need the lexicographically smallest assignment
    # That means we want as many 1's as possible at the beginning
    # In our coloring, we used 1 and 2. To make it lex smallest,
    # we should ensure that color 1 is assigned to the lower indexed nodes when possible
    
    # Actually, our BFS already ensures a valid 2-coloring
    # To get lexicographically smallest, we can just ensure that
    # node 1 (if present) gets color 1
    # But since we're processing nodes in order, and assigning 1 first,
    # the result should already be lex smallest
    
    # Let's re-do the coloring to ensure lex smallest
    color = {}
    for start in range(1, n+1):
        if start not in color:
            # Start with color 1
            queue = deque()
            queue.append(start)
            color[start] = 1
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 2 if current_color == 1 else 1
                
                # Process neighbors in sorted order for consistency
                for v in sorted(adj[u]):
                    if v not in color:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] != next_color:
                        print("NO")
                        return
    
    # All nodes including isolated ones should be assigned
    result = []
    for i in range(1, n+1):
        if i not in color:
            # Isolated node - assign 1 for lex smallest
            result.append('1')
        else:
            result.append(str(color[i]))
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()
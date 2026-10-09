import sys
from collections import defaultdict, deque

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        # No constraints, all 1s is the lexicographically smallest solution
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # For the interference formula p_u^2 + p_v^2 + p_u * p_v = 7
    # With p_u, p_v in {1, 2}:
    # 1,1: 1+1+1=3
    # 1,2: 1+4+2=7  <-- Valid
    # 2,1: 4+1+2=7  <-- Valid
    # 2,2: 4+4+4=12
    # So only (1,2) and (2,1) pairs are valid.
    
    # This means the graph must be bipartite, and we need to 2-color it.
    # We color with 1 and 2.
    
    colors = [0] * (n + 1)  # 0 means unvisited, 1 and 2 are the two colors
    
    # Check if the graph is bipartite
    for start in range(1, n + 1):
        if colors[start] == 0:
            queue = deque()
            queue.append(start)
            colors[start] = 1
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = 3 - colors[u]  # Flip color: 1->2, 2->1
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        print("NO")
                        return
    
    # The graph is bipartite. Now we need the lex smallest valid coloring.
    # Since both 1 and 2 are valid "first" colors for the first node,
    # we try both and pick the lex smaller result.
    
    def get_coloring(first_color):
        col = [0] * (n + 1)
        queue = deque()
        queue.append(1)
        col[1] = first_color
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if col[v] == 0:
                    col[v] = 3 - col[u]
                    queue.append(v)
                elif col[v] != 3 - col[u]:
                    return None  # Not bipartite or conflict
        return col
    
    # Try coloring node 1 with color 1
    col1 = get_coloring(1)
    # Try coloring node 1 with color 2
    col2 = get_coloring(2)
    
    if col1 is None and col2 is None:
        print("NO")
        return
    
    result = None
    if col1 is not None:
        result = col1
    if col2 is not None:
        if result is None or tuple(col2[1:]) < tuple(result[1:]):
            result = col2
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result[1:])))

solve()
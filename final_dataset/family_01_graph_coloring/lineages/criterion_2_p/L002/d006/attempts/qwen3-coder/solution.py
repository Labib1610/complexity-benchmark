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
    
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # For each edge (u,v), we need to count arrangements of t_u primary and t_v secondary audits
    # where no two of the same type are adjacent, and this count equals 1.
    # 
    # Let's say t_u = a, t_v = b.
    # We want to arrange 'a' P's and 'b' S's such that no two adjacent chars are same.
    # The number of such arrangements is:
    # If |a - b| > 1, then 0 arrangements (impossible).
    # If |a - b| = 1, then 1 arrangement.
    # If |a - b| = 0, then 2 arrangements (starting with P or S).
    #
    # We want exactly 1 arrangement, so we need |a - b| = 1.
    # That means one of {a,b} is 1 and the other is 2.
    # So for every edge, one endpoint gets tier 1 and the other gets tier 2.
    # This is equivalent to 2-coloring the graph.
    
    # So the problem reduces to checking if the graph is bipartite.
    # If not, output "NO".
    # If yes, find the lexicographically smallest 2-coloring.
    
    color = [-1] * n  # -1 means unvisited, 0 and 1 are the two colors (we'll map to 1 and 2 later)
    
    for start in range(n):
        if color[start] == -1:
            # BFS to 2-color the component
            queue = deque()
            queue.append(start)
            color[start] = 0  # Start with color 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        # Not bipartite
                        print("NO")
                        return
    
    # Graph is bipartite. Now we need the lexicographically smallest coloring.
    # In our encoding: 0 means tier 1, 1 means tier 2 OR 0 means tier 2, 1 means tier 1.
    # To get lex smallest sequence of tiers, we try both mappings and pick the better one.
    
    # Color 0 -> tier 1, Color 1 -> tier 2
    option1 = [1 if c == 0 else 2 for c in color]
    # Color 0 -> tier 2, Color 1 -> tier 1
    option2 = [2 if c == 0 else 1 for c in color]
    
    # Find the first index where they differ
    for i in range(n):
        if option1[i] < option2[i]:
            result = option1
            break
        elif option1[i] > option2[i]:
            result = option2
            break
    else:
        # They are identical (only happens if component has 1 node)
        result = option1
    
    print("YES")
    print(' '.join(map(str, result)))

solve()
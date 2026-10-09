import sys
from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # For the quadratic x^2 - (t_u + t_v)x + 2 = 0 to have integer roots,
    # the discriminant must be a perfect square.
    # Discriminant = (t_u + t_v)^2 - 8
    # For this to be a perfect square, let (t_u + t_v)^2 - 8 = k^2
    # So (t_u + t_v)^2 - k^2 = 8
    # (t_u + t_v - k)(t_u + t_v + k) = 8
    # The factor pairs of 8 are: (1,8), (2,4), (-1,-8), (-2,-4)
    # Solving these gives possible values for t_u + t_v: 3, -3, 3, -3
    # So t_u + t_v = 3 or -3
    # Since tiers are 1 or 2, t_u + t_v can only be 2, 3, or 4
    # So only t_u + t_v = 3 is valid (since 2 and 4 don't make discriminant a perfect square)
    # This means one tier is 1 and the other is 2.
    
    # So each edge must connect a node with tier 1 to a node with tier 2
    # This is equivalent to a bipartite graph where each edge connects nodes of different partitions
    
    # We can model this as a 2-SAT problem or as a graph coloring problem
    # Each node must be colored 1 or 2 such that adjacent nodes have different colors
    # This is possible iff the graph is bipartite
    
    # Check if the graph is bipartite and find the lexicographically smallest 2-coloring
    
    color = [-1] * n  # -1: unvisited, 0: color 1, 1: color 2
    
    # Process components in order to ensure lexicographically smallest assignment
    for start in range(n):
        if color[start] == -1:
            # BFS to color the component
            queue = deque()
            queue.append(start)
            # To get lexicographically smallest, we try to assign color 0 (tier 1) to the first node
            color[start] = 0
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                next_color = 1 - current_color
                
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = next_color
                        queue.append(v)
                    elif color[v] == current_color:
                        print("NO")
                        return
    
    # If we reach here, a valid coloring exists
    # Convert colors to tiers: color 0 -> tier 1, color 1 -> tier 2
    tiers = []
    for c in color:
        tiers.append(str(c + 1))
    
    print("YES")
    print(" ".join(tiers))

solve()
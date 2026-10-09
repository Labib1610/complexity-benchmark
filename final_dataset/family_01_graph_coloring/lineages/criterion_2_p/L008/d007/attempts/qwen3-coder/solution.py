import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    index = 2
    edges = []
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        index += 2
        edges.append((u, v))
        adj[u].append(len(edges)-1)
        adj[v].append(len(edges)-1)
    
    # Try both possibilities for the first node: c=1 and c=2
    # For each node, we'll determine if setting c=1 or c=2 leads to a consistent labeling
    
    # We model this as a 2-SAT problem
    # Each node i has two variables: c[i]=1 (var i*2) and c[i]=2 (var i*2+1)
    # For each edge (u,v), depending on their degrees, we derive constraints
    
    # Actually, let's think differently.
    # Let’s consider that for each edge (u,v), when we orient it as u->v,
    # then v gets +1 into its in-degree, and u gets +1 to its out-degree.
    # We want in-degree of node i to be d_i * (c_i - 1)
    # So if c_i = 1 => in-degree should be 0
    #    if c_i = 2 => in-degree should be d_i
    
    # Let’s build a graph where each node can be labeled 1 or 2
    # And there are implications based on edges
    
    # But perhaps simpler approach:
    # Try all 2^n combinations? No, too large.
    # Let's see if we can model this as a graph coloring with constraints.
    
    # Key insight:
    # For each node i, degree d_i, we want in-degree = d_i*(c_i - 1)
    # So if c_i=1, in-degree = 0
    #    if c_i=2, in-degree = d_i
    
    # That means:
    # If c_i=1, ALL edges incident to i must be oriented OUT from i
    # If c_i=2, ALL edges incident to i must be oriented IN to i
    
    # Wait, that's not right. Let me re-read...
    # "the total number of endpoints bringing data INTO lens i is exactly d_i * (c_i - 1)"
    # d_i is total number of tube endpoints connected to lens i.
    # Each tube contributes 2 endpoints to d_i if it's a self-loop on i,
    # otherwise 1 endpoint if it's incident to i.
    # Actually, looking at example:
    # Node degrees: 
    # 1: degree 2 (connected to 2 and 4)
    # 2: degree 2 
    # 3: degree 2
    # 4: degree 2
    # Solution: 1 2 1 2
    # Orient edges: 1->2, 2<-3, 3->4, 1<-4
    # In-degrees: 1:1, 2:1, 3:1, 4:1
    # Check: d_i * (c_i - 1) = 2*(1-1)=0 for c_i=1, = 2*(2-1)=2 for c_i=2
    # But observed in-degrees are 1 each. Hmm.
    
    # Re-examining problem statement:
    # "let d_i be the total number of tube endpoints connected to it"
    # "(If a tube connects a lens to itself, it provides two endpoints to that lens)"
    # So for a normal edge (u,v) with u != v, it contributes 1 to d_u and 1 to d_v
    # For self-loop (u,u), it contributes 2 to d_u
    
    # So d_i is just the degree of node i in the graph (counting self-loops twice)
    
    # Now, when we orient edges, each orientation decides which node gets +1 in-degree
    # We want final in-degree of i to be exactly d_i * (c_i - 1)
    
    # So if c_i = 1, desired in-degree = 0
    #    if c_i = 2, desired in-degree = d_i
    
    # This gives us a constraint satisfaction problem.
    # For each node i:
    #   if c_i = 1, then ALL edges incident to i must be oriented AWAY from i
    #   if c_i = 2, then ALL edges incident to i must be oriented TOWARD i
    
    # This is very restrictive!
    # For any two adjacent nodes u and v:
    # if c_u = 1, edge must go u -> v
    # if c_v = 2, edge must go u -> v
    # if c_u = 2, edge must go v -> u  
    # if c_v = 1, edge must go v -> u
    
    # So for edge (u,v):
    # if c_u=1 and c_v=1: impossible (u wants it away, v wants it away)
    # if c_u=1 and c_v=2: okay (u wants away, v wants toward) -> u->v
    # if c_u=2 and c_v=1: okay (u wants toward, v wants away) -> v->u  
    # if c_u=2 and c_v=2: impossible (u wants it toward, v wants it toward)
    
    # So valid pairs are (1,2) and (2,1)
    # This means the graph must be bipartite!
    # And we need to assign colors 1,2 such that adjacent nodes have different values
    # AND among all valid assignments, pick lexicographically smallest one
    
    # But wait, what about isolated vertices?
    # They have d_i = 0, so desired in-degree = 0*(c_i - 1) = 0 regardless of c_i
    # So they can be labeled 1 or 2. To get lex smallest, label them 1.
    
    # What about self-loops?
    # For self-loop (u,u): contributes 2 to d_u
    # When oriented, it gives 1 in and 1 out to u
    # Desired in-degree for u = d_u * (c_u - 1)  
    # With self-loop, d_u >= 2
    # If c_u = 1: desired = 0, but actual in-degree from self-loop is 1 -> impossible
    # If c_u = 2: desired = d_u >= 2, but actual in-degree from self-loop is 1 -> impossible unless d_u = 2
    # So if there's a self-loop, d_u must be exactly 2, and c_u must be 2
    
    # Summary:
    # 1. No self-loops allowed unless degree is exactly 2 and node gets label 2
    # 2. Graph must be bipartite
    # 3. Among valid 2-colorings, choose one that is lexicographically smallest
    
    # Check for self-loops
    has_self_loop = [False] * n
    degree = [0] * n
    for u, v in edges:
        if u == v:
            has_self_loop[u] = True
        degree[u] += 1
        degree[v] += 1
    
    # Build adjacency list without self-loops for bipartition check
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        if u != v:
            adj_list[u].append(v)
            adj_list[v].append(u)
    
    # Color array: -1 unvisited, 0 color 0, 1 color 1
    color = [-1] * n
    c = [0] * n  # Final assignment, 1 or 2
    
    # BFS to check bipartiteness and assign initial colors
    for start in range(n):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0
            
            while queue:
                u = queue.popleft()
                current_color = color[u]
                
                for v in adj_list[u]:
                    if color[v] == -1:
                        color[v] = 1 - current_color
                        queue.append(v)
                    elif color[v] == current_color:
                        # Not bipartite
                        print("NO")
                        return
    
    # Now assign c values based on color and special cases
    # Rule:
    # if has_self_loop[i]: c[i] = 2 (and degree[i] must be 2)
    # else: c[i] = color[i] + 1
    
    for i in range(n):
        if has_self_loop[i]:
            if degree[i] != 2:
                print("NO")
                return
            c[i] = 2
        else:
            # Assign 1 to color 0, 2 to color 1 to get lex smallest
            c[i] = color[i] + 1
    
    # Validate that this works:
    # For each edge (u,v) with u != v:
    # if c[u]=1, c[v]=2: orient u->v (okay because u wants all out, v wants all in)
    # if c[u]=2, c[v]=1: orient v->u (okay)
    # if c[u]=c[v]: contradiction since graph is bipartite
    print("YES")
    print(' '.join(map(str, c)))

if __name__ == "__main__":
    main()
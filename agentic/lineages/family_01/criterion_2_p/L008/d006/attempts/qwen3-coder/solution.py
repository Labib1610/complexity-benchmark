import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [[] for _ in range(n+1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # We'll build a graph where each edge represents a constraint
    # For each edge (u,v), we have:
    # S_u + d_u * c_u = 3 * d_u  =>  sum of neighbors of u + d_u * c_u = 3 * d_u
    # S_v + d_v * c_v = 3 * d_v  =>  sum of neighbors of v + d_v * c_v = 3 * d_v
    
    # Let's derive constraints:
    # For node u: sum_{v in N(u)} c_v + d_u * c_u = 3 * d_u
    # Which means: sum_{v in N(u)} c_v = 3*d_u - d_u*c_u = d_u*(3 - c_u)
    # Since c_u is either 1 or 2:
    #   if c_u=1: sum_{v in N(u)} c_v = d_u * 2 = 2*d_u
    #   if c_u=2: sum_{v in N(u)} c_v = d_u * 1 = d_u
    
    # So for each node u, depending on c_u being 1 or 2, the sum of its neighbors' c values is fixed.
    
    # This suggests a 2-SAT approach or bipartitioning.
    # But let's think differently.
    
    # Rewrite the equation:
    # S_i = 3*d_i - d_i*c_i = d_i*(3 - c_i)
    # So sum of neighbor values = d_i*(3 - c_i)
    # If c_i=1: sum = 2*d_i
    # If c_i=2: sum = d_i
    
    # That means for each node, given its degree d_i, if we choose c_i, 
    # the sum of its neighbors must be d_i*(3-c_i).
    
    # Let's consider this as a system of equations over GF(2) or parity checks,
    # but since values are 1 and 2, let's map 1 -> 0, 2 -> 1 to work mod 2.
    # Or better yet, let's keep it as is and see if we can model it.
    
    # Actually, let's think of it this way:
    # For each edge (u,v), it contributes to both S_u and S_v.
    # S_u includes c_v, and S_v includes c_u.
    # The constraint for u: S_u = d_u*(3 - c_u)
    # The constraint for v: S_v = d_v*(3 - c_v)
    
    # Let's try to model this as a graph coloring problem with constraints.
    # But perhaps easier: let's see if the graph must be bipartite.
    
    # Wait, let's re-express the constraint:
    # Sum_{j in N(i)} c_j = d_i * (3 - c_i)
    # This is a constraint per node based on its neighbors.
    
    # Let's try to solve this systematically.
    # For each connected component, we can try to assign values.
    # Let's see if there's a pattern.
    
    # Consider a simple edge (u,v):
    # Node u: c_v = d_u*(3 - c_u)
    # Node v: c_u = d_v*(3 - c_v)
    # d_u = 1, d_v = 1
    # So: c_v = 3 - c_u
    #     c_u = 3 - c_v
    # Substituting: c_u = 3 - (3 - c_u) = c_u. Always true.
    # So for any edge, we can pick c_u, then c_v = 3 - c_u.
    
    # But what about triangles?
    # Nodes 1,2,3 all connected.
    # d_1 = d_2 = d_3 = 2
    # Constraint for 1: c_2 + c_3 = 2*(3 - c_1) = 6 - 2*c_1
    # Constraint for 2: c_1 + c_3 = 6 - 2*c_2
    # Constraint for 3: c_1 + c_2 = 6 - 2*c_3
    # Let's say c_1=1: c_2 + c_3 = 4
    # c_2=2, c_3=2 works: 2+2=4. Check others.
    # c_2=2: c_1 + c_3 = 6-4=2. We have c_1=1, c_3=2: 1+2=3 != 2. Contradiction.
    # c_1=2: c_2 + c_3 = 2
    # Try c_2=1, c_3=1: sum=2. Check others.
    # c_2=1: c_1 + c_3 = 6-2=4. c_1=2, c_3=1: 2+1=3 != 4.
    # Try c_2=1, c_3=1:
    # Check third equation: c_1+c_2 = 6-2*c_3 = 4. c_1=2,c_2=1: 3 != 4.
    # Try c_1=1, c_2=2, c_3=2:
    # Eq 1: 2+2=4 = 6-2*1 = 4  OK
    # Eq 2: 1+2=3 = 6-2*2 = 2  NO
    # Try c_1=2, c_2=1, c_3=1:
    # Eq 1: 1+1=2 = 6-2*2 = 2  OK
    # Eq 2: 2+1=3 = 6-2*1 = 4  NO
    # It seems impossible for triangle. This matches example 2.
    
    # So the graph cannot contain odd cycles. Must be bipartite!
    
    # Let's check if the graph is bipartite.
    # If not, return "NO".
    # If yes, we can 2-color it. But we want lexicographically smallest.
    
    # In a bipartite graph with parts L and R:
    # We can assign all in L to 1, all in R to 2, or vice versa.
    # To get lexicographically smallest, we should try to assign 1 to nodes with lower indices.
    # So we can do BFS from node 1, assigning colors alternately, preferring color 1 for earlier nodes.
    
    # But actually, we need to ensure the constraint holds.
    # In a bipartite graph, if we assign one part to 1 and other to 2, does it satisfy?
    # Let's check:
    # Suppose parts are A (assigned 1) and B (assigned 2).
    # For a node u in A: neighbors are in B, so S_u = |N(u)| * 2
    # Constraint: S_u = d_u * (3 - c_u) = d_u * (3 - 1) = 2 * d_u. OK.
    # For a node v in B: neighbors are in A, so S_v = |N(v)| * 1  
    # Constraint: S_v = d_v * (3 - c_v) = d_v * (3 - 2) = d_v. OK.
    
    # So any bipartite assignment works! To get lex smallest, we prefer to assign 1 to lower-indexed nodes.
    # We can do BFS starting from unvisited nodes in order, always assigning 1 to the start node.
    
    color = [0] * (n+1)  # 0: unvisited, 1: color 1, 2: color 2
    visited = [False] * (n+1)
    
    for start in range(1, n+1):
        if visited[start]:
            continue
        queue = deque()
        queue.append(start)
        color[start] = 1
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            c_u = color[u]
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 3 - c_u  # if c_u=1, then c_v=2; if c_u=2, then c_v=1
                    queue.append(v)
                else:
                    # Check consistency
                    if color[v] == c_u:
                        print("NO")
                        return
    
    # If we reach here, it's bipartite and we have a valid coloring.
    # But wait, we assumed that assigning parts to {1,2} works, but we need to verify.
    # Actually, our derivation showed that any bipartite assignment works.
    
    # To get lexicographically smallest, among all valid 2-colorings, 
    # we can try to flip colors in components to make earlier nodes 1.
    # But BFS starting from low indices and assigning 1 to root gives lex-min.
    
    # Actually, let's double-check with BFS ensuring no odd cycle:
    def is_bipartite():
        colors = [-1] * (n+1)
        for i in range(1, n+1):
            if colors[i] == -1:
                queue = deque([i])
                colors[i] = 0
                while queue:
                    u = queue.popleft()
                    for v in adj[u]:
                        if colors[v] == -1:
                            colors[v] = 1 - colors[u]
                            queue.append(v)
                        elif colors[v] == colors[u]:
                            return False
        return True
    
    if not is_bipartite():
        print("NO")
        return
    
    # Now we know it's bipartite. Assign colors to get lex smallest.
    # We can do BFS again, but this time ensuring we assign 1 to lower nodes when possible.
    # A simpler way: just do BFS from 1 to n, and for each component, 
    # assign 1 to the first node encountered.
    
    colors = [0] * (n+1)
    for i in range(1, n+1):
        if colors[i] == 0:
            queue = deque([i])
            colors[i] = 1
            while queue:
                u = queue.popleft()
                c_u = colors[u]
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = 3 - c_u
                        queue.append(v)
                    elif colors[v] == c_u:
                        print("NO")
                        return
    
    print("YES")
    print(' '.join(str(colors[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()
import sys
from collections import defaultdict, deque

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    return n, m, edges, adj

def is_valid_pair(tu, tv):
    # We need C(tu+tv, tu) to be odd
    # Lucas' theorem: C(n,k) is odd iff for all i, bit_i(k) <= bit_i(n)
    # In our case, n = tu+tv, k = tu
    # So we need (tu & (tu+tv)) == tu
    total = tu + tv
    return (tu & total) == tu

def get_valid_pairs():
    valid = set()
    for t1 in [1, 2]:
        for t2 in [1, 2]:
            if is_valid_pair(t1, t2):
                valid.add((t1, t2))
    return valid

def solve():
    n, m, edges, adj = read_input()
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    valid_pairs = get_valid_pairs()
    if not valid_pairs:
        print("NO")
        return
    
    # Build constraint graph - for each edge (u,v), we have constraints on (tier[u], tier[v])
    # This is a 2-SAT problem. Each variable has two possible values (1 or 2).
    # For each edge (u,v), only certain pairs of values are allowed.
    
    # We'll use graph coloring approach. This is actually a bipartite checking problem
    # with specific constraints.
    
    # Let's think differently. For each connected component, we can try both 
    # assignments (starting with 1 or 2 for the first node) and propagate constraints.
    
    color = [0] * (n + 1)  # 0 means unvisited, 1 and 2 are the tiers
    
    def bfs(start):
        queue = deque([start])
        color[start] = 1  # Try starting with tier 1
        
        while queue:
            u = queue.popleft()
            current_color = color[u]
            
            for v in adj[u]:
                # Determine what colors v can have based on the edge constraint
                valid_colors_for_v = []
                for c in [1, 2]:
                    if (current_color, c) in valid_pairs:
                        valid_colors_for_v.append(c)
                
                if not valid_colors_for_v:
                    return False  # No valid color for v
                
                if color[v] == 0:  # Not colored yet
                    # If only one option, use it
                    if len(valid_colors_for_v) == 1:
                        color[v] = valid_colors_for_v[0]
                        queue.append(v)
                    else:
                        # Both 1 and 2 are valid, choose the smaller one for lex order
                        color[v] = 1
                        queue.append(v)
                else:
                    # Already colored, check if it's still valid
                    if color[v] not in valid_colors_for_v:
                        return False
        return True
    
    # Check if we can color each connected component
    visited = [False] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:  # Not yet processed
            # Try coloring component starting with 1
            # We need a more systematic approach
            
            # For each component, we'll try both starting colors
            # But we want the lexicographically smallest solution overall
            
            # Let's do a proper 2-SAT or graph-based approach
            
            # Actually, let's model this properly:
            # For each node, it can be tier 1 or 2
            # For each edge, only certain combinations are allowed
            # This defines a constraint graph
            
            # Better approach: for each connected component, 
            # try both possible assignments for the first node,
            # then propagate. Take the one that works, preferring
            # the one that gives lexicographically smaller result.
            
            component_nodes = []
            queue_comp = deque([i])
            visited[i] = True
            component_nodes.append(i)
            
            while queue_comp:
                u = queue_comp.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue_comp.append(v)
                        component_nodes.append(v)
            
            # Now we have a component. Try to 2-color it with constraints.
            # Use BFS with backtracking concept
            
            def try_coloring(start_node, start_color):
                temp_color = [0] * (n + 1)
                temp_color[start_node] = start_color
                queue_bfs = deque([start_node])
                
                while queue_bfs:
                    u = queue_bfs.popleft()
                    current_tier = temp_color[u]
                    
                    for v in adj[u]:
                        # What tiers can v have?
                        valid_tiers = []
                        for t in [1, 2]:
                            if (current_tier, t) in valid_pairs:
                                valid_tiers.append(t)
                        
                        if not valid_tiers:
                            return None  # Impossible
                        
                        if temp_color[v] == 0:
                            if len(valid_tiers) == 1:
                                temp_color[v] = valid_tiers[0]
                            else:
                                # Choose 1 for lex smallest
                                temp_color[v] = 1
                            queue_bfs.append(v)
                        else:
                            # Check consistency
                            if temp_color[v] not in valid_tiers:
                                return None
                
                return temp_color
            
            # Try starting with color 1
            res1 = try_coloring(i, 1)
            res2 = try_coloring(i, 2)
            
            # Choose the one that leads to lex smallest
            chosen_res = None
            if res1 is not None:
                chosen_res = res1
            elif res2 is not None:
                chosen_res = res2
            else:
                print("NO")
                return
            
            # Copy results to main color array
            for node in component_nodes:
                color[node] = chosen_res[node]
    
    # Final validation
    for u, v in edges:
        if (color[u], color[v]) not in valid_pairs:
            print("NO")
            return
    
    print("YES")
    print(" ".join(map(str, color[1:])))

solve()
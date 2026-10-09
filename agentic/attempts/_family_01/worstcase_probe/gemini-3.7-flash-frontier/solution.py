import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v:
            adj[u].append(v)
            adj[v].append(u)
            
    for i in range(n):
        adj[i] = list(set(adj[i]))

    # Check for self loops
    # If self-loop existed it would be impossible, but standard graphs don't have them or u != v handled.
    
    # Solve per connected component
    visited = [False] * n
    final_colors = [0] * n
    
    for start_node in range(n):
        if visited[start_node]:
            continue
        
        # BFS to get component
        comp = []
        queue = [start_node]
        visited[start_node] = True
        for u in queue:
            comp.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        
        # Subgraph for this component
        comp_size = len(comp)
        node_to_id = {u: i for i, u in enumerate(comp)}
        comp_adj = [[node_to_id[v] for v in adj[u]] for u in comp]
        
        # 3-coloring solver with Forward Checking and MRV
        # domains represented as bitmask: 1 -> color 0, 2 -> color 1, 4 -> color 2
        domains = [7] * comp_size
        
        popcount = [0, 1, 1, 2, 1, 2, 2, 3]
        
        def backtrack(domains):
            # Unit propagation
            domains = list(domains)
            changed = True
            while changed:
                changed = False
                for i in range(comp_size):
                    d = domains[i]
                    if popcount[d] == 0:
                        return None
                    if popcount[d] == 1:
                        # Check if any neighbor has this color
                        for v in comp_adj[i]:
                            if domains[v] & d:
                                domains[v] &= ~d
                                if domains[v] == 0:
                                    return None
                                changed = True
            
            # Check if all assigned
            all_assigned = True
            best_var = -1
            min_dom = 4
            for i in range(comp_size):
                cnt = popcount[domains[i]]
                if cnt > 1:
                    all_assigned = False
                    if cnt < min_dom:
                        min_dom = cnt
                        best_var = i
            
            if all_assigned:
                return domains
            
            # Branch on best_var
            var_dom = domains[best_var]
            for c in (1, 2, 4):
                if var_dom & c:
                    next_domains = list(domains)
                    next_domains[best_var] = c
                    res = backtrack(next_domains)
                    if res is not None:
                        return res
            return None

        # To break symmetry for the first node in component
        domains[0] = 1
        res = backtrack(domains)
        if res is None:
            print("NO")
            return
        
        for i, u in enumerate(comp):
            d = res[i]
            if d == 1:
                final_colors[u] = 1
            elif d == 2:
                final_colors[u] = 2
            elif d == 4:
                final_colors[u] = 3
            else:
                final_colors[u] = 1

    print("YES")
    print(*(final_colors[i] for i in range(n)))

if __name__ == '__main__':
    solve()
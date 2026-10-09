import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each clause (a or b), we create implications:
    # not a => b and not b => a
    # Variables are 1-indexed. We'll use 2*i for x_i and 2*i+1 for not x_i
    # But actually, let's think of it as: 
    # variable i (1-based) -> node 2*i (positive) and 2*i+1 (negative)
    # So for variable i: positive literal is node 2*i, negative literal is node 2*i+1
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    idx = 2
    clauses = []
    for i in range(m):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        clauses.append((a, b))
        
        # Clause: a or b
        # This is equivalent to: not a => b and not b => a
        
        # Node IDs:
        # For variable x (1-based):
        # Positive literal x: node 2*x
        # Negative literal -x: node 2*x + 1
        
        # not a => b
        # If a is positive (a > 0): not a is node 2*a + 1, b depends on its sign
        # If a is negative (a < 0): not a is node 2*abs(a), b depends on its sign
        
        # Let's define a function to get node id
        def get_node(lit):
            if lit > 0:
                return 2 * lit      # positive literal
            else:
                return 2 * (-lit) + 1  # negative literal
                
        def get_neg_node(lit):
            if lit > 0:
                return 2 * lit + 1   # negation of positive literal
            else:
                return 2 * (-lit)    # negation of negative literal
        
        # not a => b
        adj[get_neg_node(a)].append(get_node(b))
        rev_adj[get_node(b)].append(get_neg_node(a))
        
        # not b => a
        adj[get_neg_node(b)].append(get_node(a))
        rev_adj[get_node(a)].append(get_neg_node(b))
    
    # Now we do Kosaraju's algorithm to find strongly connected components
    # First DFS to get finishing times
    visited = [False] * (2 * n + 2)
    finish_stack = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        finish_stack.append(u)
    
    for i in range(2, 2*n + 2):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on transpose graph in reverse finish order
    visited = [False] * (2 * n + 2)
    scc_id = [0] * (2 * n + 2)
    scc_count = 0
    
    def dfs2(u, cid):
        visited[u] = True
        scc_id[u] = cid
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, cid)
    
    while finish_stack:
        u = finish_stack.pop()
        if not visited[u]:
            scc_count += 1
            dfs2(u, scc_count)
    
    # Check for contradictions: variable and its negation in same SCC
    for i in range(1, n + 1):
        pos = 2 * i
        neg = 2 * i + 1
        if scc_id[pos] == scc_id[neg]:
            print("NO")
            return
    
    # Assign values based on SCC topological order
    # In the finish_stack, later finishing nodes should be assigned False first
    # Actually, in Kosaraju, the first SCC we visit in second pass is sink
    # We can assign it False, and work backwards
    
    # Let's recompute the topological order of SCCs
    scc_graph = defaultdict(set)
    scc_nodes = defaultdict(list)
    
    for i in range(1, n + 1):
        pos = 2 * i
        neg = 2 * i + 1
        scc_nodes[scc_id[pos]].append((i, True))   # (variable_index, is_positive)
        scc_nodes[scc_id[neg]].append((i, False))
    
    for u in range(2, 2*n + 2):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_graph[scc_id[u]].add(scc_id[v])
    
    # Topological sort of SCCs
    in_degree = defaultdict(int)
    for u in scc_graph:
        for v in scc_graph[u]:
            in_degree[v] += 1
            
    # Find SCCs with in-degree 0
    queue = deque()
    all_scc = set()
    for cid in scc_nodes:
        all_scc.add(cid)
    for cid in all_scc:
        if in_degree[cid] == 0:
            queue.append(cid)
            
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in scc_graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Assign truth values
    assignment = [None] * (n + 1)
    for cid in topo_order:
        for var, is_pos in scc_nodes[cid]:
            if assignment[var] is None:
                if is_pos:
                    assignment[var] = 0  # We want True literals in later SCCs
                else:
                    assignment[var] = 1
                    
    # Actually, let's think carefully about the implication graph logic
    # If there's a path from node u to node v, then u being true forces v to be true
    # In the condensation graph, if we process SCCs in topological order,
    # and assign False to earliest SCCs, we satisfy all implications
    
    # But we need to be more careful. Let's just do standard 2-SAT assignment:
    # Process SCCs in reverse topological order (last finished first)
    # Assign False to literals in earliest processed SCCs
    
    # finish_stack had earliest finishes at the bottom
    # So we process in order we popped them (reverse finish time)
    # But we already used finish_stack, let's rebuild it
    
    visited = [False] * (2 * n + 2)
    finish_list = []
    
    def dfs1b(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1b(v)
        finish_list.append(u)
    
    for i in range(2, 2*n + 2):
        if not visited[i]:
            dfs1b(i)
    
    # Now finish_list has earliest finish at the end
    # Reverse it to get latest finish first
    finish_list.reverse()
    
    # Reset visited for second pass
    visited = [False] * (2 * n + 2)
    assignment = [None] * (n + 1)
    
    # Process nodes in reverse finish time order
    # When we visit a node, if its variable isn't assigned yet, we assign it appropriately
    for u in finish_list:
        if visited[u]: continue
        # Do DFS to find whole SCC
        stack = [u]
        scc_members = []
        while stack:
            node = stack.pop()
            if visited[node]: continue
            visited[node] = True
            scc_members.append(node)
            for v in rev_adj[node]:
                if not visited[v]:
                    stack.append(v)
                    
        # Now assign values to variables in this SCC
        # Since this SCC comes early in reverse finish time, 
        # we should set these literals to False to satisfy implications
        # No, wait. That's confusing.
        
        # Standard approach: process in topological order of SCCs
        # and for each unassigned variable, set it to make the literal in later SCC true
        
        # Let's just reorient our thinking:
        # Build the condensation graph properly
        
    # Let's simplify and follow a known working approach:
    # Rebuild everything with clearer logic
    
    # Redo Kosaraju clearly
    visited = [False] * (2 * n + 2)
    finish_stack = []
    
    def dfs_1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs_1(v)
        finish_stack.append(u)
    
    # First pass
    for i in range(2, 2*n + 2):
        if not visited[i]:
            dfs_1(i)
    
    # Second pass
    visited = [False] * (2 * n + 2)
    scc_id = [-1] * (2 * n + 2)
    current_scc = 0
    
    def dfs_2(u):
        visited[u] = True
        scc_id[u] = current_scc
        for v in rev_adj[u]:
            if not visited[v]:
                dfs_2(v)
    
    # Process in reverse order of finishing times
    while finish_stack:
        u = finish_stack.pop()
        if not visited[u]:
            dfs_2(u)
            current_scc += 1
            
    # Check for contradictions
    for i in range(1, n+1):
        if scc_id[2*i] == scc_id[2*i + 1]:
            print("NO")
            return
            
    # Assign values
    # Create mapping from SCC to literals
    scc_to_literals = defaultdict(list)
    for i in range(1, n+1):
        scc_to_literals[scc_id[2*i]].append((i, True))
        scc_to_literals[scc_id[2*i + 1]].append((i, False))
        
    # Build SCC graph
    scc_graph = defaultdict(set)
    for u in range(2, 2*n + 2):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_graph[scc_id[u]].add(scc_id[v])
                
    # Topological sort of SCCs
    in_deg = defaultdict(int)
    all_sccs = set()
    for u in scc_graph:
        for v in scc_graph[u]:
            in_deg[v] += 1
            all_sccs.add(u)
            all_sccs.add(v)
    for cid in scc_to_literals:
        all_sccs.add(cid)
            
    queue = deque()
    for cid in all_sccs:
        if in_deg[cid] == 0:
            queue.append(cid)
            
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in scc_graph[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)
                
    # Assign truth values: process in reverse topological order
    # Variables in later SCCs (in topological order) are set to satisfy their literals
    assignment = [None] * (n + 1)
    for cid in topo_order:
        for var, is_positive in scc_to_literals[cid]:
            if assignment[var] is None:
                assignment[var] = 1 if is_positive else 0
                
    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()
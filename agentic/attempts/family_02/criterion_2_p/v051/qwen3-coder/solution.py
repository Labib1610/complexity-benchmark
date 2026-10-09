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
    
    # Build implication graph for 2-SAT
    # Variables: for valve i (1-based), 
    # node 2*i represents valve i in bypass mode (1)
    # node 2*i+1 represents valve i in radiator mode (0)
    # But we'll use 2*(i-1) and 2*(i-1)+1 for 0-based indexing internally
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    idx = 2
    for i in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        # clause: (x1 or x2)
        # implications: (~x1 -> x2) and (~x2 -> x1)
        
        # Convert literals to node numbers
        # l1 > 0 means variable l1 is True (bypass mode)
        # l1 < 0 means variable |l1| is False (radiator mode)
        if l1 > 0:
            var1 = l1 - 1  # 0-indexed variable
            node1_true = 2 * var1      # valve var1 in bypass (1)
            node1_false = 2 * var1 + 1 # valve var1 in radiator (0)
        else:
            var1 = -l1 - 1
            node1_true = 2 * var1 + 1
            node1_false = 2 * var1
            
        if l2 > 0:
            var2 = l2 - 1
            node2_true = 2 * var2
            node2_false = 2 * var2 + 1
        else:
            var2 = -l2 - 1
            node2_true = 2 * var2 + 1
            node2_false = 2 * var2
            
        # Add implications
        # (~x1 -> x2) : node1_false -> node2_true
        adj[node1_false].append(node2_true)
        rev_adj[node2_true].append(node1_false)
        
        # (~x2 -> x1) : node2_false -> node1_true
        adj[node2_false].append(node1_true)
        rev_adj[node1_true].append(node2_false)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on transpose graph
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check if satisfiable
    for i in range(n):
        node_true = 2 * i
        node_false = 2 * i + 1
        if scc_id[node_true] == scc_id[node_false]:
            print("NO")
            return
    
    # Assign values based on SCC completion order
    assignment = [-1] * n
    # Create a mapping from SCC id to nodes in that SCC
    scc_nodes = defaultdict(list)
    for i in range(2 * n):
        scc_nodes[scc_id[i]].append(i)
    
    # Process SCCs in reverse topological order
    scc_order = list(range(scc_count))
    # Actually, since we used Kosaraju, the finishing order gives us what we need
    # We can process in the order of scc ids from highest to lowest finish time
    # But since we don't have explicit finish times, we'll use the fact that 
    # if there's an edge from u to v, then finish[u] > finish[v] in first DFS
    # So when we process SCCs in reverse order of their ids (as computed),
    # we're processing in topological order of the condensation
    
    # Better approach: just go through all nodes and assign values
    for i in range(2 * n):
        var_index = i // 2
        if assignment[var_index] == -1:
            # If this node's SCC was processed already, we know its value
            # Otherwise, we decide based on which node (true/false) comes first
            node_false = 2 * var_index + 1
            node_true = 2 * var_index
            # In 2-SAT, if scc_id[node_false] > scc_id[node_true], 
            # then node_false is reachable from node_true in implication,
            # so we should set variable to false.
            # Wait, let's think carefully.
            # The SCC ids are assigned in post-order of the reverse graph traversal.
            # So higher SCC id means it was finished later in the first DFS.
            # In the original graph, if there's a path from u to v, 
            # then u finishes after v in the first DFS.
            # So if scc_id[u] > scc_id[v], there might be a path from u to v.
            # For a variable, if scc_id[node_true] > scc_id[node_false],
            # it suggests node_true can reach node_false, meaning setting var=True forces var=False,
            # which would be inconsistent unless we avoid setting var=True.
            # So we should set the variable to the one with lower SCC id.
            
            # Actually, standard approach:
            # If scc_id[node_x] > scc_id[~node_x], then node_x should be true.
            # Because in the implication graph, if node_x is in a later SCC than ~node_x,
            # it means setting node_x to true doesn't lead to contradiction immediately,
            # whereas setting ~node_x to true might force node_x to be true too.
            
            # No wait, let's recheck the Kosaraju logic.
            # In our case, scc_id is assigned during the second DFS on the reverse graph.
            # Nodes in the same SCC are strongly connected.
            # When we process SCCs in the order found by Kosaraju (increasing scc_id),
            # we're going in reverse topological order of the SCC DAG.
            # To get the actual topological order, we process from highest scc_id to lowest.
            # For each unassigned variable, we look at which literal (positive or negative)
            # is in the SCC with higher index (processed later in first DFS).
            # That literal should be set to true.
            
            # Simpler: for each variable, check which of its literals is in the higher SCC id
            id_false = scc_id[node_false]
            id_true = scc_id[node_true]
            if id_true > id_false:
                assignment[var_index] = 1
            elif id_false > id_true:
                assignment[var_index] = 0
            else:
                # Same SCC, either is fine, but shouldn't happen in satisfiable case
                # Just pick one
                assignment[var_index] = 1
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()
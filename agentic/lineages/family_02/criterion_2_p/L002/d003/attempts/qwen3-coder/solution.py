import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each clause (c1, c2), we must have at least one of them true.
    # This is a 2-SAT problem.
    # Variable x_i represents machine i being in mode 1 (True) or mode 0 (False).
    # c_i > 0 means x_{c_i} should be True
    # c_i < 0 means x_{|c_i|} should be False (i.e. not x_{|c_i|} should be True)
    # So clause (c1, c2) means (x1 OR x2) where:
    #   if c1 > 0, then x1 = x_{c1}
    #   if c1 < 0, then x1 = not x_{|c1|}
    # Similarly for x2 and c2.
    
    # Build implication graph
    # For clause (a OR b), we add edges (not a -> b) and (not b -> a)
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    def add_implication(a, a_neg, b, b_neg):
        # a OR b is the same as (not a -> b) and (not b -> a)
        # a is var_a with sign a_neg
        # b is var_b with sign b_neg
        # not a is var_a with sign not a_neg
        # not b is var_b with sign not b_neg
        from_node = (abs(a), 1 - a_neg if a < 0 else a_neg)
        to_node = (abs(b), 1 - b_neg if b < 0 else b_neg)
        adj[from_node].append(to_node)
        rev_adj[to_node].append(from_node)
        
        from_node_rev = (abs(b), b_neg if b < 0 else 1 - b_neg)
        to_node_rev = (abs(a), a_neg if a < 0 else 1 - a_neg)
        adj[from_node_rev].append(to_node_rev)
        rev_adj[to_node_rev].append(from_node_rev)
    
    for _ in range(m):
        c1, c2 = map(int, sys.stdin.readline().split())
        # Clause is (x1 OR x2) where:
        # x1 is True if c1 > 0 and machine |c1| is in mode 1
        # x1 is True if c1 < 0 and machine |c1| is in mode 0
        # Similarly for x2
        # So we want (x1 OR x2)
        add_implication(c1, 0, c2, 0)
    
    # Now we do Kosaraju's algorithm to find strongly connected components
    visited = set()
    order = []
    
    def dfs1(node):
        if node in visited:
            return
        visited.add(node)
        for nei in adj[node]:
            dfs1(nei)
        order.append(node)
    
    # All possible nodes
    nodes = set()
    for u in adj:
        nodes.add(u)
        for v in adj[u]:
            nodes.add(v)
    for u in rev_adj:
        nodes.add(u)
        for v in rev_adj[u]:
            nodes.add(v)
            
    for node in nodes:
        dfs1(node)
    
    visited = set()
    scc = {}
    scc_id = 0
    
    def dfs2(node):
        if node in visited:
            return
        visited.add(node)
        scc[node] = scc_id
        for nei in rev_adj[node]:
            dfs2(nei)
    
    while order:
        node = order.pop()
        if node not in visited:
            dfs2(node)
            scc_id += 1
    
    # Check if any variable and its negation are in the same SCC
    for i in range(1, n+1):
        pos = (i, 1)  # x_i
        neg = (i, 0)  # not x_i
        if scc.get(pos, -1) == scc.get(neg, -2):
            print("NO")
            return
    
    # Build assignment
    assignment = {}
    # Process SCCs in reverse topological order
    # SCCs are already numbered in reverse topological order by Kosaraju
    for node, sid in scc.items():
        if node[0] not in assignment:
            # If not assigned yet, assign it false if it's in a lower SCC
            # But actually, in Kosaraju, we process in reverse, so higher scc_id means later in topological order
            # So if we process from highest scc_id to lowest, and assign when first seen...
            # Actually, let's think differently:
            # In the implication graph, if there's a path from u to v, then u being true forces v to be true.
            # In the reverse graph with SCCs, if SCC A -> SCC B in the condensation,
            # then we should assign False to all in A before assigning True to all in B.
            # Kosaraju gives SCC ids such that if there's a path from u to v, then scc[u] <= scc[v]
            # So to satisfy implications, we process SCCs in order of increasing SCC id,
            # and for each unassigned variable in that SCC, we assign it False if its negation was assigned True,
            # or True if its negation was assigned False, or default to False.
            # But there's a simpler way:
            # For each variable, if scc of (x_i) comes AFTER scc of (not x_i) in topological order,
            # then x_i should be True. Otherwise False.
            # Since Kosaraju gives reverse topological order in the finishing order of first DFS,
            # and we used that to create order, higher scc_id means earlier in reverse topological order.
            # So if scc[(i,1)] has higher id than scc[(i,0)], then (i,1) is processed first in reverse,
            # meaning (i,0) is processed first in normal topological order, so we should set x_i to False.
            # Wait, let's re-examine Kosaraju:
            # 1. Do DFS on original graph, record finish times
            # 2. Do DFS on transpose graph in order of decreasing finish times
            # 3. Each tree in second DFS is an SCC
            # The SCCs are found in reverse topological order.
            # So first SCC found in step 2 is last in topological order.
            # So when we assign, we can go through SCCs in the order we found them (reverse topological)
            # and for each unassigned variable, assign it to make the SCC consistent.
            # But there's a simpler check: for each variable x, if SCC(x) == SCC(not x), unsatisfiable.
            # Otherwise, in a satisfying assignment, if SCC(x) comes before SCC(not x) in topological order,
            # we must set x to False. If SCC(x) comes after SCC(not x), we set x to True.
            # Since Kosaraju finds SCCs in reverse topological order, 
            # if scc_id of x < scc_id of not x, then SCC(x) is later in topological order, so set x=True.
            # if scc_id of x > scc_id of not x, then SCC(x) is earlier in topological order, so set x=False.
            pass  # We already checked for contradiction
    
    # Let's re-process to get assignment
    # Create a list of SCCs in the order they were discovered (reverse topological order of condensation)
    scc_order = []
    scc_to_nodes = defaultdict(list)
    for node, sid in scc.items():
        scc_to_nodes[sid].append(node)
    
    # We need to get the topological order of SCCs
    # In Kosaraju, the order we find SCCs in DFS2 is reverse topological order of the condensation
    # So first SCC found is sink in condensation (last in topological order)
    # Let's just sort SCC ids by the order in which they were discovered
    # We can simulate this by noting the order in which we incremented scc_id
    # But we already have scc dictionary
    # Let's just iterate through scc_id from 0 to scc_id-1
    # and for each, assign values to variables
    
    assigned = {}
    # Process SCCs in order from 0 to scc_id-1, which is reverse topological order
    for sid in range(scc_id):
        for node in scc_to_nodes[sid]:
            var, val = node
            if var not in assigned:
                # In a satisfying assignment, if we're processing SCC of (var, val),
                # and (var, 1-val) was already processed (i.e. is in a previous SCC),
                # then we must have (var, 1-val) in a lower SCC id, meaning 
                # SCC of (var, 1-val) is later in topological order than SCC of (var, val)
                # which means (var, 1-val) ->* (var, val) in implication graph,
                # so (var, val) should be True.
                # Wait, that's not right.
                # Let me think of a standard way.
                # In the condensation graph, there's an edge SCC(u) -> SCC(v) if there's u->v in original.
                # Kosaraju finds SCCs in reverse topological order of condensation.
                # So first found SCC is a sink in condensation.
                # When processing SCCs in the order found (reverse topological):
                # for each unassigned variable in the SCC, we can assign it any value that's consistent.
                # But to satisfy all implications, if there's a path from u to v and we set u to False,
                # then v must be False. 
                # The standard approach:
                # Process SCCs in topological order of condensation (reverse of discovery order).
                # For each variable not yet assigned, if its negation was assigned, it's determined.
                # Otherwise, we can choose. Standard is to set to False.
                # But we need to be more careful.
                # Actually, there's a simpler criterion:
                # For variable x_i, let's look at SCC(x_i, True) and SCC(x_i, False).
                # If SCC index of (x_i, True) < SCC index of (x_i, False), 
                # it means (x_i, True) was discovered before (x_i, False) in DFS2,
                # which means (x_i, False) is processed first in the topological order of SCCs,
                # which means in a satisfying assignment we should set x_i to False.
                # If the index is >, we should set x_i to True.
                # If =, it's unsatisfiable - but we already checked that.
                pass
    
    # Simpler: for each variable, check which of (i,0) and (i,1) has higher SCC id.
    # Higher SCC id means it was discovered first in DFS2, which means it's processed earlier 
    # in the topological order of SCCs in the condensation.
    # In a valid assignment, we want to set variables such that we don't force 
    # a node in an earlier SCC (in topological order) to be true when it should be false.
    # The standard way: process SCCs in topological order (reverse of Kosaraju discovery order).
    # When we process an SCC, for each variable in it not yet assigned, 
    # we set it to make its positive literal false (i.e. variable = False).
    # But if we set variable i to False, we're setting (i,1) to False and (i,0) to True.
    # If (i,0) is in an SCC that was discovered later (higher SCC id), 
    # that means it's later in topological order, which is consistent.
    # So the rule is: for each variable i, if scc[(i,1)] < scc[(i,0)] (discovered earlier), 
    # set i to False. Otherwise set i to True.
    
    result = [0] * (n + 1)  # 1-indexed
    for i in range(1, n + 1):
        scc_true = scc.get((i, 1), -1)
        scc_false = scc.get((i, 0), -1)
        if scc_true < scc_false:
            result[i] = 0
        else:
            result[i] = 1
    
    print("YES")
    print(" ".join(map(str, result[1:])))

if __name__ == "__main__":
    main()
import sys
from collections import defaultdict

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
    
    # For each dependency (l1, l2), we create implications
    # If l1 is False, then l2 must be True
    # If l2 is False, then l1 must be True
    # This is a 2-SAT problem
    
    # We'll use implication graph and solve with SCC
    # Variables: for relay i, variable i (1-based) represents relay i active
    # Literal values: positive = active, negative = dormant
    # So x_i = 1 means relay i is active, x_i = 0 means dormant
    # -x_i = 1 means relay i is dormant, -x_i = 0 means active
    
    # For each clause (l1 or l2), we add edges:
    # not l1 -> l2 and not l2 -> l1
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    def add_implication(x, y):
        # x => y
        adj[x].append(y)
        rev_adj[y].append(x)
    
    idx = 2
    while idx < len(data):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        # Clause: l1 or l2
        # This is equivalent to: (not l1 => l2) and (not l2 => l1)
        
        # not l1 => l2
        if l1 > 0:
            # not (x_l1) => x_l2
            add_implication(-l1, l2)
        else:
            # not (not x_|l1|) => x_|l1|
            # which is x_|l1| => x_|l1| (always true, can ignore)
            # Actually: not (-relay) = relay
            # so not l1 = |l1| => l2 
            add_implication(abs(l1), l2)
            
        if l2 > 0:
            # not (x_l2) => x_l1  
            add_implication(-l2, l1)
        else:
            # not (-x_|l2|) => x_l1
            # which is x_|l2| => x_l1
            add_implication(abs(l2), l1)
            
        # Let me re-think this more carefully
        # l1 or l2 means at least one of them is true
        # not l1 => l2   and   not l2 => l1
        # 
        # If l1 = +i (relay i active), then not l1 = (relay i dormant) = -i
        # If l1 = -i (relay i dormant), then not l1 = (relay i active) = +i
        #
        # So:
        # not l1 => l2 translates to:
        #   if l1 > 0: -l1 => l2
        #   if l1 < 0: abs(l1) => l2
        # Similarly for not l2 => l1
        
        not_l1 = -l1 if l1 > 0 else abs(l1)
        not_l2 = -l2 if l2 > 0 else abs(l2)
        
        add_implication(not_l1, l2)
        add_implication(not_l2, l1)
    
    # Now we do Kosaraju's algorithm to find SCCs
    visited = set()
    order = []
    
    def dfs1(u):
        if u in visited:
            return
        visited.add(u)
        for v in adj[u]:
            dfs1(v)
        order.append(u)
    
    # Run DFS1 on all nodes
    nodes = set()
    for u in adj:
        nodes.add(u)
    for u in rev_adj:
        nodes.add(u)
        
    for u in nodes:
        dfs1(u)
    
    # Reverse the order
    order.reverse()
    
    # Second DFS to find SCCs
    visited.clear()
    scc_id = {}
    current_scc = 0
    
    def dfs2(u):
        if u in visited:
            return
        visited.add(u)
        scc_id[u] = current_scc
        for v in rev_adj[u]:
            dfs2(v)
    
    for u in order:
        if u not in visited:
            dfs2(u)
            current_scc += 1
            
    # Check if for any variable x, x and -x are in the same SCC
    for i in range(1, n+1):
        if scc_id.get(i, -1) == scc_id.get(-i, -2):
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    # Variables in later SCCs (higher index) should be assigned TRUE
    assignment = {}
    
    # Create mapping from SCC id to literals in that SCC
    scc_literals = defaultdict(list)
    for lit, sid in scc_id.items():
        scc_literals[sid].append(lit)
    
    # Process SCCs in reverse topological order (lowest to highest SCC id works here)
    # Actually, we want to process in the order that Kosaraju found them reversed,
    # but since we used the finish times, we process in increasing order of SCC ids
    
    for sid in sorted(scc_literals.keys()):
        for lit in scc_literals[sid]:
            if lit not in assignment and -lit not in assignment:
                # Assign FALSE to this literal, TRUE to its negation would put -lit in a later SCC
                # No, let's think differently:
                # In 2-SAT, if a literal and its negation are in different SCCs,
                # and the literal's SCC comes AFTER the negation's SCC in the topological sort,
                # then the literal should be TRUE.
                
                # But in our case, we have to be careful about the meaning.
                # Let's just assign values properly:
                # If we process SCCs in topological order, and when we process an SCC,
                # if neither x nor -x has been assigned yet, we can assign x = False.
                
                # But actually, there's a simpler way:
                # The SCCs form a DAG. If we process them in topological order,
                # and for each unassigned variable, we assign it false if it appears
                # in an earlier SCC than its negation, or true otherwise.
                
                # Even simpler approach:
                # Go through all variables. For each unassigned variable x:
                # if SCC(x) comes before SCC(-x) in topological order, set x = False
                # else set x = True
                
                # But how do we determine the topological order?
                # In Kosaraju, the 'order' list gives vertices in reverse finish time order
                # The first vertex in 'order' finishes last, so is in a sink SCC
                # The last vertex in 'order' finishes first, so is in a source SCC
                
                # So SCCs should be processed in the order they appear in the transposed graph DFS
                # which is the reverse of 'order'
                
                # Let's build a finishing time map
                finish_time = {u: i for i, u in enumerate(order)}
                
                if finish_time.get(lit, -1) < finish_time.get(-lit, float('inf')):
                    assignment[lit] = False
                    assignment[-lit] = True
                else:
                    assignment[lit] = True
                    assignment[-lit] = False
    
    # Output result
    result = []
    for i in range(1, n+1):
        if assignment.get(i, False):  # Default to False if not constrained
            result.append("1")
        else:
            result.append("0")
            
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()
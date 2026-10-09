import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # If there are no requirements, any assignment works
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build implication graph
    # Each variable x_i has two nodes: 2*i (for x_i = 0) and 2*i+1 (for x_i = 1)
    # But we'll use a more intuitive approach with variables and their negations
    
    # For each variable i (1-based), we have:
    # i represents x_i = 1 (day)
    # -i represents x_i = 0 (night)
    
    # For clause (a OR b), we add edges (-a -> b) and (-b -> a)
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    idx = 2
    clauses = []
    while idx < len(data):
        a = int(data[idx])
        b = int(data[idx+1])
        clauses.append((a, b))
        idx += 2
        
        # Add implications: (-a => b) and (-b => a)
        adj[-a].append(b)
        adj[-b].append(a)
        rev_adj[b].append(-a)
        rev_adj[a].append(-b)
    
    # Now we do Kosaraju's algorithm to check for contradictions
    # Nodes are scene numbers with signs
    
    visited = set()
    order = []
    
    def dfs1(u):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                dfs1(v)
        order.append(u)
    
    # Collect all nodes
    all_nodes = set()
    for a, b in clauses:
        all_nodes.add(a)
        all_nodes.add(-a)
        all_nodes.add(b)
        all_nodes.add(-b)
        
    for node in all_nodes:
        if node not in visited:
            dfs1(node)
    
    # Second DFS on reverse graph
    visited.clear()
    components = {}
    comp_num = 0
    
    def dfs2(u):
        visited.add(u)
        components[u] = comp_num
        for v in rev_adj[u]:
            if v not in visited:
                dfs2(v)
                
    while order:
        u = order.pop()
        if u not in visited:
            dfs2(u)
            comp_num += 1
            
    # Check for contradiction: variable and its negation in same component
    for i in range(1, n+1):
        if components.get(i, -1) == components.get(-i, -2):
            print("NO")
            return
            
    # If no contradiction, build assignment
    # Assign values based on component numbers
    assignment = {}
    
    # Process components in reverse topological order
    # We can get this by processing the finishing times from first DFS
    # But since we stored them in 'order', and popped them off, 
    # the components were assigned in reverse topological order
    
    # Actually, let's re-process the components properly
    
    # Create mapping from component number to list of nodes
    comp_to_nodes = defaultdict(list)
    for node, c in components.items():
        comp_to_nodes[c].append(node)
        
    # Process components in topological order (reverse of finishing time of first DFS)
    # Since we appended in dfs1 and then popped from end, the last finished is first processed in dfs2
    # So component numbers are already in a useful order
    
    # Let's just assign truth values
    assigned = {}
    
    # Go through components in reverse order of finishing time (which corresponds to topological order in condensation)
    # In our case, since we used the order from first DFS and processed in reverse,
    # higher comp_num was assigned later, so lower comp_num corresponds to earlier in topological order
    
    for c in sorted(comp_to_nodes.keys()):
        for node in comp_to_nodes[c]:
            var = abs(node)
            if var not in assigned:
                # If node is positive literal, set variable to True
                # If node is negative literal, set variable to False
                if node > 0:
                    assigned[var] = 1
                else:
                    assigned[var] = 0
                    
    # But we need to be more careful. 
    # In Kosaraju, when we process a component, if any literal in it is unassigned,
    # we can set all literals consistently.
    # However, it's easier to think in terms of: for each variable, 
    # if var and -var are in different components, 
    # and the component containing var is reachable after the one with -var in the topological order,
    # then var should be True.
    
    # Simpler approach: 
    # Go through components in topological order (increasing comp_num),
    # and for each unassigned variable in the component, 
    # if the component also contains the negation, it's unsat.
    # Otherwise, assign according to the literal sign.
    
    # But actually, we already checked for contradiction.
    # Now we just need to extract a satisfying assignment.
    
    # Let's rebuild: for each variable, decide its value
    val = [None] * (n+1)  # 1-indexed
    
    # Process components in reverse topological order of SCC DAG
    # That means process component numbers in decreasing order
    # because in first DFS, the sink components finish first
    
    for c in sorted(comp_to_nodes.keys(), reverse=True):
        for node in comp_to_nodes[c]:
            var = abs(node)
            if val[var] is None:
                if node > 0:
                    val[var] = 1
                else:
                    val[var] = 0
                    
    # But wait, this might not be right either.
    # Correct way: in the condensation graph (DAG of SCCs),
    # process sources first. Sources are SCCs with no incoming edges.
    # In terms of our numbering, it's complex.
    
    # Let's take a simpler route:
    # We know there's no contradiction.
    # So for each variable, in the two SCCs that contain var and -var,
    # one comes before the other in topological order.
    # We want to set the variable according to which SCC was processed later in dfs2.
    
    # Recall: in dfs2, we process in order of the 'order' list (popped from end).
    # So the last things we process in dfs2 are the "sink" components in the original graph,
    # which are "source" components in the condensation.
    
    # Therefore, if a variable appears positively in a component processed later,
    # we should set it to true.
    
    # To implement correctly, let's track when each variable was assigned
    val = [None] * (n+1)
    
    # Process components in the order they were discovered in dfs2 (which is reverse topological)
    # So first discovered component in dfs2 is actually a source in the condensation
    for c in range(comp_num):  # comp_num is total number of components
        for node in comp_to_nodes[c]:
            var = abs(node)
            if val[var] is None:
                if node > 0:
                    val[var] = 1
                else:
                    val[var] = 0
                    
    # Output result
    print("YES")
    res = []
    for i in range(1, n+1):
        if val[i] is None:
            res.append("1")  # Default to day if unconstrained
        else:
            res.append(str(val[i]))
    print(" ".join(res))

if __name__ == "__main__":
    main()
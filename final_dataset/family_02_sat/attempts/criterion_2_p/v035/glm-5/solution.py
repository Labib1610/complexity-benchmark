import sys

# Increase recursion depth for deep DFS calls
sys.setrecursionlimit(300000)

def solve():
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Total nodes in implication graph: 2 * n
    # Node indices:
    # 2*i     -> Switch i is OFF (0)
    # 2*i + 1 -> Switch i is ON  (1)
    # For 1-based switch index k (1 <= k <= n):
    # Node for k is ON:  2*(k-1) + 1
    # Node for -k is ON: 2*(k-1)
    
    total_nodes = 2 * n
    adj = [[] for _ in range(total_nodes)]
    rev_adj = [[] for _ in range(total_nodes)]

    for _ in range(m):
        try:
            u_cond = int(next(iterator))
            v_cond = int(next(iterator))
        except StopIteration:
            break
        
        # Process condition u_cond
        # If u_cond > 0, it means switch u_cond is ON.
        # If u_cond < 0, it means switch |u_cond| is OFF.
        
        # Calculate node indices for the conditions being TRUE
        # u_node: node index if u_cond is satisfied
        # v_node: node index if v_cond is satisfied
        
        # Helper to get node index for a condition being TRUE
        # val > 0: switch val is ON -> node 2*(val-1) + 1
        # val < 0: switch |val| is OFF -> node 2*(|val|-1)
        
        if u_cond > 0:
            u_node = 2 * (u_cond - 1) + 1
        else:
            u_node = 2 * (-u_cond - 1)
            
        if v_cond > 0:
            v_node = 2 * (v_cond - 1) + 1
        else:
            v_node = 2 * (-v_cond - 1)
            
        # The rule is (u_cond OR v_cond).
        # This implies:
        # NOT u_cond -> v_cond
        # NOT v_cond -> u_cond
        
        # NOT u_node is the opposite state for the same switch.
        # If u_node is ON-state, NOT u_node is OFF-state (u_node ^ 1).
        # If u_node is OFF-state, NOT u_node is ON-state (u_node ^ 1).
        
        not_u = u_node ^ 1
        not_v = v_node ^ 1
        
        adj[not_u].append(v_node)
        adj[not_v].append(u_node)
        
        rev_adj[v_node].append(not_u)
        rev_adj[u_node].append(not_v)

    # Kosaraju's Algorithm for Strongly Connected Components
    
    # 1. First DFS: compute finishing order
    visited = [False] * total_nodes
    order = []
    
    # Using an explicit stack to avoid recursion limit issues
    # Though sys.setrecursionlimit is set, iterative is safer for N=10^5
    
    for i in range(total_nodes):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                curr, idx = stack[-1]
                if not visited[curr]:
                    visited[curr] = True
                
                # Explore neighbors
                if idx < len(adj[curr]):
                    neighbor = adj[curr][idx]
                    stack[-1] = (curr, idx + 1)
                    if not visited[neighbor]:
                        stack.append((neighbor, 0))
                else:
                    stack.pop()
                    order.append(curr)

    # 2. Second DFS: process in reverse order of finishing times
    visited = [False] * total_nodes
    comp_id = [-1] * total_nodes
    
    current_id = 0
    for u in reversed(order):
        if not visited[u]:
            # DFS on rev_adj
            stack = [u]
            visited[u] = True
            component_nodes = []
            
            while stack:
                curr = stack.pop()
                component_nodes.append(curr)
                
                for neighbor in rev_adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            for node in component_nodes:
                comp_id[node] = current_id
            current_id += 1

    # Check for contradictions
    # For each switch i (0 to n-1), check if ON and OFF states are in the same SCC
    for i in range(n):
        on_node = 2 * i + 1
        off_node = 2 * i
        if comp_id[on_node] == comp_id[off_node]:
            sys.stdout.write("NO\n")
            return

    # Construct assignment
    # If comp_id[ON] > comp_id[OFF], then ON is topologically 'later' (or equal),
    # meaning OFF does not imply ON, so we can pick OFF.
    # Actually, in standard SCC condensation graph (edges reversed from original),
    # or simply: if comp_id[a] > comp_id[b], a is 'closer to sink' in the original graph.
    # If comp_id[ON] > comp_id[OFF], it means ON is processed later in the topological sort.
    # If there was a path OFF -> ON, then OFF would be processed after ON (or same SCC).
    # Since they are different SCCs, comp_id[ON] > comp_id[OFF] implies no path OFF -> ON.
    # Thus, we can set switch to OFF.
    # Conversely, if comp_id[ON] < comp_id[OFF], there is no path ON -> OFF, so we set to ON.
    
    # Wait, the standard logic is:
    # Process SCCs in topological order. If we haven't assigned a value to a variable,
    # set it to FALSE (0). This forces its negation to TRUE.
    # Since we process in topological order, setting a variable to FALSE ensures
    # no later SCC will force it to TRUE (which would be a contradiction).
    
    # The order of SCCs is 0, 1, ..., num_sccs-1.
    # comp_id[u] gives the topological order (reversed).
    # Actually, Kosaraju gives components in topological order of the component graph.
    # If comp_id[u] < comp_id[v], u comes before v in topological sort.
    # We want to assign FALSE to variables in earlier components.
    
    # Let's stick to the comp_id comparison logic which is robust:
    # If comp_id[ON] < comp_id[OFF], then ON is topologically earlier.
    # Assigning FALSE to ON means we pick OFF.
    # If comp_id[ON] > comp_id[OFF], then OFF is topologically earlier.
    # Assigning FALSE to OFF means we pick ON.
    
    # Simplified:
    # If comp_id[ON] > comp_id[OFF]: result[i] = 1
    # If comp_id[ON] < comp_id[OFF]: result[i] = 0
    
    result = []
    for i in range(n):
        on_node = 2 * i + 1
        off_node = 2 * i
        if comp_id[on_node] > comp_id[off_node]:
            result.append(1)
        else:
            result.append(0)

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, result)) + "\n")

if __name__ == '__main__':
    solve()
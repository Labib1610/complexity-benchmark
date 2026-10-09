import sys

# Increase recursion depth just in case, though we use iterative DFS.
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for 2-SAT graph
    # Nodes: 0 to 2n-1
    # Node 2*i corresponds to s[i] = 0
    # Node 2*i + 1 corresponds to s[i] = 1
    adj = [[] for _ in range(2 * n)]
    
    # Helper to add implication u -> v
    def add_implication(u, v):
        adj[u].append(v)

    for _ in range(m):
        try:
            l1 = int(next(iterator))
            l2 = int(next(iterator))
        except StopIteration:
            break
        
        # We process l1 then l2.
        # We need Z_final < 3.
        # The transformation rules are:
        # v > 0: if s=0, Z -> 2Z+1; if s=1, Z -> Z
        # v < 0: if s=1, Z -> 2Z+1; if s=0, Z -> Z
        
        # We analyze based on the value of Z before processing v.
        # If Z < 2, then 2Z+1 < 3. The operation is safe.
        # If Z >= 2, then 2Z+1 >= 5. The operation fails.
        # So, if Z >= 2, we must avoid the 2Z+1 update.
        
        # Processing l1:
        # Z starts at 0 (< 2).
        # If l1 requires 2Z+1 update, Z becomes 1. Safe.
        # If l1 requires Z update, Z remains 0. Safe.
        # So l1 is always safe, but it sets Z for l2.
        # Z_after_l1 is 1 if update happened, 0 otherwise.
        
        # Determine condition for update on l1
        # update1 happens if:
        # l1 > 0 and s_{|l1|} = 0  =>  implies s_{|l1|} = 1 avoids update
        # l1 < 0 and s_{|l1|} = 1  =>  implies s_{|l1|} = 0 avoids update
        
        # Let's denote the state of hub |v| that causes update as "bad_state_for_v"
        # and the state that avoids update as "good_state_for_v".
        # For l1, if bad_state happens, Z becomes 1.
        # For l2, if Z=1 and bad_state happens, Z becomes 3 (Fail).
        # So if l1 causes update, l2 MUST NOT cause update.
        # Implication: (l1 causes update) => (l2 does not cause update)
        
        u = abs(l1) - 1
        v = abs(l2) - 1
        
        # Determine states for l1
        if l1 > 0:
            # update if s[u] = 0
            # bad: 0, good: 1
            l1_bad_state = 0
            l1_good_state = 1
        else:
            # update if s[u] = 1
            # bad: 1, good: 0
            l1_bad_state = 1
            l1_good_state = 0
            
        # Determine states for l2
        if l2 > 0:
            # update if s[v] = 0
            l2_bad_state = 0
            l2_good_state = 1
        else:
            # update if s[v] = 1
            l2_bad_state = 1
            l2_good_state = 0
            
        # Add implication: s[u] == l1_bad_state => s[v] == l2_good_state
        # Node indices: 2*i for state 0, 2*i+1 for state 1
        u_node = 2 * u + l1_bad_state
        v_node = 2 * v + l2_good_state
        add_implication(u_node, v_node)
        
        # We also need the contrapositive: s[v] == l2_bad_state => s[u] == l1_good_state
        u_node_contra = 2 * u + l1_good_state
        v_node_contra = 2 * v + l2_bad_state
        add_implication(v_node_contra, u_node_contra)

    # Kosaraju's algorithm to find SCCs and topological order
    num_nodes = 2 * n
    visited = [False] * num_nodes
    order = []
    
    # DFS on original graph to get finish times
    # Using stack to avoid recursion limit issues
    for start_node in range(num_nodes):
        if not visited[start_node]:
            stack = [(start_node, 0)]
            while stack:
                node, idx = stack[-1]
                if not visited[node]:
                    visited[node] = True
                    while idx < len(adj[node]):
                        neighbor = adj[node][idx]
                        if not visited[neighbor]:
                            break
                        idx += 1
                    if idx < len(adj[node]):
                        stack[-1] = (node, idx + 1)
                        stack.append((neighbor, 0))
                    else:
                        stack.pop()
                        order.append(node)
                else:
                    stack.pop()

    # Reverse graph
    rev_adj = [[] for _ in range(num_nodes)]
    for u in range(num_nodes):
        for v in adj[u]:
            rev_adj[v].append(u)
            
    # DFS on reversed graph in order of decreasing finish times
    visited = [False] * num_nodes
    comp_id = [-1] * num_nodes
    current_comp_id = 0
    
    for node in reversed(order):
        if not visited[node]:
            # Assign component ID
            stack = [node]
            visited[node] = True
            comp_id[node] = current_comp_id
            while stack:
                curr = stack.pop()
                for neighbor in rev_adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        comp_id[neighbor] = current_comp_id
                        stack.append(neighbor)
            current_comp_id += 1
            
    # Check for contradictions and assign states
    result = [0] * n
    possible = True
    
    for i in range(n):
        node0 = 2 * i
        node1 = 2 * i + 1
        if comp_id[node0] == comp_id[node1]:
            possible = False
            break
        # If comp_id of state 1 is greater, it appears later in topological order,
        # meaning it is not reachable from state 0.
        # We can pick state 1.
        if comp_id[node1] > comp_id[node0]:
            result[i] = 1
        else:
            result[i] = 0
            
    if not possible:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, result)) + "\n")

if __name__ == '__main__':
    solve()
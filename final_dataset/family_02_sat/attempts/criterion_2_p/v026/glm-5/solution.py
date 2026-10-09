import sys
from collections import deque

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

    # 2-SAT setup: variables are 1 to n, each has two states (0 and 1)
    # Node indices: 2*i for False (standby), 2*i+1 for True (active), 0-indexed i
    # Total nodes: 2*n
    num_nodes = 2 * n
    adj = [[] for _ in range(num_nodes)]
    radj = [[] for _ in range(num_nodes)]

    def get_node_indices(val):
        """Returns (node_index, negated_node_index) for a literal."""
        # val > 0: component val is active (True)
        # val < 0: component |val| is standby (False)
        comp = abs(val) - 1
        if val > 0:
            return (2 * comp + 1, 2 * comp)
        else:
            return (2 * comp, 2 * comp + 1)

    for _ in range(m):
        try:
            u_val = int(next(iterator))
            v_val = int(next(iterator))
        except StopIteration:
            break
        
        u_node, u_neg = get_node_indices(u_val)
        v_node, v_neg = get_node_indices(v_val)
        
        # Clause: (u OR v) <=> (!u -> v) and (!v -> u)
        adj[u_neg].append(v_node)
        adj[v_neg].append(u_node)
        
        radj[v_node].append(u_neg)
        radj[u_node].append(v_neg)

    # Kosaraju's algorithm for SCCs
    visited = [False] * num_nodes
    order = []
    
    for i in range(num_nodes):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, idx = stack[-1]
                if not visited[node]:
                    visited[node] = True
                
                if idx < len(adj[node]):
                    neighbor = adj[node][idx]
                    stack[-1] = (node, idx + 1)
                    if not visited[neighbor]:
                        stack.append((neighbor, 0))
                else:
                    stack.pop()
                    order.append(node)

    scc_id = [-1] * num_nodes
    current_id = 0
    
    for node in reversed(order):
        if scc_id[node] == -1:
            stack = [node]
            scc_id[node] = current_id
            while stack:
                curr = stack.pop()
                for neighbor in radj[curr]:
                    if scc_id[neighbor] == -1:
                        scc_id[neighbor] = current_id
                        stack.append(neighbor)
            current_id += 1

    # Check for unsatisfiability
    for i in range(n):
        if scc_id[2 * i] == scc_id[2 * i + 1]:
            sys.stdout.write("NO\n")
            return

    # Topological order of SCCs is the reverse of finishing order
    # Nodes finished later (appearing earlier in reversed `order`) have higher topological order
    # We want to assign False if topological order of `True` node < `False` node
    # Which means we check if scc_id[true] < scc_id[false] (since we assigned IDs in topological order)
    
    assignment = [0] * n
    for i in range(n):
        # Node for True is 2*i+1, for False is 2*i
        if scc_id[2 * i + 1] > scc_id[2 * i]:
            assignment[i] = 1
        else:
            assignment[i] = 0

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, assignment)) + "\n")

if __name__ == '__main__':
    solve()
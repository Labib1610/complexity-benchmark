import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        
        # Clause: (x_u or x_v)
        # u > 0 means x_u=1, u < 0 means x_{|u|}=0
        # Map to indices: 2*(val-1) for False, 2*(val-1)+1 for True
        # u > 0: literal is x_u=1. If False (x_u=0), implies v must be True.
        #        Edge: not(u) -> v. not(u) is index 2*(u-1). v is mapped accordingly.
        # u < 0: literal is x_{|u|}=0. If False (x_{|u|}=1), implies v must be True.
        #        Edge: not(u) -> v. not(u) is index 2*(|u|-1)+1.
        
        def get_node(val):
            # Returns index for the literal being True
            val_abs = abs(val) - 1
            if val > 0:
                return 2 * val_abs + 1
            else:
                return 2 * val_abs
        
        u_node = get_node(u)
        v_node = get_node(v)
        
        # not u -> v
        adj[u_node ^ 1].append(v_node)
        # not v -> u
        adj[v_node ^ 1].append(u_node)
    
    # Kosaraju's algorithm to find SCCs
    N = 2 * n
    visited = [False] * N
    order = []
    
    for i in range(N):
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
    
    # Process in reverse order of finishing times
    comp_id = [-1] * N
    current_comp = 0
    
    # Build reverse graph
    rev_adj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            rev_adj[v].append(u)
            
    for u in reversed(order):
        if comp_id[u] == -1:
            stack = [u]
            comp_id[u] = current_comp
            while stack:
                curr = stack.pop()
                for neighbor in rev_adj[curr]:
                    if comp_id[neighbor] == -1:
                        comp_id[neighbor] = current_comp
                        stack.append(neighbor)
            current_comp += 1
    
    # Check satisfiability and assign values
    assignment = [0] * n
    for i in range(n):
        node_true = 2 * i + 1
        node_false = 2 * i
        if comp_id[node_true] == comp_id[node_false]:
            print("NO")
            return
        assignment[i] = 1 if comp_id[node_true] > comp_id[node_false] else 0
    
    print("YES")
    print(*(assignment))

if __name__ == "__main__":
    solve()
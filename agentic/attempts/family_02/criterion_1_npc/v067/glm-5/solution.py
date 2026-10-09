import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT setup
    # Variable x_i: True means ACTIVE (1), False means INACTIVE (0)
    # Node indices: 0 to 2n-1
    # For channel i (1-indexed): 
    #   True node: 2*(i-1)
    #   False node: 2*(i-1) + 1
    
    adj = [[] for _ in range(2 * n)]
    
    def get_node(channel, is_active):
        # channel is 1-indexed
        # is_active is True for ACTIVE, False for INACTIVE
        idx = (channel - 1) * 2
        if is_active:
            return idx
        else:
            return idx + 1
    
    def add_implication(u, v):
        adj[u].append(v)
    
    # Process each check
    # A check passes if at least one condition is met.
    # Condition: channel j should be mode M.
    # If M is ACTIVE, condition is (x_j == True).
    # If M is INACTIVE, condition is (x_j == False).
    #
    # For a check with conditions c1, c2, c3:
    # (c1 or c2 or c3) must be true.
    # This is equivalent to:
    # (not c1 -> c2) and (not c1 -> c3) and
    # (not c2 -> c1) and (not c2 -> c3) and
    # (not c3 -> c1) and (not c3 -> c2)
    
    for _ in range(m):
        l = [int(next(it)) for _ in range(3)]
        nodes = []
        for val in l:
            channel = abs(val)
            is_active = (val > 0)
            nodes.append(get_node(channel, is_active))
        
        u1, u2, u3 = nodes
        v1, v2, v3 = u1 ^ 1, u2 ^ 1, u3 ^ 1 # Negations
        
        add_implication(v1, u2)
        add_implication(v1, u3)
        add_implication(v2, u1)
        add_implication(v2, u3)
        add_implication(v3, u1)
        add_implication(v3, u2)
    
    # Kosaraju's algorithm to find SCCs and topological order
    N = 2 * n
    adj_rev = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            adj_rev[v].append(u)
            
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                child = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[child]:
                    stack.append((child, 0))
            else:
                stack.pop()
                order.append(node)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
            
    component = [-1] * N
    comp_id = 0
    
    for u in reversed(order):
        if component[u] == -1:
            # DFS on reverse graph
            stack = [u]
            component[u] = comp_id
            while stack:
                node = stack.pop()
                for child in adj_rev[node]:
                    if component[child] == -1:
                        component[child] = comp_id
                        stack.append(child)
            comp_id += 1
            
    # Check for unsatisfiability
    for i in range(n):
        if component[2*i] == component[2*i + 1]:
            print("NO")
            return
            
    # Assign values
    # If component of TRUE node is greater than FALSE node, set to TRUE
    # Because in reverse topological order (which we used for labeling),
    # higher component ID means it appears earlier in the original topological sort,
    # meaning it can reach the lower ID components.
    # Actually, standard Kosaraju assigns components in reverse topological order.
    # So if comp[True] > comp[False], True is "later" in the SCC DAG, 
    # meaning False can reach True. If we pick True, False must be False (consistent).
    # Wait, standard logic: if comp[x] > comp[!x], then x should be true.
    
    result = [0] * n
    for i in range(n):
        if component[2*i] > component[2*i + 1]:
            result[i] = 1
            
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == '__main__':
    solve()
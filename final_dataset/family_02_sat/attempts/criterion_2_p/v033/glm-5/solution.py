import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT problem
    # Variables: x1, ..., xn. Each can be true (1) or false (0).
    # Literals: +x (xi is 1), -x (xi is 0).
    # Indices for literals in implication graph:
    # Graph has 2*n nodes.
    # Node 2*i:     variable i+1 is False (literal -i)
    # Node 2*i + 1: variable i+1 is True  (literal +i)
    
    N_nodes = 2 * n
    adj = [[] for _ in range(N_nodes)]
    
    def get_node(var):
        # var is positive => switch var is 1 => node index 2*(var-1) + 1
        # var is negative => switch |var| is 0 => node index 2*(|var|-1)
        idx = abs(var) - 1
        if var > 0:
            return 2 * idx + 1
        else:
            return 2 * idx
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        
        # Rule: (literal u) OR (literal v) must be true.
        # This implies: NOT u => v  AND  NOT v => u
        
        # NOT u is the negation of literal u.
        # If u is +x (True), NOT u is -x (False). Nodes: u=2x+1, ~u=2x.
        # If u is -x (False), NOT u is +x (True). Nodes: u=2x, ~u=2x+1.
        
        u_node = get_node(u)
        v_node = get_node(v)
        
        u_neg = u_node ^ 1
        v_neg = v_node ^ 1
        
        adj[u_neg].append(v_node)
        adj[v_neg].append(u_node)
        
    # Kosaraju's algorithm to find SCCs
    visited = [False] * N_nodes
    order = []
    
    for i in range(N_nodes):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, idx = stack[-1]
                if not visited[node]:
                    visited[node] = True
                
                found_next = False
                limit = len(adj[node])
                while idx < limit:
                    nei = adj[node][idx]
                    stack[-1] = (node, idx + 1)
                    if not visited[nei]:
                        stack.append((nei, 0))
                        found_next = True
                        break
                    idx += 1
                
                if not found_next:
                    stack.pop()
                    order.append(node)
                    
    # Second pass on reversed graph
    rev_adj = [[] for _ in range(N_nodes)]
    for u in range(N_nodes):
        for v in adj[u]:
            rev_adj[v].append(u)
            
    comp_id = [-1] * N_nodes
    cid = 0
    for u in reversed(order):
        if comp_id[u] == -1:
            stack = [u]
            comp_id[u] = cid
            while stack:
                node = stack.pop()
                for nei in rev_adj[node]:
                    if comp_id[nei] == -1:
                        comp_id[nei] = cid
                        stack.append(nei)
            cid += 1
            
    # Check for contradiction: x and NOT x in same SCC
    for i in range(n):
        if comp_id[2*i] == comp_id[2*i+1]:
            print("NO")
            return
            
    # Construct assignment
    assignment = [0] * n
    # If comp_id[True] > comp_id[False], set to True (topological order)
    for i in range(n):
        if comp_id[2*i+1] > comp_id[2*i]:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    print("YES")
    print(*(assignment))

if __name__ == '__main__':
    solve()
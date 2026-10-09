import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # Build implication graph for 2-SAT
    # Variables: x_1, ..., x_n (True = active, False = inactive)
    # Node indices: 0 to 2n-1
    # For variable i (1-indexed): 
    #   True node: 2*(i-1)
    #   False node: 2*(i-1) + 1
    
    adj = [[] for _ in range(2 * n)]
    
    def get_node(var, is_true):
        # var is 1-indexed component number
        return 2 * (var - 1) + (0 if is_true else 1)
    
    def add_implication(u, v):
        adj[u].append(v)
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        l3 = int(next(it))
        
        # Parse conditions: positive means active, negative means inactive
        conditions = []
        for val in [l1, l2, l3]:
            comp = abs(val)
            is_active = val > 0
            conditions.append((comp, is_active))
        
        # For each condition, add implications from negation to other conditions
        for i in range(3):
            comp_i, is_active_i = conditions[i]
            u = get_node(comp_i, not is_active_i)  # negation of condition i
            
            for j in range(3):
                if i != j:
                    comp_j, is_active_j = conditions[j]
                    v = get_node(comp_j, is_active_j)
                    add_implication(u, v)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(v):
        stack = [(v, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
            if idx < len(adj[node]):
                stack.append((node, idx + 1))
                if not visited[adj[node][idx]]:
                    stack.append((adj[node][idx], 0))
            else:
                order.append(node)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Build reverse graph
    radj = [[] for _ in range(2 * n)]
    for u in range(2 * n):
        for v in adj[u]:
            radj[v].append(u)
    
    visited = [False] * (2 * n)
    comp_id = [-1] * (2 * n)
    current_comp = 0
    
    def dfs2(v, cid):
        stack = [v]
        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            comp_id[node] = cid
            for neighbor in radj[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    
    for v in reversed(order):
        if not visited[v]:
            dfs2(v, current_comp)
            current_comp += 1
    
    # Check satisfiability and assign values
    assignment = [False] * n
    
    for i in range(n):
        true_node = 2 * i
        false_node = 2 * i + 1
        if comp_id[true_node] == comp_id[false_node]:
            print("NO")
            return
        assignment[i] = comp_id[true_node] > comp_id[false_node]
    
    print("YES")
    print(' '.join('1' if x else '0' for x in assignment))

if __name__ == "__main__":
    solve()
import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    clauses = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        index += 2
        clauses.append((l1, l2))
    
    # Build implication graph
    # Variables: 1..n (positive), -1..-n (negative)
    # Nodes: 1..n for x_i, n+1..2n for not x_i
    # node i (1<=i<=n) represents x_i
    # node i+n represents not x_i
    
    adj = [[] for _ in range(2*n + 1)]
    rev_adj = [[] for _ in range(2*n + 1)]
    
    def var_to_node(x):
        if x > 0:
            return x
        else:
            return n + (-x)
    
    def node_to_var(node):
        if node <= n:
            return node
        else:
            return -(node - n)
    
    # For each clause (l1 or l2), we add edges:
    # (not l1) => l2  and (not l2) => l1
    for l1, l2 in clauses:
        # not l1 => l2
        adj[var_to_node(-l1)].append(var_to_node(l2))
        rev_adj[var_to_node(l2)].append(var_to_node(-l1))
        
        # not l2 => l1
        adj[var_to_node(-l2)].append(var_to_node(l1))
        rev_adj[var_to_node(l1)].append(var_to_node(-l2))
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2*n + 1)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(1, 2*n + 1):
        if not visited[i]:
            dfs1(i)
    
    # Transpose graph DFS
    visited = [False] * (2*n + 1)
    components = [-1] * (2*n + 1)
    component_nodes = []
    
    def dfs2(u, comp_num):
        visited[u] = True
        components[u] = comp_num
        component_nodes[comp_num].append(u)
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, comp_num)
    
    comp_num = 0
    while order:
        u = order.pop()
        if not visited[u]:
            component_nodes.append([])
            dfs2(u, comp_num)
            comp_num += 1
    
    # Check for contradictions
    assignment = [-1] * (n+1)  # 1-indexed
    
    for c in range(comp_num):
        nodes = component_nodes[c]
        for node in nodes:
            var = node_to_var(node)
            if var > 0:
                if assignment[var] == 0:  # already assigned false
                    if components[var_to_node(-var)] == c:
                        print("NO")
                        return
                elif assignment[var] == -1:  # unassigned
                    assignment[var] = 1  # assign true
            else:
                var = -var
                if assignment[var] == 1:  # already assigned true
                    if components[var_to_node(var)] == c:
                        print("NO")
                        return
                elif assignment[var] == -1:  # unassigned
                    assignment[var] = 0  # assign false
    
    # Assign remaining unassigned variables
    for i in range(1, n+1):
        if assignment[i] == -1:
            assignment[i] = 1  # default to true
    
    print("YES")
    print(' '.join(str(assignment[i]) for i in range(1, n+1)))

if __name__ == "__main__":
    main()
import sys
sys.setrecursionlimit(1 << 25)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # For each clause (a or b), we add edges (~a -> b) and (~b -> a)
    # Variables: 0 to n-1 (for valves 1 to n in state 0)
    #            n to 2n-1 (for valves 1 to n in state 1)
    # Literal x (1-based) represents variable x-1 in state 1 --> node x-1
    # Literal -x (1-based) represents variable x-1 in state 0 --> node x-1 + n
    
    adj = [[] for _ in range(2 * n)]
    rev_adj = [[] for _ in range(2 * n)]
    
    index = 2
    for _ in range(m):
        v1 = int(data[index])
        v2 = int(data[index+1])
        index += 2
        
        # Convert to 0-based variable indices and determine nodes
        # For literal v: if v > 0, node = v-1; if v < 0, node = abs(v)-1 + n
        def get_node(lit):
            if lit > 0:
                return lit - 1
            else:
                return (-lit - 1) + n
        
        node1 = get_node(v1)
        node2 = get_node(v2)
        
        # Add implications: ~node1 -> node2 and ~node2 -> node1
        # ~node1 is (node1 + n) % (2*n)
        not_node1 = (node1 + n) % (2 * n)
        not_node2 = (node2 + n) % (2 * n)
        
        adj[not_node1].append(node2)
        adj[not_node2].append(node1)
        rev_adj[node2].append(not_node1)
        rev_adj[node1].append(not_node2)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check for contradiction: variable and its negation in same SCC
    for i in range(n):
        if scc_id[i] == scc_id[i + n]:
            print("NO")
            return
    
    # Assign values based on SCC topological order
    assignment = [-1] * n
    # Create SCC graph
    scc_graph = [set() for _ in range(scc_count)]
    for u in range(2 * n):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_graph[scc_id[u]].add(scc_id[v])
    
    # Topological sort of SCCs
    scc_visited = [False] * scc_count
    scc_order = []
    
    def scc_dfs(u):
        scc_visited[u] = True
        for v in scc_graph[u]:
            if not scc_visited[v]:
                scc_dfs(v)
        scc_order.append(u)
    
    for i in range(scc_count):
        if not scc_visited[i]:
            scc_dfs(i)
    
    scc_order.reverse()
    
    # Assign truth values
    scc_value = [-1] * scc_count
    for scc in scc_order:
        if scc_value[scc] == -1:
            scc_value[scc] = 0
            # If this SCC represents some variables, their negation SCC should be 1
            # But we need to make sure we don't contradict
            # Actually, since implication graph is built correctly, if we assign 0 to SCC,
            # then all SCCs reachable from it are also 0, which is handled by toposort
            # We just need to ensure if a SCC and its complement are both unassigned,
            # we can choose a value.
            pass
    
    # Now assign to variables
    for i in range(n):
        scc_var = scc_id[i]
        scc_neg = scc_id[i + n]
        if scc_value[scc_var] == -1 and scc_value[scc_neg] == -1:
            # Can assign either, let's assign 0 to var (1 to neg)
            scc_value[scc_var] = 0
            scc_value[scc_neg] = 1
        elif scc_value[scc_var] == -1:
            scc_value[scc_var] = 1 - scc_value[scc_neg]
        elif scc_value[scc_neg] == -1:
            scc_value[scc_neg] = 1 - scc_value[scc_var]
    
    for i in range(n):
        assignment[i] = scc_value[scc_id[i]]
    
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    main()
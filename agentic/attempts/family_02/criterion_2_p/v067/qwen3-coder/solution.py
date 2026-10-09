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
        clauses.append((l1, l2))
        index += 2
    
    # Build implication graph for 2-SAT
    # Variables: 0 to n-1 represent x1 to xn (0 means False, 1 means True)
    # xi is at index i, not xi is at index i+n
    adj = [[] for _ in range(2 * n)]
    adj_rev = [[] for _ in range(2 * n)]
    
    # For each clause (l1 or l2), we add edges:
    # not l1 -> l2 and not l2 -> l1
    
    for l1, l2 in clauses:
        # Convert literals to variable indices
        # l1 = +x -> x-1 (True), l1 = -x -> x-1+n (False)
        if l1 > 0:
            var1 = l1 - 1       # x_i is True
            not_var1 = var1 + n # x_i is False
        else:
            var1 = (-l1) - 1 + n # not x_i is True (i.e., x_i is False)
            not_var1 = var1 - n  # not x_i is False (i.e., x_i is True)
            
        if l2 > 0:
            var2 = l2 - 1
            not_var2 = var2 + n
        else:
            var2 = (-l2) - 1 + n
            not_var2 = var2 - n
            
        # Add implications: not l1 -> l2 and not l2 -> l1
        adj[not_var1].append(var2)
        adj[not_var2].append(var1)
        adj_rev[var2].append(not_var1)
        adj_rev[var1].append(not_var2)
        
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
            
    # Second DFS on transpose graph
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v)
                
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
            
    # Check if any variable and its negation are in the same SCC
    for i in range(n):
        if scc_id[i] == scc_id[i + n]:
            print("NO")
            return
            
    # Assign values based on topological order of SCCs
    # Variables in later SCCs should be assigned True
    assignment = [False] * n
    scc_order = list(range(scc_count))
    # We need the reverse of the finishing order of SCCs
    # But since we used Kosaraju, SCCs are already in reverse topological order
    # So higher scc_id means earlier in topological order
    # Actually, let's recompute the topological order properly
    
    # Rebuild SCC graph
    scc_graph = [set() for _ in range(scc_count)]
    for u in range(2 * n):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_graph[scc_id[u]].add(scc_id[v])
                
    # Topological sort of SCCs
    in_degree = [0] * scc_count
    for u in range(scc_count):
        for v in scc_graph[u]:
            in_degree[v] += 1
            
    from collections import deque
    queue = deque()
    for i in range(scc_count):
        if in_degree[i] == 0:
            queue.append(i)
            
    topo_scc = []
    while queue:
        u = queue.popleft()
        topo_scc.append(u)
        for v in scc_graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    # Assign truth values: process SCCs in reverse topological order
    scc_value = [None] * scc_count
    for scc in reversed(topo_scc):
        if scc_value[scc] is None:
            scc_value[scc] = False # Can be arbitrary, but we'll derive from implications
            # Actually, better approach: assign False to sink SCCs, propagate backwards
            pass
            
    # Simpler: just assign based on which SCC comes first in topological order
    # Variables in earlier SCCs (smaller topo index) are assigned False
    # But this is complex. Let's use the fact that in Kosaraju,
    # the order in which we finish SCCs in second DFS gives reverse topological order
    # So we can assign values accordingly
    
    # Simpler yet: for each variable, if scc_id[x] > scc_id[not x], then x is True
    for i in range(n):
        if scc_id[i] > scc_id[i + n]:
            assignment[i] = True
        elif scc_id[i] < scc_id[i + n]:
            assignment[i] = False
        # else impossible due to earlier check
            
    print("YES")
    print(' '.join(str(int(b)) for b in assignment))

if __name__ == "__main__":
    main()
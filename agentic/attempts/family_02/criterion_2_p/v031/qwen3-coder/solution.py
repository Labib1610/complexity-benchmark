import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # Build implication graph
    # Each variable x_i has two nodes: 2*i (for x_i = 0) and 2*i + 1 (for x_i = 1)
    # For clause (a OR b), we add edges: NOT a -> b and NOT b -> a
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    idx = 2
    clauses = []
    for i in range(m):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        clauses.append((a, b))
        
    for a, b in clauses:
        # Convert to 0-based indexing and handle signs
        # For a literal x, if x > 0, then x corresponds to variable x-1 = True
        # If x < 0, then -x corresponds to variable x-1 = False
        # Node IDs: for variable v (0-based), 
        # node 2*v represents v=False, node 2*v+1 represents v=True
        
        # Clause (a OR b) means (NOT a -> b) AND (NOT b -> a)
        # a is literal, say +k means var k-1 is True, -k means var k-1 is False
        # So NOT(+k) is var k-1 is False, which is node 2*(k-1)
        #    NOT(-k) is var k-1 is True,  which is node 2*(k-1)+1
        
        # First, derive node numbers for literals a and b
        if a > 0:
            node_a_true = 2*(a-1) + 1
            node_a_false = 2*(a-1)
        else:
            node_a_true = 2*(-a-1) + 1
            node_a_false = 2*(-a-1)
            
        if b > 0:
            node_b_true = 2*(b-1) + 1
            node_b_false = 2*(b-1)
        else:
            node_b_true = 2*(-b-1) + 1
            node_b_false = 2*(-b-1)
            
        # Add implications: NOT a -> b and NOT b -> a
        adj[node_a_false].append(node_b_true)
        adj[node_b_false].append(node_a_true)
        rev_adj[node_b_true].append(node_a_false)
        rev_adj[node_a_true].append(node_b_false)
    
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
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check for contradictions
    for i in range(n):
        if scc_id[2*i] == scc_id[2*i + 1]:
            print("NO")
            return
    
    # Assign values based on topological order of SCCs
    # Variables in later SCCs should be assigned True if possible
    assignment = [-1] * n
    
    # Create SCC DAG
    scc_graph = defaultdict(set)
    scc_nodes = defaultdict(list)
    
    for i in range(2 * n):
        scc_nodes[scc_id[i]].append(i)
    
    for u in range(2 * n):
        for v in adj[u]:
            if scc_id[u] != scc_id[v]:
                scc_graph[scc_id[u]].add(scc_id[v])
    
    # Topological sort of SCCs
    in_degree = [0] * scc_count
    for u in scc_graph:
        for v in scc_graph[u]:
            in_degree[v] += 1
    
    queue = deque()
    for i in range(scc_count):
        if in_degree[i] == 0:
            queue.append(i)
    
    scc_order = []
    while queue:
        u = queue.popleft()
        scc_order.append(u)
        for v in scc_graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Assign truth values
    for scc in reversed(scc_order):
        for node in scc_nodes[scc]:
            var = node // 2
            val = node % 2
            if assignment[var] == -1:
                assignment[var] = val
    
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == "__main__":
    main()
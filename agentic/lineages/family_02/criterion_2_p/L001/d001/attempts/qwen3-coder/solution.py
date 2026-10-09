import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each constraint (a or b), we can rewrite it as (~a => b) and (~b => a)
    # This creates a 2-SAT problem
    # We'll use node IDs: for hub i (1-indexed), 
    # node 2*i represents hub i being ACTIVE
    # node 2*i+1 represents hub i being DORMANT
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        
        # Convert to 0-indexed hub numbers and determine if they should be ACTIVE or DORMANT
        if l1 > 0:
            hub1, state1 = l1 - 1, 0  # 0 means ACTIVE
        else:
            hub1, state1 = -l1 - 1, 1  # 1 means DORMANT
            
        if l2 > 0:
            hub2, state2 = l2 - 1, 0  # 0 means ACTIVE
        else:
            hub2, state2 = -l2 - 1, 1  # 1 means DORMANT
        
        # Node IDs: 2*i for ACTIVE, 2*i+1 for DORMANT
        node1 = 2 * hub1 + state1  # node for hub1 having state1
        node2 = 2 * hub2 + state2  # node for hub2 having state2
        
        # The constraint is (state1 of hub1 OR state2 of hub2)
        # In implication form: (~state1 of hub1 => state2 of hub2) and (~state2 of hub2 => state1 of hub1)
        
        # ~node1 => node2  which is (node1 + 1) ^ 1 => node2
        # ~node2 => node1  which is (node2 + 1) ^ 1 => node1
        
        not_node1 = node1 ^ 1
        not_node2 = node2 ^ 1
        
        adj[not_node1].append(node2)
        adj[not_node2].append(node1)
        rev_adj[node2].append(not_node1)
        rev_adj[node1].append(not_node2)
    
    # Kosaraju's algorithm for finding SCCs
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
    
    # Check if any variable and its negation are in the same SCC
    for i in range(n):
        active_node = 2 * i
        dormant_node = 2 * i + 1
        if scc_id[active_node] == scc_id[dormant_node]:
            print("NO")
            return
    
    # Assign values based on SCC topological order
    # SCCs with higher index in Kosaraju are "earlier" in topological sort
    result = [-1] * n
    
    # For each hub, decide its state based on which node (ACTIVE or DORMANT) is in a later SCC
    for i in range(n):
        active_node = 2 * i
        dormant_node = 2 * i + 1
        
        if scc_id[active_node] > scc_id[dormant_node]:
            result[i] = 0  # ACTIVE (0-indexed), but output needs to be 1 for ACTIVE
        else:
            result[i] = 1  # DORMANT (0-indexed), but output needs to be 0 for DORMANT
    
    print("YES")
    # Convert: 0 (ACTIVE) -> 1, 1 (DORMANT) -> 0
    print(" ".join(str(1 - x) for x in result))

solve()
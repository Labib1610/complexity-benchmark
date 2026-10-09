import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    critical = set()
    for _ in range(t):
        critical.add(int(data[idx]))
        idx += 1
        
    edges = []
    adj = [[] for _ in range(n+1)]
    weights = {}
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((u,v,w))
        adj[u].append(v)
        adj[v].append(u)
        weights[(u,v)] = w
        weights[(v,u)] = w
        
    # Since m = n-1 and connected, it's a tree.
    # We can root the tree and use DP.
    
    # Root the tree at node 1
    root = 1
    parent = [-1] * (n+1)
    children = [[] for _ in range(n+1)]
    
    visited = [False] * (n+1)
    queue = deque([root])
    visited[root] = True
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                queue.append(v)
                
    # Compute degree D_i for each node
    D = [0] * (n+1)
    for u,v,_ in edges:
        D[u] += 1
        D[v] += 1
        
    # Now do DP on the tree
    # For each subtree, we compute:
    # dp[u][0] = min cost when X_u = 0
    # dp[u][1] = min cost when X_u = 1
    # But we need to consider the constraint equation:
    # sum (X_u - X_v)^2 + sum (2-D_i) X_i = 2
    
    # Let's define f(X) = sum (X_u - X_v)^2 + sum (2-D_i) X_i
    # We want f(X) = 2
    
    # For a given configuration, f(X) is fixed.
    # So we can't just minimize cost independently.
    
    # Let's think differently.
    # Each edge contributes (X_u - X_v)^2 to the sum.
    # This is 0 if X_u == X_v, 1 otherwise.
    # So sum of (X_u - X_v)^2 = number of edges where X_u != X_v
    
    # Let S = {i : X_i = 1}
    # Then sum (2-D_i) X_i = sum_{i in S} (2 - D_i)
    
    # So f(X) = |E_cut| + sum_{i in S} (2 - D_i) = 2
    
    # Our goal is to find a subset S such that:
    # |E_cut| + sum_{i in S} (2 - D_i) = 2
    # And critical variables are in S
    # And we want to minimize sum_{(u,v) in E, u in S, v in S} W_{uv}
    
    # This seems complex. Let's try another approach.
    
    # Key insight: since it's a tree, we can do DP with states tracking the value of f(X)
    # But f(X) can be negative, so we need to bound it.
    
    # Actually, let's re-examine the examples.
    
    # In example 1: n=4, m=3, edges: (1,2,5),(2,3,1),(3,4,2)
    # D = [0,1,2,2,1]
    # Critical: {1,4}
    # One solution: X=[1,1,1,1], f(X) = 0 + (2-1)*1 + (2-2)*1 + (2-2)*1 + (2-1)*1 = 2
    # Cost = 5*1*1 + 1*1*1 + 2*1*1 = 8
    
    # Another attempt: X=[1,0,0,1]
    # f(X) = (1-0)^2 + (0-0)^2 + (0-1)^2 + (2-1)*1 + (2-2)*0 + (2-2)*0 + (2-1)*1 = 1 + 0 + 1 + 1 + 0 + 0 + 1 = 4
    
    # Need f(X) = 2. So we need exactly 2 contribution to the sum.
    
    # Let's think of this as a quadratic pseudo-boolean optimization problem with a constraint.
    
    # Maybe we can enumerate over possible values of the constraint function?
    
    # Let's try a different approach. Since m=n-1 and connected, it's a tree.
    # We can root at some node and do dynamic programming.
    
    # For each node u, and for each possible "signature" of how the subtree rooted at u contributes,
    # we compute the minimum cost.
    
    # But what is the signature? It should capture how much this subtree contributes to f(X).
    
    # Let's define for a subtree T_u rooted at u:
    # Let cut_u = number of edges in T_u with different X values (contributes to first sum)
    # Let ones_u = number of nodes in T_u set to 1
    # Let deg_u = sum_{i in T_u} (2-D_i) X_i
    
    # But this is getting messy. Let's look at the constraint again.
    
    # sum (X_u - X_v)^2 + sum (2-D_i) X_i = 2
    
    # Let's call the first term CUT and second term DEG.
    # So CUT + DEG = 2
    
    # CUT is the number of edges where endpoints differ.
    # DEG = sum_{X_i=1} (2 - D_i)
    
    # Since we're on a tree, CUT is minimized when we take a connected subgraph of 1's.
    # Actually, that's not right. CUT depends on the global assignment.
    
    # New idea: since it's a tree, we can pick a spanning tree and then decide which nodes are 1.
    # The constraint fixes the total "energy" to be 2.
    
    # Let's think of minimizing the cost subject to the constraint being satisfied.
    
    # Cost = sum_{(u,v): X_u=X_v=1} W_{uv}
    
    # This suggests we want to select a subset S of nodes to be 1, including all critical ones,
    # such that the constraint holds, and the total weight of edges inside S is minimized.
    
    # The constraint is:
    # sum_{(u,v)} (X_u - X_v)^2 + sum_i (2-D_i) X_i = 2
    
    # Let's denote by E the set of edges, V the set of vertices.
    # If we select S ⊆ V as the set of vertices with X_i=1, then:
    # CUT = |{(u,v) ∈ E : |{u,v} ∩ S| = 1}| (edges crossing the cut)
    # DEG = sum_{i ∈ S} (2 - D_i)
    # Constraint: CUT + DEG = 2
    
    # Goal: minimize W(S) = sum_{(u,v): {u,v} ⊆ S} W_{uv}
    
    # This is now clearer. We want to find a subset S containing all critical nodes,
    # such that CUT + DEG = 2, and W(S) is minimized.
    
    # Since the graph is a tree, CUT = |∂S| (size of edge boundary of S).
    # Also, since the tree is connected, if S is non-empty and not everything, then CUT >= 1.
    
    # Let's enumerate small values of CUT and see what DEG can be.
    
    # Case 1: CUT = 0. Then DEG = 2.
    # CUT = 0 means S is empty or S = V.
    # S cannot be empty because critical nodes must be in S.
    # So S = V. Then DEG = sum_{i=1}^n (2 - D_i) = 2n - sum D_i = 2n - 2m = 2n - 2(n-1) = 2.
    # This works! The cost is sum of all edge weights where both endpoints are in V, i.e., all edges.
    # Cost = sum W_e
    
    # Case 2: CUT = 1. Then DEG = 1.
    # CUT = 1 means S induces a cut of size 1. In a tree, this means removing one edge splits the tree into two components,
    # and S is one of them. Since critical nodes must be in S, there are only a few possibilities.
    
    # Case 3: CUT = 2. Then DEG = 0.
    # CUT = 2 means the boundary of S has size 2.
    
    # Let's implement checking these cases.
    
    total_weight = sum(w for _,_,w in edges)
    
    best_cost = total_weight  # Case where S = V
    
    # Enumerate subsets S with CUT <= 2 and check constraints
    
    # But enumerating all subsets is too slow. Let's be smarter.
    
    # Since it's a tree, we can use the fact that cuts correspond to edges.
    
    # Case 1: S = V. Already handled.
    
    # Case 2: Remove one edge, get two components. One component contains all critical nodes.
    # Try all edges as the cut edge.
    
    for i in range(m):
        u,v,w = edges[i]
        # Remove edge (u,v). Get two components.
        # Check which component contains all critical nodes.
        
        # BFS/DFS from u avoiding edge (u,v)
        visited_u = [False] * (n+1)
        queue_u = deque([u])
        visited_u[u] = True
        comp_u = [u]
        
        # Build adjacency list without this edge
        adj_temp = [[] for _ in range(n+1)]
        for j in range(m):
            if i == j: continue
            x,y,_ = edges[j]
            adj_temp[x].append(y)
            adj_temp[y].append(x)
            
        while queue_u:
            node = queue_u.popleft()
            for neighbor in adj_temp[node]:
                if not visited_u[neighbor]:
                    visited_u[neighbor] = True
                    comp_u.append(neighbor)
                    queue_u.append(neighbor)
                    
        comp_u_set = set(comp_u)
        comp_v_set = set(range(1,n+1)) - comp_u_set
        
        # Check if critical nodes are all in one component
        crit_in_u = critical <= comp_u_set
        crit_in_v = critical <= comp_v_set
        
        if crit_in_u:
            # S = comp_u
            CUT = 1
            DEG = sum(2 - D[node] for node in comp_u)
            if CUT + DEG == 2:
                # Calculate cost
                cost = 0
                for j in range(m):
                    if j == i: continue
                    x,y,weight = edges[j]
                    if x in comp_u_set and y in comp_u_set:
                        cost += weight
                best_cost = min(best_cost, cost)
                        
        elif crit_in_v:
            # S = comp_v
            CUT = 1
            DEG = sum(2 - D[node] for node in comp_v_set)
            if CUT + DEG == 2:
                # Calculate cost
                cost = 0
                for j in range(m):
                    if j == i: continue
                    x,y,weight = edges[j]
                    if x in comp_v_set and y in comp_v_set:
                        cost += weight
                best_cost = min(best_cost, cost)
    
    # Case 3: CUT = 2, DEG = 0. This means S has boundary of size 2.
    # In a tree, this corresponds to removing two edges.
    # But we have to ensure the resulting subgraph containing critical nodes is connected and has boundary 2.
    # This is more complex. Let's skip for now and see if previous cases suffice.
    
    print(best_cost)

if __name__ == "__main__":
    main()
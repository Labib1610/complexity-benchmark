import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each variable x_i, we have two nodes: 2*i (for x_i = 0) and 2*i+1 (for x_i = 1)
    # But we'll use a more standard 2-SAT approach:
    # Variables: for variable i (1-based), we use node 2*i for x_i (valve i in pos 0) 
    # and node 2*i+1 for ~x_i (valve i in pos 1)
    # Actually, let's reindex from 0: variable i (0-based) -> node 2*i (x_i=0), 2*i+1 (x_i=1)
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    # Helper function to convert literal to node id
    # l > 0 means valve l (1-based) in position 1 -> x_{l-1} = 1 -> node 2*(l-1)+1
    # l < 0 means valve |l| (1-based) in position 0 -> x_{|l|-1} = 0 -> node 2*(|l|-1)
    def lit_to_node(l):
        if l > 0:
            return 2 * (l - 1) + 1  # x_i = 1
        else:
            return 2 * (-l - 1)     # x_i = 0
    
    # For clause (a OR b), we add edges (~a -> b) and (~b -> a)
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Convert literals to nodes
        n1 = lit_to_node(l1)
        n2 = lit_to_node(l2)
        # Add clauses: (~n1 -> n2) and (~n2 -> n1)
        # ~n1 is n1^1, ~n2 is n2^1
        adj[n1 ^ 1].append(n2)
        adj[n2 ^ 1].append(n1)
        rev_adj[n2].append(n1 ^ 1)
        rev_adj[n1].append(n2 ^ 1)
    
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
    component = []
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        component.append(u)
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    order.reverse()
    for u in order:
        if not visited[u]:
            component.clear()
            dfs2(u)
            scc_count += 1
    
    # Check if satisfiable
    assignment = [-1] * n
    for i in range(n):
        node_false = 2 * i       # x_i = 0
        node_true = 2 * i + 1    # x_i = 1
        if scc_id[node_false] == scc_id[node_true]:
            print("NO")
            return
        # In the implication graph, if there's a path from ~x to x, then x must be true
        # In SCC terms, higher SCC ids in the condensation correspond to true values
        # So if scc_id[~x] > scc_id[x], then x should be true
        if scc_id[node_false] > scc_id[node_true]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    main()
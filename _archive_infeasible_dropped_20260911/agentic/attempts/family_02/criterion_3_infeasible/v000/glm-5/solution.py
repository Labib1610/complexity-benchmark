import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # Build implication graph
    # Node indices: 2*i for positive literal i, 2*i+1 for negative literal -i
    # i ranges from 1 to n
    N = 2 * (n + 1)
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        
        # Map literal to node index
        # u > 0: node 2*u, u < 0: node 2*(-u) + 1
        # Implication: not u -> v
        # not u is the opposite state of u
        nu = u ^ 1
        
        node_nu = 2 * abs(nu) + (1 if nu < 0 else 0)
        node_v = 2 * abs(v) + (1 if v < 0 else 0)
        
        adj[node_nu].append(node_v)
        radj[node_v].append(node_nu)
        
        # Also the symmetric implication: not v -> u
        nv = v ^ 1
        node_nv = 2 * abs(nv) + (1 if nv < 0 else 0)
        node_u = 2 * abs(u) + (1 if u < 0 else 0)
        
        adj[node_nv].append(node_u)
        radj[node_u].append(node_nv)

    # Kosaraju's algorithm to find SCCs
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [u]
        while stack:
            curr = stack.pop()
            if visited[curr]:
                continue
            visited[curr] = True
            # Push children then self for post-order processing
            # To simulate recursion order properly for simple stack DFS:
            # We can push (node, iterator_state) or just push children and rely on visited check
            # But for correct finishing order, we need to process children before node is "finished"
            # A common iterative approach:
            stack.append(curr) # Push again to add to order later
            for v in adj[curr]:
                if not visited[v]:
                    stack.append(v)
        # This simple stack DFS visits children, but the order list addition needs to happen after children are done.
        # Let's use a standard iterative DFS with explicit "processing" state or just recursion if safe.
        # Recursion limit is increased. Let's use recursion for simplicity and correctness of order.
    
    # Re-implementing DFS with recursion
    sys.setrecursionlimit(max(1000000, N + m + 10))
    
    visited = [False] * N
    
    def dfs1_rec(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1_rec(v)
        order.append(u)

    for i in range(2, N): # Nodes 2 to 2n+1
        if not visited[i]:
            dfs1_rec(i)

    comp_id = [-1] * N
    current_id = 0
    
    def dfs2(u, cid):
        stack = [u]
        while stack:
            curr = stack.pop()
            if comp_id[curr] != -1:
                continue
            comp_id[curr] = cid
            for v in radj[curr]:
                if comp_id[v] == -1:
                    stack.append(v)

    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, current_id)
            current_id += 1

    # Find the smallest trapped task
    # A task j is trapped if j and -j are in the same SCC
    # We want the smallest j
    for j in range(1, n + 1):
        pos_node = 2 * j
        neg_node = 2 * j + 1
        if comp_id[pos_node] == comp_id[neg_node]:
            print(j)
            return

if __name__ == '__main__':
    solve()
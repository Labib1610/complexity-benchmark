import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # We have 2n nodes: node 2*i is "i is 0", node 2*i+1 is "i is 1"
    # Implication graph: (u or v) is equivalent to (~u -> v) and (~v -> u)
    # Condition format: x > 0 means "x is 1", x < 0 means "|x| is 0"
    # Map variable x to node index:
    # value 1 -> node 2*x + 1
    # value 0 -> node 2*x
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        u = next(iterator)
        v = next(iterator)
        u = int(u)
        v = int(v)
        
        # Determine literals
        # u: integer representing (+x) for 1 or (-x) for 0
        # Node index for literal val:
        # var = abs(val), state = 1 if val > 0 else 0
        # node = 2*var + state
        
        # We store implications for the clause (nu OR nv)
        # which means NOT nu -> nv and NOT nv -> nu
        
        def get_node(literal):
            var = abs(literal) - 1 # 0-indexed variable
            state = 1 if literal > 0 else 0
            return 2 * var + state
        
        nu = u
        nv = v
        
        # ~nu -> nv
        # negation of 'nu' node
        # if nu means 'var is state', ~nu means 'var is 1-state'
        # node(nu) = val_node
        node_u = get_node(nu)
        node_v = get_node(nv)
        
        # index of ~nu is node_u ^ 1 (since 2*i and 2*i+1 are paired)
        adj[node_u ^ 1].append(node_v)
        adj[node_v ^ 1].append(node_u)

    # Kosaraju's algorithm for SCC
    sys.setrecursionlimit(2 * 10**5 + 10)
    
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
            
    reverse_adj = [[] for _ in range(2 * n)]
    for u in range(2 * n):
        for v in adj[u]:
            reverse_adj[v].append(u)
            
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
    current_scc = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = current_scc
        for v in reverse_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    for u in reversed(order):
        if not visited[u]:
            dfs2(u)
            current_scc += 1
            
    # Check satisfiability
    result = [0] * n
    for i in range(n):
        if scc_id[2 * i] == scc_id[2 * i + 1]:
            print("NO")
            return
        # If scc_id of '1' is greater than '0', assign 1
        # Standard topological order relation: later in order = higher scc id = True
        if scc_id[2 * i + 1] > scc_id[2 * i]:
            result[i] = 1
        else:
            result[i] = 0
            
    print("YES")
    print(*(result))

if __name__ == "__main__":
    solve()
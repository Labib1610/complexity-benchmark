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
    # Node indices: 0 to 2n-1
    # For hub k (1-indexed): (k-1)*2 is False (DORMANT), (k-1)*2+1 is True (ACTIVE)
    # Negation: x ^ 1
    N = 2 * n
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        # Map literal to node index
        # l > 0: ACTIVE (True) -> node 2*(l-1) + 1
        # l < 0: DORMANT (False) -> node 2*(|l|-1)
        def get_node(lit):
            k = abs(lit) - 1
            is_true = lit > 0
            return 2 * k + (1 if is_true else 0)

        u = get_node(l1)
        v = get_node(l2)
        
        # Clause (l1 OR l2) is equivalent to (NOT l1 -> l2) AND (NOT l2 -> l1)
        adj[u ^ 1].append(v)
        adj[v ^ 1].append(u)
        
        radj[v].append(u ^ 1)
        radj[u].append(v ^ 1)

    # Kosaraju's algorithm to find SCCs
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                neighbor = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[neighbor]:
                    stack.append((neighbor, 0))
            else:
                stack.pop()
                order.append(node)

    for i in range(N):
        if not visited[i]:
            dfs1(i)

    comp_id = [-1] * N
    current_id = 0
    
    for u in reversed(order):
        if comp_id[u] == -1:
            # DFS on reversed graph
            stack = [u]
            comp_id[u] = current_id
            while stack:
                node = stack.pop()
                for v in radj[node]:
                    if comp_id[v] == -1:
                        comp_id[v] = current_id
                        stack.append(v)
            current_id += 1

    # Check for contradictions
    for i in range(0, N, 2):
        if comp_id[i] == comp_id[i ^ 1]:
            print("NO")
            return

    # Construct assignment
    # If comp_id[True] > comp_id[False], then we must set True (to satisfy the implication)
    # Note: In Kosaraju's, later finishing times (processed later in reversed order) 
    # belong to components with higher topological order (closer to source in condensation graph).
    # We process in reverse finishing order, so the first component found (id 0) is a sink.
    # A sink component must be true. So if comp_id[True] < comp_id[False], True is in a sink.
    # Actually, standard logic: if comp_id[True] > comp_id[False], then there is a path 
    # from False to True, meaning False implies True, so we must pick True.
    # Wait, the standard Kosaraju assigns IDs in topological order (0 is sink).
    # If comp_id[True] < comp_id[False], True is in a component closer to sink.
    # Let's stick to: if comp_id[True] > comp_id[False], pick True.
    # This is equivalent to: if comp_id[True] < comp_id[False], pick False.
    
    assignment = [0] * n
    for i in range(n):
        node_true = 2 * i + 1
        node_false = 2 * i
        if comp_id[node_true] > comp_id[node_false]:
            assignment[i] = 1
        else:
            assignment[i] = 0

    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == '__main__':
    solve()
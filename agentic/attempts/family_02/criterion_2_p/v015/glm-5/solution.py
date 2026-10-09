import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT setup
    # Variables: 1 to n
    # For each variable x, we have two nodes: 2*x (True) and 2*x+1 (False)
    # Node indices: 2 to 2*n+1
    N = 2 * n + 2
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    def get_nodes(val):
        # val > 0: gate val is OPEN (True)
        # val < 0: gate -val is CLOSED (False)
        gate = abs(val)
        if val > 0:
            return 2 * gate, 2 * gate + 1  # True node, False node
        else:
            return 2 * gate + 1, 2 * gate  # False node, True node
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        u, not_u = get_nodes(l1)
        v, not_v = get_nodes(l2)
        # Mandate: (l1) OR (l2)
        # Implications: (not l1 -> l2) and (not l2 -> l1)
        adj[not_u].append(v)
        adj[not_v].append(u)
        radj[v].append(not_u)
        radj[u].append(not_v)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * N
    order = []
    
    def dfs(u):
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
    
    for i in range(2, N):
        if not visited[i]:
            dfs(i)
    
    comp = [-1] * N
    comp_id = 0
    
    for u in reversed(order):
        if comp[u] != -1:
            continue
        stack = [u]
        comp[u] = comp_id
        while stack:
            node = stack.pop()
            for neighbor in radj[node]:
                if comp[neighbor] == -1:
                    comp[neighbor] = comp_id
                    stack.append(neighbor)
        comp_id += 1
    
    # Check for contradiction and assign values
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        true_node = 2 * i
        false_node = 2 * i + 1
        if comp[true_node] == comp[false_node]:
            print("NO")
            return
        # If true_node comes later in reverse topological order (higher comp_id),
        # it means it should be assigned True
        if comp[true_node] > comp[false_node]:
            result[i] = 1
        else:
            result[i] = 0
    
    print("YES")
    print(' '.join(map(str, result[1:])))

solve()
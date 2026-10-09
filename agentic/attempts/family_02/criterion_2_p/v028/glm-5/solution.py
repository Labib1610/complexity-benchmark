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
    # Each species i has two nodes: 2*i (False/Arid) and 2*i+1 (True/Humid)
    # For variable x: if x > 0, means species x is Humid (node 2*x+1)
    #                if x < 0, means species |x| is Arid (node 2*|x|)
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        # Clause: (l1 OR l2)
        # Add edges: NOT l1 -> l2 and NOT l2 -> l1
        
        # Convert l1, l2 to node indices
        # For value v: if v > 0, node = 2*v+1; if v < 0, node = 2*|v|
        # NOT of node: flip last bit
        
        def to_node(v):
            if v > 0:
                return 2 * v + 1
            else:
                return 2 * (-v)
        
        def neg_node(node):
            return node ^ 1
        
        n1 = to_node(l1)
        n2 = to_node(l2)
        
        adj[neg_node(n1)].append(n2)
        adj[neg_node(n2)].append(n1)
    
    # Kosaraju's algorithm for SCC
    N = 2 * n
    visited = [False] * N
    order = []
    
    for i in range(N):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, idx = stack[-1]
                if not visited[node]:
                    visited[node] = True
                while idx < len(adj[node]) and visited[adj[node][idx]]:
                    idx += 1
                if idx < len(adj[node]):
                    stack[-1] = (node, idx + 1)
                    stack.append((adj[node][idx], 0))
                else:
                    stack.pop()
                    order.append(node)
    
    # Reverse graph
    radj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            radj[v].append(u)
    
    visited = [False] * N
    comp = [-1] * N
    comp_id = 0
    
    for u in reversed(order):
        if not visited[u]:
            stack = [u]
            visited[u] = True
            while stack:
                node = stack.pop()
                comp[node] = comp_id
                for v in radj[node]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            comp_id += 1
    
    # Check if any variable has both True and False in same SCC
    for i in range(n):
        if comp[2 * i] == comp[2 * i + 1]:
            print("NO")
            return
    
    # Assign values: if comp[True] > comp[False], set to True
    # Since we process in reverse topological order, higher comp_id means earlier in order
    result = [0] * n
    for i in range(n):
        if comp[2 * i + 1] > comp[2 * i]:
            result[i] = 1
        else:
            result[i] = 0
    
    print("YES")
    print(' '.join(map(str, result)))

solve()
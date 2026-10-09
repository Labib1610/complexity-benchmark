import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        # A rule triggers fault if both targets are contradicted.
        # To avoid fault, we must satisfy at least one.
        # So we add implication: if we contradict l1, we must satisfy l2.
        # Contradicting l1 means setting switch to opposite of l1's target.
        # Satisfying l2 means setting switch to l2's target.
        
        # Node indices: 2*i for OFF (0), 2*i+1 for ON (1)
        # l > 0 means target ON, l < 0 means target OFF
        
        # If we contradict l1:
        # l1 > 0 (target ON) -> contradict means set OFF -> node 2*(l1-1)
        # l1 < 0 (target OFF) -> contradict means set ON -> node 2*(-l1-1)+1
        u = 2 * (abs(l1) - 1) + (1 if l1 > 0 else 0)
        
        # If we satisfy l2:
        # l2 > 0 (target ON) -> satisfy means set ON -> node 2*(l2-1)+1
        # l2 < 0 (target OFF) -> satisfy means set OFF -> node 2*(-l2-1)
        v = 2 * (abs(l2) - 1) + (1 if l2 > 0 else 0)
        
        adj[u].append(v)
        
        # Similarly: if we contradict l2, we must satisfy l1
        u2 = 2 * (abs(l2) - 1) + (1 if l2 > 0 else 0)
        v2 = 2 * (abs(l1) - 1) + (1 if l1 > 0 else 0)
        adj[u2].append(v2)
    
    # Kosaraju's algorithm for SCC
    N = 2 * n
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
    
    # Reverse graph
    radj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            radj[v].append(u)
    
    comp_id = [-1] * N
    cid = 0
    
    def dfs2(u, cid):
        stack = [u]
        while stack:
            node = stack.pop()
            if comp_id[node] != -1:
                continue
            comp_id[node] = cid
            for neighbor in radj[node]:
                if comp_id[neighbor] == -1:
                    stack.append(neighbor)
    
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, cid)
            cid += 1
    
    # Check 2-SAT satisfiability
    for i in range(n):
        if comp_id[2*i] == comp_id[2*i+1]:
            print("NO")
            return
    
    # Build assignment
    assignment = [0] * n
    for i in range(n):
        # If OFF (2*i) has higher comp_id than ON (2*i+1), set to ON
        if comp_id[2*i] > comp_id[2*i+1]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

solve()
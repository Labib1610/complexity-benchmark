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
        
        # Clause: NOT(l1 AND l2) = (NOT l1) OR (NOT l2)
        # Implications: l1 -> NOT l2, l2 -> NOT l1
        # Variable x: node 2*x for False (x=0), 2*x+1 for True (x=1)
        # Condition k (mode 0): node 2*(k-1)
        # Condition -k (mode 1): node 2*(k-1)+1
        
        def get_node(val):
            k = abs(val) - 1
            if val > 0: # condition mode 0
                return 2 * k
            else: # condition mode 1
                return 2 * k + 1
        
        u = get_node(l1)
        v = get_node(l2)
        
        # u -> NOT v
        adj[u].append(v ^ 1)
        # v -> NOT u
        adj[v].append(u ^ 1)
    
    # Kosaraju's algorithm for SCC
    N = 2 * n
    visited = [False] * N
    order = []
    
    for i in range(N):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, idx = stack.pop()
                if idx == 0:
                    if visited[node]:
                        continue
                    visited[node] = True
                    stack.append((node, 1))
                    for nei in adj[node]:
                        if not visited[nei]:
                            stack.append((nei, 0))
                else:
                    order.append(node)
    
    comp_id = [-1] * N
    current_comp = 0
    
    # Build reverse graph
    radj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            radj[v].append(u)
            
    for u in reversed(order):
        if comp_id[u] == -1:
            stack = [u]
            comp_id[u] = current_comp
            while stack:
                node = stack.pop()
                for nei in radj[node]:
                    if comp_id[nei] == -1:
                        comp_id[nei] = current_comp
                        stack.append(nei)
            current_comp += 1
    
    # Check satisfiability
    assignment = [0] * n
    for i in range(n):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp_id[2 * i] > comp_id[2 * i + 1] else 0
    
    print("YES")
    print(" ".join(map(str, assignment)))

solve()
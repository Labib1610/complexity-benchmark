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
        
        u = abs(l1) - 1
        v = abs(l2) - 1
        
        # Determine implication: if first condition fails, second must hold
        if l1 > 0:
            u_from = 2 * u + 1  # u is 0
        else:
            u_from = 2 * u      # u is 1
            
        if l2 > 0:
            v_to = 2 * v        # v is 1
        else:
            v_to = 2 * v + 1    # v is 0
            
        adj[u_from].append(v_to)
        
        # Reverse implication
        if l2 > 0:
            v_from = 2 * v + 1  # v is 0
        else:
            v_from = 2 * v      # v is 1
            
        if l1 > 0:
            u_to = 2 * u        # u is 1
        else:
            u_to = 2 * u + 1    # u is 0
            
        adj[v_from].append(u_to)

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
    
    # Transpose graph
    radj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            radj[v].append(u)
            
    comp_id = [-1] * N
    cid = 0
    for u in reversed(order):
        if comp_id[u] == -1:
            stack = [u]
            comp_id[u] = cid
            while stack:
                node = stack.pop()
                for v in radj[node]:
                    if comp_id[v] == -1:
                        comp_id[v] = cid
                        stack.append(v)
            cid += 1
            
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
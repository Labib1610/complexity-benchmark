import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 2-SAT variables: 2*i for STANDBY (0), 2*i+1 for ACTIVE (1)
    # 0-indexed subsystems: i from 0 to n-1
    N = 2 * n
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    def add_imp(u, v):
        adj[u].append(v)
        radj[v].append(u)
        
    for k in range(m):
        c1 = int(input_data[2 + 3*k])
        c2 = int(input_data[3 + 3*k])
        c3 = int(input_data[4 + 3*k])
        
        # Map condition to variable index
        def get_var(c):
            i = abs(c) - 1
            if c > 0:
                return 2*i + 1  # ACTIVE
            else:
                return 2*i      # STANDBY
                
        v1 = get_var(c1)
        v2 = get_var(c2)
        v3 = get_var(c3)
        
        # Protocol is a clause (v1 OR v2 OR v3)
        # Add implications for 3-SAT to 2-SAT reduction
        add_imp(v1 ^ 1, v2)
        add_imp(v1 ^ 1, v3)
        add_imp(v2 ^ 1, v1)
        add_imp(v2 ^ 1, v3)
        add_imp(v3 ^ 1, v1)
        add_imp(v3 ^ 1, v2)
        
    # Kosaraju's algorithm to find SCCs
    visited = [False] * N
    order = []
    for i in range(N):
        if not visited[i]:
            stack = [(i, 0)]
            while stack:
                node, idx = stack[-1]
                if idx < len(adj[node]):
                    stack[-1] = (node, idx + 1)
                    nei = adj[node][idx]
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append((nei, 0))
                else:
                    stack.pop()
                    order.append(node)
                    
    comp_id = [-1] * N
    cid = 0
    for i in reversed(order):
        if comp_id[i] == -1:
            stack = [i]
            comp_id[i] = cid
            while stack:
                node = stack.pop()
                for nei in radj[node]:
                    if comp_id[nei] == -1:
                        comp_id[nei] = cid
                        stack.append(nei)
            cid += 1
            
    # Check for unsatisfiability
    for i in range(n):
        if comp_id[2*i] == comp_id[2*i + 1]:
            print("NO")
            return
            
    # Topological sort of SCCs is implicitly given by cid (decreasing order)
    assignment = [-1] * n
    for i in range(n):
        # If STANDBY (2*i) has a smaller comp_id, it appears later in topological order
        # so we should set it to True (which means STANDBY is chosen).
        # This matches the standard 2-SAT assignment rule.
        assignment[i] = 1 if comp_id[2*i] < comp_id[2*i + 1] else 0
        
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == '__main__':
    solve()
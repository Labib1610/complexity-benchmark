import sys
sys.setrecursionlimit(300000)

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
        
        # Determine the state indices
        # If l > 0, reference is mode 1. 
        # "Fails to match" means mode 0.
        # If l < 0, reference is mode 0.
        # "Fails to match" means mode 1.
        
        if l1 > 0:
            u_fail = 2 * u      # u in mode 0
            u_match = 2 * u + 1 # u in mode 1
        else:
            u_fail = 2 * u + 1  # u in mode 1
            u_match = 2 * u     # u in mode 0
            
        if l2 > 0:
            v_fail = 2 * v
            v_match = 2 * v + 1
        else:
            v_fail = 2 * v + 1
            v_match = 2 * v
            
        # Implication: u fails -> v must match
        adj[u_fail].append(v_match)
        # Implication: v fails -> u must match
        adj[v_fail].append(u_match)
        
        # Add contrapositives for 2-SAT completeness
        adj[v_match ^ 1].append(u_fail ^ 1)
        adj[u_match ^ 1].append(v_fail ^ 1)

    # Kosaraju's algorithm to find SCCs
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
                
                if idx < len(adj[node]):
                    neighbor = adj[node][idx]
                    stack[-1] = (node, idx + 1)
                    if not visited[neighbor]:
                        stack.append((neighbor, 0))
                else:
                    stack.pop()
                    order.append(node)
    
    visited = [False] * N
    comp_id = [-1] * N
    current_comp_id = 0
    
    # Build reverse graph
    rev_adj = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            rev_adj[v].append(u)
            
    for u in reversed(order):
        if not visited[u]:
            stack = [u]
            visited[u] = True
            component_nodes = []
            while stack:
                node = stack.pop()
                component_nodes.append(node)
                for v in rev_adj[node]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            
            for node in component_nodes:
                comp_id[node] = current_comp_id
            current_comp_id += 1
            
    # Check validity and assign values
    assignment = [0] * n
    for i in range(n):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            print("NO")
            return
        assignment[i] = 1 if comp_id[2 * i] > comp_id[2 * i + 1] else 0
        
    print("YES")
    print(" ".join(map(str, assignment)))

if __name__ == '__main__':
    solve()
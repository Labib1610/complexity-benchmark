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
        
        # Clause: (l1 is satisfied) OR (l2 is satisfied)
        # Implications:
        # If l1 is NOT satisfied, then l2 MUST be satisfied.
        # If l2 is NOT satisfied, then l1 MUST be satisfied.
        
        # Map flag i to indices:
        # i ON  -> 2*i
        # i OFF -> 2*i + 1
        
        # NOT satisfied for l1:
        if l1 > 0: # l1 requires ON. Not satisfied means OFF.
            u = 2 * l1 + 1
        else:      # l1 requires OFF. Not satisfied means ON.
            u = 2 * (-l1)
            
        # Must satisfy l2:
        if l2 > 0: # l2 requires ON.
            v = 2 * l2
        else:      # l2 requires OFF.
            v = 2 * (-l2) + 1
        
        adj[u].append(v)
        
        # NOT satisfied for l2:
        if l2 > 0:
            u2 = 2 * l2 + 1
        else:
            u2 = 2 * (-l2)
            
        # Must satisfy l1:
        if l1 > 0:
            v2 = 2 * l1
        else:
            v2 = 2 * (-l1) + 1
            
        adj[u2].append(v2)

    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        stack.append((neighbor, 0))
            else:
                order.append(node)

    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
            
    adj_rev = [[] for _ in range(2 * n)]
    for u in range(2 * n):
        for v in adj[u]:
            adj_rev[v].append(u)
            
    visited = [False] * (2 * n)
    comp_id = [-1] * (2 * n)
    cid = 0
    
    for u in reversed(order):
        if not visited[u]:
            stack = [u]
            visited[u] = True
            component_nodes = []
            while stack:
                node = stack.pop()
                component_nodes.append(node)
                for neighbor in adj_rev[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            for node in component_nodes:
                comp_id[node] = cid
            cid += 1
            
    # Check satisfiability
    for i in range(1, n + 1):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            print("NO")
            return
            
    # Construct assignment
    # If comp_id[ON] > comp_id[OFF], set ON (1)
    # else set OFF (0)
    # Since we process in reverse topological order, higher comp_id means earlier in topological sort
    # which means it can imply the other but not vice versa.
    # We want the one that appears earlier in topological order (higher comp_id in Kosaraju).
    
    res = []
    for i in range(1, n + 1):
        if comp_id[2 * i] > comp_id[2 * i + 1]:
            res.append('1')
        else:
            res.append('0')
            
    print("YES")
    print(' '.join(res))

if __name__ == '__main__':
    solve()
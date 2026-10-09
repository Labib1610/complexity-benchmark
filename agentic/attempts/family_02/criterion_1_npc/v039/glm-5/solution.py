import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    # 2-SAT setup
    # Variables: 2n total. For flag i (1-based), index 2*(i-1) is DISABLED (0), 2*(i-1)+1 is ENABLED (1).
    # Clause: (a or b or c) -> ((a or b) or c) -> (not a -> b) and (not b -> a) and (not (a or b) -> c)
    # Simplified: (not a -> c) and (not b -> c) and (not c -> (a or b))
    # The last part expands to: (not c -> a) and (not c -> b)
    # Total 4 implications per clause.
    
    N = 2 * n
    adj = [[] for _ in range(N)]
    
    def get_node(flag_val):
        # flag_val: positive for ENABLED, negative for DISABLED
        # Returns node index in implication graph
        idx = abs(flag_val) - 1
        if flag_val > 0:
            return 2 * idx + 1  # ENABLED
        else:
            return 2 * idx      # DISABLED
            
    for _ in range(m):
        v1 = int(next(it))
        v2 = int(next(it))
        v3 = int(next(it))
        
        a = get_node(v1)
        b = get_node(v2)
        c = get_node(v3)
        
        na = a ^ 1
        nb = b ^ 1
        nc = c ^ 1
        
        # Implications
        adj[na].append(c)
        adj[nb].append(c)
        adj[nc].append(a)
        adj[nc].append(b)
    
    # Kosaraju's algorithm for SCCs
    visited = [False] * N
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp_id = [-1] * N
    adj_rev = [[] for _ in range(N)]
    for u in range(N):
        for v in adj[u]:
            adj_rev[v].append(u)
    
    current_comp = 0
    for u in reversed(order):
        if comp_id[u] == -1:
            stack = [u]
            comp_id[u] = current_comp
            while stack:
                curr = stack.pop()
                for prev in adj_rev[curr]:
                    if comp_id[prev] == -1:
                        comp_id[prev] = current_comp
                        stack.append(prev)
            current_comp += 1
    
    # Check validity and assign values
    assignment = [0] * n
    possible = True
    
    for i in range(n):
        disabled_node = 2 * i
        enabled_node = 2 * i + 1
        
        if comp_id[disabled_node] == comp_id[enabled_node]:
            possible = False
            break
        
        # If enabled_node is in a later (topologically larger) component, it must be False.
        # So we pick the one with smaller component ID.
        if comp_id[enabled_node] > comp_id[disabled_node]:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    if not possible:
        print("NO")
    else:
        print("YES")
        print(*(assignment))

if __name__ == '__main__':
    solve()
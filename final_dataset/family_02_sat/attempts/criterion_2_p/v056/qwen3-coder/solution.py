import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each directive (a OR b), we create implications:
    # NOT a -> b and NOT b -> a
    # Variables: 1..n represent drones with Heavy-Lift (1)
    #           -1..-n represent drones with Long-Range (0)
    # But for 2-SAT, we use variables 0..2n-1 where:
    # var i (0-based) represents drone i+1 with Heavy-Lift if var < n
    # var i (0-based) represents drone i+1-n with Long-Range if var >= n
    
    def var(drone, value):
        # drone is 1-based index
        # value: 1 for Heavy-Lift, 0 for Long-Range
        drone -= 1  # convert to 0-based
        if value == 1:
            return drone
        else:
            return drone + n
    
    def inv_var(v):
        # Given variable index, return (drone_1based, value)
        if v < n:
            return (v + 1, 1)
        else:
            return (v - n + 1, 0)
    
    adj = [[] for _ in range(2 * n)]
    adj_rev = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # l1 OR l2
        # NOT l1 -> l2
        # NOT l2 -> l1
        
        # Convert literals to our variable indices
        # literal l1: if l1 > 0, it's drone l1=Heavy-Lift
        #             if l1 < 0, it's drone -l1=Long-Range
        if l1 > 0:
            v1 = var(l1, 1)  # l1 is Heavy-Lift
            not_v1 = var(l1, 0)  # NOT l1 is Long-Range
        else:
            v1 = var(-l1, 0)  # l1 is Long-Range
            not_v1 = var(-l1, 1)  # NOT l1 is Heavy-Lift
            
        if l2 > 0:
            v2 = var(l2, 1)  # l2 is Heavy-Lift
            not_v2 = var(l2, 0)  # NOT l2 is Long-Range
        else:
            v2 = var(-l2, 0)  # l2 is Long-Range
            not_v2 = var(-l2, 1)  # NOT l2 is Heavy-Lift
            
        # Add implications
        adj[not_v1].append(v2)
        adj[not_v2].append(v1)
        adj_rev[v2].append(not_v1)
        adj_rev[v1].append(not_v2)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Second DFS on transpose graph
    visited = [False] * (2 * n)
    components = [-1] * (2 * n)
    comp_num = 0
    
    def dfs2(u):
        visited[u] = True
        components[u] = comp_num
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            comp_num += 1
    
    # Check for contradiction
    for i in range(n):
        heavy = var(i + 1, 1)
        long_range = var(i + 1, 0)
        if components[heavy] == components[long_range]:
            print("NO")
            return
    
    # Assign values based on component numbers
    assignment = [-1] * n
    # In Kosaraju, later finishing times in first DFS correspond to source components
    # So components with higher number are "later"
    # If NOT x is in a later component than x, then x should be FALSE
    for i in range(n):
        heavy = var(i + 1, 1)
        long_range = var(i + 1, 0)
        if components[heavy] > components[long_range]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

threading.Thread(target=main).start()
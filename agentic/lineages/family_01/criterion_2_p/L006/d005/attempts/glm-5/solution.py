import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    d = [0] * n
    
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        d[u] += 1
        d[v] += 1
    
    color = [0] * n
    is_possible = True
    
    for i in range(n):
        if color[i] == 0:
            stack = [i]
            color[i] = 1
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_possible = False
                        break
                if not is_possible:
                    break
        if not is_possible:
            break
    
    if not is_possible:
        sys.stdout.write("NO\n")
        return
    
    # Lexicographically smallest: greedily assign 1 if possible, else 2
    # Using DSU with parity to check if assignment is consistent
    parent = list(range(n))
    parity = [0] * n
    
    def find(x):
        root = x
        p = 0
        while parent[root] != root:
            p ^= parity[root]
            root = parent[root]
        # Path compression
        curr = x
        curr_p = 0
        while parent[curr] != root:
            next_node = parent[curr]
            next_p = curr_p ^ parity[curr]
            parity[curr] = curr_p ^ p
            parent[curr] = root
            curr = next_node
            curr_p = next_p
        return root, p
    
    def union(x, y, w):
        rx, px = find(x)
        ry, py = find(y)
        if rx == ry:
            return (px ^ py) == w
        # Attach ry to rx
        parent[ry] = rx
        parity[ry] = px ^ py ^ w
        return True
    
    ans = [0] * n
    possible = True
    for i in range(n):
        # Try to assign ans[i] = 1
        # Constraint: ans[i] + ans[j] = 3 for all neighbors j
        # If ans[i] = 1, then ans[j] = 2 for all neighbors j
        # Check consistency: for each neighbor j already assigned, ans[j] must be 2
        # Using DSU: ans[i] = 1 means we set a constraint ans[i] = 1
        # We can model: ans[x] = c means constraint between x and a virtual node? 
        # Actually, let's just use the DSU to track relationships.
        # We have constraints: ans[u] + ans[v] = 3 for each edge (u,v)
        # This means ans[u] - ans[v] = 0 (if we think of it as ans[u] = 3 - ans[v])
        # Wait, let's think: if we define b[x] = ans[x] - 1 (so b[x] in {0, 1})
        # Then ans[u] + ans[v] = 3 becomes b[u] + b[v] = 1, i.e., b[u] != b[v]
        # So b[u] XOR b[v] = 1 for each edge.
        # We want lexicographically smallest ans, which means smallest b (since ans = b + 1).
        # So we greedily try b[i] = 0, else b[i] = 1.
        # Using DSU with parity to check if b[i] = 0 is consistent.
        # Let's reset and use this formulation.
        pass
    
    # Let's redo with the b[x] = ans[x] - 1 formulation
    parent = list(range(n))
    parity = [0] * n
    
    def find2(x):
        root = x
        p = 0
        while parent[root] != root:
            p ^= parity[root]
            root = parent[root]
        curr = x
        curr_p = 0
        while parent[curr] != root:
            next_node = parent[curr]
            next_p = curr_p ^ parity[curr]
            parity[curr] = curr_p ^ p
            parent[curr] = root
            curr = next_node
            curr_p = next_p
        return root, p
    
    def union2(x, y, w):
        rx, px = find2(x)
        ry, py = find2(y)
        if rx == ry:
            return (px ^ py) == w
        parent[ry] = rx
        parity[ry] = px ^ py ^ w
        return True
    
    # First, add all edges to DSU
    for u in range(n):
        for v in adj[u]:
            if u < v:
                if not union2(u, v, 1):
                    sys.stdout.write("NO\n")
                    return
    
    # Now greedily assign
    b = [0] * n
    assigned = [False] * n
    
    for i in range(n):
        if not assigned[i]:
            # Try b[i] = 0
            # Check if this is consistent with already assigned nodes in the same component
            # We need to find the root and see if there's a forced value
            # Actually, since we haven't assigned anything in this component yet, we can choose.
            # But wait, some nodes in the component might already be assigned.
            # Let's check: for the component containing i, if any node is assigned, 
            # then b[i] is determined.
            # We can find the root, then check all assigned nodes in the component.
            # But that's slow. Instead, let's just try b[i] = 0 and see if it conflicts.
            # Actually, since we process in order, when we reach i, 
            # if i's component has no assigned node, we set b[i] = 0.
            # If it has assigned nodes, b[i] is already determined.
            
            # Let's find the root and the parity
            root_i, parity_i = find2(i)
            # Check if any node in the component is assigned
            # We can track this by checking if the root has an assigned value
            # But we don't store that. Let's just iterate? No, too slow.
            # Alternative: we can store for each root whether it's assigned and what value.
            # But let's think differently.
            # Since we process nodes in order, when we assign b[i], 
            # we can propagate to the entire component.
            # But we need to check consistency first.
            # Actually, the DSU already ensures consistency of the constraints.
            # So if we set b[i] = 0, then for any node j in the same component, 
            # b[j] = parity(i, j) XOR b[i] = parity(i, j).
            # If some node j is already assigned, we need b[j] == parity(i, j).
            # So we need to check all assigned nodes in the component.
            # To do this efficiently, we can maintain for each root a list of assigned nodes? 
            # Or we can just check when we encounter them.
            # Actually, since we process in order, when we reach i, 
            # if i is not assigned, it means no node before i in the component is assigned.
            # Wait, no. The component could have nodes both before and after i.
            # But if a node j < i in the component is assigned, then i would have been assigned during propagation.
            # So if i is not assigned, it means no node j < i in the component is assigned.
            # Therefore, we can safely set b[i] = 0 and propagate.
            # But wait, what if a node j > i in the component is assigned? 
            # That can't happen because we process in order.
            # So if i is not assigned, we set b[i] = 0 and propagate to the entire component.
            
            # Propagate b[i] = 0 to the component
            # We can do a BFS/DFS
            stack = [i]
            assigned[i] = True
            b[i] = 0
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not assigned[v]:
                        assigned[v] = True
                        b[v] = 1 - b[u]
                        stack.append(v)
    
    ans = [bi + 1 for bi in b]
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, ans)) + "\n")

solve()
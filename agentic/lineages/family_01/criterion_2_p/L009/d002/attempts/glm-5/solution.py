import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # We need to assign values 1 or 2 such that for every edge (u, v),
    # 3*x_u*x_v = 2*(x_u + x_v).
    # Valid pairs are (1, 2) and (2, 1). Invalid pairs are (1, 1) and (2, 2).
    # This means the graph must be bipartite.
    # We use BFS to check bipartiteness and assign colors.
    
    color = [-1] * n
    possible = True
    
    for i in range(n):
        if color[i] == -1:
            # Start BFS from node i
            queue = deque([i])
            color[i] = 0
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
            
    if not possible:
        print("NO")
    else:
        # The problem asks for the lexicographically smallest assignment.
        # Since 1 < 2, we want to maximize the number of 1s.
        # In each connected component, we can either map color 0 -> 1 and color 1 -> 2,
        # or color 0 -> 2 and color 1 -> 1.
        # The first option yields count(1) = size(color 0).
        # The second option yields count(1) = size(color 1).
        # We choose the option that gives more 1s.
        
        # To handle components, we can iterate through nodes.
        # Since we want to assign values greedily to get lex smallest,
        # and the choice for one component is independent of others,
        # we can process nodes in order.
        # However, the choice for a component is fixed (whichever gives more 1s).
        # If counts are equal, either works, and lex order doesn't distinguish
        # between the two resulting strings (one is bitwise inverse of the other).
        
        # Let's determine the assignment for each component.
        # We can iterate through nodes, and if a node is the "root" of its component
        # (first time we see it in a sequential scan), we decide the mapping.
        
        visited_comp = [False] * n
        res = [0] * n
        
        for i in range(n):
            if not visited_comp[i]:
                # Found a new component, calculate sizes of color groups
                q_comp = deque([i])
                visited_comp[i] = True
                comp_nodes = [i]
                
                while q_comp:
                    u = q_comp.popleft()
                    for v in adj[u]:
                        if not visited_comp[v]:
                            visited_comp[v] = True
                            q_comp.append(v)
                            comp_nodes.append(v)
                
                # Count colors in this component
                cnt_c0 = 0
                cnt_c1 = 0
                for node in comp_nodes:
                    if color[node] == 0:
                        cnt_c0 += 1
                    else:
                        cnt_c1 += 1
                
                # Decide mapping
                # If cnt_c0 >= cnt_c1, map color 0 -> 1 (value 1), color 1 -> 2 (value 2)
                # Else map color 0 -> 2, color 1 -> 1
                map_c0_to_1 = (cnt_c0 >= cnt_c1)
                
                for node in comp_nodes:
                    if color[node] == 0:
                        res[node] = 1 if map_c0_to_1 else 2
                    else:
                        res[node] = 2 if map_c0_to_1 else 1
                        
        print("YES")
        print(*(res))

if __name__ == '__main__':
    solve()
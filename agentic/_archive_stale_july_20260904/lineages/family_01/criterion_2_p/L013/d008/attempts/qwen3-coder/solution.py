import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    adj = [[] for _ in range(n+1)]
    edges = []
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # First, check if the graph is bipartite.
    # For the operators to compose to a self-adjoint operator,
    # the constraint is that for each edge (u,v), the operators T_u and T_v 
    # must be such that T_u ∘ T_v is self-adjoint.
    #
    # Let's analyze when T_i ∘ T_j is self-adjoint.
    # T1(f) = f' + f
    # T2(f) = f' - f
    #
    # T1(T1(f)) = T1(f' + f) = f'' + f' + f' + f = f'' + 2f' + f
    # T2(T2(f)) = T2(f' - f) = f'' - f' - f' + f = f'' - 2f' + f
    # T1(T2(f)) = T1(f' - f) = f'' - f' + f' - f = f'' - f
    # T2(T1(f)) = T2(f' + f) = f'' + f' - f' - f = f'' - f
    #
    # The operator T_i ∘ T_j is self-adjoint iff (T_i ∘ T_j)(f) = f'' + a f' + b f
    # where the coefficient of f' is zero (i.e., a=0). This is because 
    # formally self-adjoint second-order operators have the form f'' + q(x)f.
    #
    # So:
    # T1∘T1: f'' + 2f' + f → not self-adjoint (a=2)
    # T2∘T2: f'' - 2f' + f → not self-adjoint (a=-2)
    # T1∘T2: f'' - f → self-adjoint (a=0)
    # T2∘T1: f'' - f → self-adjoint (a=0)
    #
    # Therefore, for an edge {u,v}, the operators at u and v must be DIFFERENT.
    # That means the graph must be bipartite, and we can assign operators 1 and 2 
    # to the two parts respectively.
    
    color = [-1] * (n+1)
    visited = [False] * (n+1)
    
    def is_bipartite(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    # Check all components
    valid = True
    for i in range(1, n+1):
        if color[i] == -1:
            if not is_bipartite(i):
                valid = False
                break
    
    if not valid:
        print("NO")
        return
    
    # If bipartite, construct the assignment.
    # We want the lexicographically smallest assignment.
    # That means we prefer assigning 1 to lower-indexed nodes when possible.
    # In a bipartite graph with two sets U and V, we need to decide which gets 1 and which gets 2.
    # To get lex smallest, we try assigning 1 to the set that contains node 1.
    # But we must be careful about disconnected components.
    
    # Re-color to ensure consistent labeling across components for lex smallest result.
    # Strategy: for each component, we will assign colors such that the smallest node 
    # in that component gets color 0. Then we'll see if assigning 1 to color 0 gives lex smaller.
    
    final_color = [-1] * (n+1)
    visited_comp = [False] * (n+1)
    
    for i in range(1, n+1):
        if final_color[i] == -1:
            # BFS to get component and determine min node
            queue = deque()
            queue.append(i)
            visited_comp[i] = True
            component_nodes = []
            min_node = i
            
            while queue:
                u = queue.popleft()
                component_nodes.append(u)
                if u < min_node:
                    min_node = u
                for v in adj[u]:
                    if not visited_comp[v]:
                        visited_comp[v] = True
                        queue.append(v)
            
            # Now do BFS again from min_node to get consistent coloring
            comp_color = [-1] * (n+1)
            queue = deque()
            queue.append(min_node)
            comp_color[min_node] = 0
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if comp_color[v] == -1:
                        comp_color[v] = 1 - comp_color[u]
                        queue.append(v)
            
            # Determine which color gets 1
            # We want the color of min_node to be 0 -> assign 1 to it
            # So if comp_color[min_node] == 0, then color 0 -> operator 1
            # If comp_color[min_node] == 1, then color 1 -> operator 1
            target_color_for_one = comp_color[min_node]
            
            for u in component_nodes:
                if comp_color[u] == target_color_for_one:
                    final_color[u] = 0  # Will become 1
                else:
                    final_color[u] = 1  # Will become 2
    
    # Convert to 1-based operators
    result = []
    for i in range(1, n+1):
        if final_color[i] == 0:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # We want to minimize z_1, then z_2, etc.
    # z_i can be 1 or 2.
    # Constraint: z_u & z_v == 0 for all edges (u, v).
    # Since z in {1, 2}, their binary representations are 01 and 10.
    # 1 & 1 = 1 != 0
    # 1 & 2 = 0
    # 2 & 1 = 0
    # 2 & 2 = 2 != 0
    # So, adjacent nodes cannot have the same value.
    # This is a bipartite graph check.
    # To minimize z_1, we should try to set z_1 = 1.
    # If that fails, we try z_1 = 2.
    # If that fails, output NO.
    # If successful, the assignment is unique because we fix the start node
    # and the graph structure forces the rest (or we find a contradiction).

    # We can use a single array for assignments.
    # 0: unassigned, 1: assigned 1, 2: assigned 2.
    assignment = [0] * n

    # We perform BFS/DFS. 
    # Since we want to prioritize z_1=1, we can just try to assign 1 to component of node 0.
    # If it works, great. If not, try 2.
    # For other components, we want to minimize the smallest index in that component.
    # So we iterate nodes 0 to n-1. If unassigned, it's the smallest in its component.
    # We try to assign 1 to it. If it leads to contradiction, we try 2.
    # If both fail, it's NO.
    
    # Note: The problem asks to minimize z_1, then z_2, etc.
    # This greedy approach works:
    # When we encounter the smallest unassigned node $u$ in a component,
    # setting $z_u = 1$ is better than $z_u = 2$ for the objective function.
    # If $z_u=1$ is valid, it yields the optimal assignment for that component
    # (since all other nodes in the component are larger than $u$).
    # If $z_u=1$ is invalid, we must set $z_u=2$.
    # If $z_u=2$ is also invalid, no solution exists.
    
    # Optimization: 
    # We can use a stack for DFS to avoid recursion depth issues.
    
    for i in range(n):
        if assignment[i] == 0:
            # Node i is the smallest index in its connected component.
            # Try to assign 1.
            # We need a way to rollback if it fails.
            # Or just run the check.
            # Since it's a bipartite check, we can just propagate.
            # If we hit a conflict, we know 1 is impossible.
            
            # Let's try assigning 1.
            stack = [i]
            assignment[i] = 1
            possible = True
            path = [i] # To store nodes in this component for rollback
            
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        stack.append(v)
                        path.append(v)
                    elif assignment[v] == assignment[u]:
                        possible = False
                        break
                if not possible:
                    break
            
            if possible:
                continue # Component assigned successfully with 1
            
            # If assigning 1 failed, rollback and try 2
            for node in path:
                assignment[node] = 0
            
            stack = [i]
            assignment[i] = 2
            possible = True
            
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        stack.append(v)
                    elif assignment[v] == assignment[u]:
                        possible = False
                        break
                if not possible:
                    break
            
            if not possible:
                print("NO")
                return

    print("YES")
    print(*(assignment))

if __name__ == '__main__':
    solve()
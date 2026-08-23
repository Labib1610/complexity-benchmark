import sys

# Increase recursion depth to be safe, though N=40 is small
sys.setrecursionlimit(5000)

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # Identify connected components
    # This allows us to solve the problem for each component independently
    # while maintaining the global lexicographical order.
    visited = [False] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            # Sort nodes within component to determine lexicographical order for that component
            comp.sort()
            components.append(comp)
    
    # Global assignment array
    assignment = [0] * (n + 1)
    # Forbidden masks for each node (bitmask of forbidden colors)
    # Colors are 1, 2, 3 mapped to bits 0, 1, 2
    forbidden = [0] * (n + 1)
    
    def dfs(u_idx, comp_nodes):
        # If all nodes in the component are assigned, we found a valid coloring for this component
        if u_idx == len(comp_nodes):
            return True
        
        u = comp_nodes[u_idx]
        
        # Try colors 1, 2, 3 in increasing order to ensure lexicographically smallest
        for c in range(1, 4):
            # Check if color c is valid for u (not forbidden by already assigned neighbors)
            if (forbidden[u] >> (c - 1)) & 1:
                continue
            
            assignment[u] = c
            
            changed_nodes = []
            possible = True
            
            # Update forbidden masks for unassigned neighbors (Forward Checking)
            for v in adj[u]:
                # We only care about neighbors in the current component that are not yet assigned
                # Since components are disjoint, assignment[v] == 0 correctly identifies unassigned nodes in this component
                if assignment[v] == 0:
                    old_mask = forbidden[v]
                    new_mask = old_mask | (1 << (c - 1))
                    if new_mask == 7: # 111 in binary -> all colors forbidden
                        possible = False
                    else:
                        forbidden[v] = new_mask
                        changed_nodes.append((v, old_mask))
                    if not possible:
                        break
            
            if possible:
                if dfs(u_idx + 1, comp_nodes):
                    return True
            
            # Backtrack: revert changes
            for v, old_mask in changed_nodes:
                forbidden[v] = old_mask
            assignment[u] = 0
            
        return False

    # Solve for each component
    for comp in components:
        if not dfs(0, comp):
            print("NO")
            return

    # Output the result
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()
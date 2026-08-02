import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(300000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment, we iterate from 1 to n.
    # If a hub is not assigned, we assign it '1' (the smallest possible)
    # and perform a 2-coloring traversal on its connected component.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS/DFS for this component
            stack = [(i, 1)]
            assignment[i] = 1
            component = []
            
            # Use a list as a stack for iterative DFS
            # To ensure lexicographically smallest, we might need a specific traversal order,
            # but standard 2-coloring is fixed once the first node is chosen.
            # Actually, the choice for the first node of each component is always '1'.
            
            idx_stack = 0
            stack = [i]
            assignment[i] = 1
            
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        stack.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
                        
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()
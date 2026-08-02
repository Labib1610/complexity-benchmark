import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(500000)

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
    
    # To get the lexicographically smallest, we must decide 1, 2, ..., n in order.
    # If a person is not assigned, we try assigning them to 1 first (greedy).
    # If that fails, we try 2.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Component traversal
            stack = [(i, 1)]
            assignment[i] = 1
            component = []
            
            # Use iterative DFS to avoid recursion limits and manage state
            q = [i]
            component.append(i)
            
            # BFS/DFS to find all connected nodes
            head = 0
            while head < len(component):
                u = component[head]
                head += 1
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        component.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
            
    print("YES")
    print(*(assignment[1:]))

solve()
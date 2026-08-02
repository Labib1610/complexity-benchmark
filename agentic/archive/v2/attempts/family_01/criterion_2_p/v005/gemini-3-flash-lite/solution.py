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
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    assignment = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment:
    # We iterate i from 1 to n. If worker i is unassigned, 
    # we try assigning them to shift 1. If that fails, try shift 2.
    # Since we want the smallest overall sequence, we greedily pick 1 
    # whenever possible.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS/DFS for this connected component
            component = []
            stack = [i]
            assignment[i] = 1
            component.append(i)
            
            # Use stack to traverse component
            idx_stack = 0
            while idx_stack < len(component):
                curr = component[idx_stack]
                idx_stack += 1
                for neighbor in adj[curr]:
                    if assignment[neighbor] == 0:
                        assignment[neighbor] = 3 - assignment[curr]
                        component.append(neighbor)
                    elif assignment[neighbor] == assignment[curr]:
                        print("NO")
                        return
            
            # Check if this component's assignment is the lexicographically smallest
            # We already chose 1 for the first node i. If there's another valid 
            # assignment for this component (swapping 1s and 2s), we check which 
            # one is lexicographically smaller.
            
            # Actually, simply picking 1 for the first node of each component 
            # encountered in 1..n order works because for any component, 
            # the choice for the first worker (smallest ID) determines the rest.
            # 1 is smaller than 2, so assigning 1 to the smallest ID is optimal.
            
    print("YES")
    print(*(assignment[1:]))

solve()
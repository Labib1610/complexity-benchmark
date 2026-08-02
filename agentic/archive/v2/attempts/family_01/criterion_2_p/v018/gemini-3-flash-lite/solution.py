import sys

# Increase recursion depth for deep graphs
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
    # If unassigned, try assigning 1. If that fails, try 2.
    # Because it's a 2-coloring problem, each connected component can be 
    # colored in at most 2 ways (swapping 1s and 2s).
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Component found. We want the smallest assignment.
            # Try assigning 1 to the current node i.
            component = []
            stack = [(i, 1)]
            assignment[i] = 1
            
            possible = True
            comp_nodes = []
            
            # DFS to color component
            stack = [i]
            comp_nodes = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        comp_nodes.append(v)
                        stack.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return

            # Now check if this assignment is lexicographically optimal for this component.
            # The two possible colorings for a component are:
            # 1. Keep assignment as is.
            # 2. Swap 1s and 2s.
            # We compare the two resulting colorings based on the first node index.
            
            # Actually, simply greedily assigning 1 to the first unvisited node 
            # in numerical order is sufficient to find the lexicographically smallest.
            # Let's verify: for node i, we have no choice but to pick 1 if we want
            # the lexicographically smallest result.
            
    print("YES")
    print(*(assignment[1:]))

solve()
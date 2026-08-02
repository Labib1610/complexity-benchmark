import sys

# Increase recursion depth for deep graphs
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
    
    # We want the lexicographically smallest sequence.
    # This means for each node i from 1 to n, we prefer assigning it 1.
    # If not possible, we assign it 2.
    # This is a standard 2-coloring problem.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS/DFS for the connected component
            # To get lexicographically smallest, we process nodes in increasing order
            # and try assigning 1 first.
            stack = [i]
            assignment[i] = 1
            
            component = []
            while stack:
                u = stack.pop()
                component.append(u)
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        stack.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
            
            # Check if this assignment is the lexicographically smallest for this component.
            # If we started with 1, we might have had a choice.
            # Actually, for a connected bipartite graph, there are only two ways to color.
            # We compare the two ways and pick the one that is lexicographically smaller.
            
            comp_nodes = sorted(component)
            # Current assignment is one valid way. Let's see if flipping it is smaller.
            # The two assignments are (val) and (3-val).
            # Lexicographical comparison: find the first index where they differ.
            
            # Since we fixed the first node of the component to 1, we check if flipping 
            # makes the sequence smaller. Flipping means 1 becomes 2, 2 becomes 1.
            # A flip is better if the first node where they differ has a smaller value.
            # Since we fixed the first node (smallest ID) to 1, flipping it to 2 
            # would make the sequence lexicographically LARGER.
            # So the current assignment (starting with 1) is already the best.
            
    print("YES")
    print(*(assignment[1:]))

solve()
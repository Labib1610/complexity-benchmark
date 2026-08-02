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
    
    # To get the lexicographically smallest assignment, we iterate 1 to n.
    # If a person is unassigned, we try assigning them to slot 1.
    # If that forces a conflict, we backtrack or fail.
    # Since this is bipartite coloring, we can use a standard BFS/DFS.
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS/DFS for this connected component
            # To ensure lexicographically smallest, we must be careful.
            # Actually, for each connected component, we have two choices:
            # 1. Start node i with 1
            # 2. Start node i with 2
            # We want the smallest overall sequence.
            
            # Use a list to store nodes in this component
            component = []
            stack = [i]
            assignment[i] = 1
            component.append(i)
            
            idx_comp = 0
            while idx_comp < len(component):
                u = component[idx_comp]
                idx_comp += 1
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        component.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
            
            # Check if starting node i with 1 was optimal.
            # If we had assigned i=2, the whole component would be flipped.
            # We compare the two possibilities:
            # Since we want lexicographically smallest, we check the first node
            # in the component (which is the smallest index i).
            # If we assign i=1, the sequence for this component is fixed.
            # If we assign i=2, the sequence is flipped (1->2, 2->1).
            # We want the one that puts 1s in the smallest indices.
            
            # Actually, simply greedily picking 1 for the first unvisited node
            # in numerical order is NOT always optimal for lexicographical order.
            # However, in bipartite coloring, once the first node of a component
            # is fixed, the entire component's assignment is fixed.
            # We should pick the assignment that results in a smaller value
            # at the smallest index in the component.
            
            # Let's re-evaluate: for component starting at i,
            # Assigning i=1 makes the sequence S1, S2...
            # Assigning i=2 makes the sequence S1', S2'... where S_j' = 3 - S_j
            # We want the one where the first index j where S_j != S_j' is 1.
            # That is always true because S_i=1 and S_i'=2.
            # So S_i=1 is always better for the lexicographical order.
            # Thus, greedy assignment works!
            
    print("YES")
    print(*(assignment[1:]))

solve()
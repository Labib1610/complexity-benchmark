import sys
from collections import deque

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

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # We need to find the lexicographically smallest valid assignment.
    # This is equivalent to finding the lexicographically smallest binary string
    # that satisfies the constraints (where 1=long, 2=short).
    # We can use a greedy approach: iterate through nodes 1 to n.
    # If a node is not yet assigned, we tentatively assign it 1.
    # Then we check if this assignment creates a conflict with any already assigned neighbor.
    # If it creates a conflict, we must assign it 2.
    # If assigning 2 also creates a conflict, we must backtrack.
    # Since the graph is bipartite, we can use a BFS-based approach to assign connected components.
    # To ensure lexicographical minimality, we process nodes in order 1 to n.
    # When we encounter an unassigned node, we try to assign it 1.
    # We then propagate the constraints to its connected component.
    # If a conflict is found during propagation, we backtrack and assign the starting node 2.
    # If a conflict is still found, the graph is not bipartite.

    assignment = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Try assigning 1 to node i
            # We use a queue for BFS traversal of the connected component
            # We need to track the nodes involved in this attempt to backtrack if necessary
            
            # Attempt 1: assign i to 1
            queue = deque([i])
            assignment[i] = 1
            path = [i]
            conflict = False
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        path.append(v)
                        queue.append(v)
                    elif assignment[v] == assignment[u]:
                        conflict = True
                        break
                if conflict:
                    break
            
            if conflict:
                # Backtrack: reset assignments for nodes in path
                for node in path:
                    assignment[node] = 0
                
                # Attempt 2: assign i to 2
                queue = deque([i])
                assignment[i] = 2
                path = [i]
                conflict = False
                
                while queue:
                    u = queue.popleft()
                    for v in adj[u]:
                        if assignment[v] == 0:
                            assignment[v] = 3 - assignment[u]
                            path.append(v)
                            queue.append(v)
                        elif assignment[v] == assignment[u]:
                            conflict = True
                            break
                    if conflict:
                        break
                
                if conflict:
                    print("NO")
                    return

    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()
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

    # We want the lexicographically smallest valid configuration.
    # Lexicographically smallest means we prefer type 1 (100g) over type 2 (200g).
    # Constraint: for every edge (u, v), types must be different (1+2=300g).
    # This is a graph bipartition problem.
    # To get the lexicographically smallest valid assignment:
    # We process nodes in order 1 to n.
    # If a node is unassigned, we try to assign it type 1.
    # This forces its neighbors to be type 2.
    # We propagate these forced assignments using BFS.
    # If we encounter a conflict, the configuration is impossible.
    
    type_assignment = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if type_assignment[i] == 0:
            # Start a BFS for this component
            # We want to assign i to 1 if possible (lexicographically smallest)
            # But we must check if assigning i to 1 is consistent with current assignments.
            # Since i is unassigned, its neighbors are also unassigned (otherwise i would be assigned via propagation).
            # So we can freely choose the root's type. We choose 1.
            
            queue = deque([i])
            type_assignment[i] = 1
            
            while queue:
                u = queue.popleft()
                current_type = type_assignment[u]
                required_neighbor_type = 3 - current_type
                
                for v in adj[u]:
                    if type_assignment[v] == 0:
                        type_assignment[v] = required_neighbor_type
                        queue.append(v)
                    elif type_assignment[v] != required_neighbor_type:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
            
    if not possible:
        print("NO")
    else:
        print("YES")
        print(*(type_assignment[1:]))

if __name__ == '__main__':
    solve()
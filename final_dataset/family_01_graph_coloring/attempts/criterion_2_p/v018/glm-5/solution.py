import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # We want lexicographically smallest assignment.
    # This means we want to assign s[i] = 1 whenever possible.
    # If we use BFS starting from node 1, then 2, etc.,
    # we process nodes in increasing order.
    # When we process a node u, if it's unassigned, we assign it 1.
    # Then we assign its neighbors 2.
    # If a neighbor is already assigned, we check for conflict.
    # If conflict, output NO.
    
    assignment = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS for this component
            queue = deque([i])
            assignment[i] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        queue.append(v)
                    elif assignment[v] == assignment[u]:
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
        print(*(assignment[1:]))

if __name__ == '__main__':
    solve()
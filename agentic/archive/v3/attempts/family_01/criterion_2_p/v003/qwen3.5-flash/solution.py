import sys
from collections import deque

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
    
    # Build adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
        
    # Array to store the mode assignment: 0 = unvisited, 1 = Mode 1, 2 = Mode 2
    ans = [0] * (n + 1)
    
    # Iterate through all components
    for i in range(1, n + 1):
        if ans[i] == 0:
            # Found a new connected component.
            # To achieve the lexicographically smallest sequence, we assign Mode 1
            # to the smallest index node in the component. Since we iterate i from 1 to n,
            # i is guaranteed to be the smallest index in this unvisited component.
            ans[i] = 1
            q = deque([i])
            
            # BFS to traverse the component and check bipartiteness
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if ans[v] == 0:
                        # Assign the opposite mode
                        ans[v] = 3 - ans[u]
                        q.append(v)
                    elif ans[v] == ans[u]:
                        # Conflict detected: adjacent nodes have the same mode
                        print("NO")
                        return
    
    # If we successfully assign all components
    print("YES")
    print(*(ans[1:]))

if __name__ == '__main__':
    solve()
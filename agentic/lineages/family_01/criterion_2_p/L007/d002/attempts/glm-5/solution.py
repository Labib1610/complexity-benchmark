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

    adj = [[] for _ in range(n + 1))
    
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # We want the lexicographically smallest valid sequence.
    # Valid values are 1 and 2. Lexicographically smallest means we should
    # prefer 1 over 2 whenever possible.
    # The constraint is that for every edge (u, v), s[u] * s[v] = 2.
    # This implies one endpoint must be 1 and the other must be 2.
    # This is a bipartite graph check.
    # To get the lexicographically smallest sequence, we perform BFS
    # and assign the smallest valid value (1) to the current node, and
    # the other valid value (2) to its neighbors.
    
    color = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS from node i
            queue = deque([i])
            color[i] = 1 # Assign 1 to the root of the component
            
            while queue:
                u = queue.popleft()
                
                for v in adj[u]:
                    if color[v] == 0:
                        # The constraint s[u] * s[v] = 2 implies:
                        # if s[u] == 1, s[v] must be 2.
                        # if s[u] == 2, s[v] must be 1.
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        # Conflict found
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
        print(*(color[1:n+1]))

if __name__ == '__main__':
    solve()
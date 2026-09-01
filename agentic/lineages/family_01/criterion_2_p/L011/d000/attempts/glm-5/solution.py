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
    
    # Values: 0 = unassigned, 1 = assigned 1, 2 = assigned 2
    val = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if val[i] == 0:
            # BFS for this component
            queue = deque([i])
            val[i] = 1  # Lexicographically smallest starts with 1
            valid_component = True
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    expected = 3 - val[u]
                    if val[v] == 0:
                        val[v] = expected
                        queue.append(v)
                    elif val[v] != expected:
                        valid_component = False
                        # We can break early but need to finish processing to mark
                        # Actually, we can just return NO immediately
                        print("NO")
                        return
            
            # Check if component is bipartite (valid)
            # The check is done inside the loop above
    
    # If we reach here, all components are valid
    print("YES")
    print(*(val[1:]))

if __name__ == "__main__":
    solve()
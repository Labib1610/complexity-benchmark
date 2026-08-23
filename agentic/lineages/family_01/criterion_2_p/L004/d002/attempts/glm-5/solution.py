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

    # Values: 0 = unassigned, 1 = factor 1, 2 = factor 2
    val = [0] * (n + 1)
    
    # Process components in order 1 to n to ensure lexicographically smallest result
    for i in range(1, n + 1):
        if val[i] == 0:
            # Start BFS for this component
            # Try assigning 1 to the root node i
            # If contradiction found, we will try assigning 2 to root node i
            # Since we iterate i from 1 to n, assigning 1 to root i is lexicographically preferred
            
            queue = deque([i])
            val[i] = 1
            path = [i]
            possible = True
            
            while queue:
                u = queue.popleft()
                pu = val[u]
                # The product must be 2.
                # If u has factor 1, neighbor must have factor 2.
                # If u has factor 2, neighbor must have factor 1.
                required_neighbor_val = 2 if pu == 1 else 1
                
                for v in adj[u]:
                    if val[v] == 0:
                        val[v] = required_neighbor_val
                        path.append(v)
                        queue.append(v)
                    elif val[v] != required_neighbor_val:
                        possible = False
                        # Clear queue to break loop fast
                        queue.clear()
                        break
            
            if possible:
                continue
            
            # If assignment starting with val[i]=1 failed, reset and try val[i]=2
            for node in path:
                val[node] = 0
            
            queue = deque([i])
            val[i] = 2
            possible = True
            
            while queue:
                u = queue.popleft()
                pu = val[u]
                required_neighbor_val = 2 if pu == 1 else 1
                
                for v in adj[u]:
                    if val[v] == 0:
                        val[v] = required_neighbor_val
                        queue.append(v)
                    elif val[v] != required_neighbor_val:
                        possible = False
                        queue.clear()
                        break
            
            if not possible:
                print("NO")
                return

    print("YES")
    print(*(val[1:]))

if __name__ == '__main__':
    solve()
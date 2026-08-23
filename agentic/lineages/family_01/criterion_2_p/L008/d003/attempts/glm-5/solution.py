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

    # Values: 0=unassigned, 1, 2
    val = [0] * (n + 1)
    possible = True

    for i in range(1, n + 1):
        if val[i] == 0:
            # BFS for connected component
            # Start with lexicographically smallest valid value for the start node
            val[i] = 1
            queue = deque([i])
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    # Constraint: val[u] * val[v] == 2
                    # If val[u] == 1, val[v] must be 2
                    # If val[u] == 2, val[v] must be 1
                    required = 2 // val[u]
                    
                    if val[v] == 0:
                        val[v] = required
                        queue.append(v)
                    elif val[v] != required:
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
        # Output values 1 to n
        print(*(val[1:]))

if __name__ == '__main__':
    solve()
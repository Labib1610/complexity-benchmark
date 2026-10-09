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

    # 0: unassigned, 1: assigned value 1, 2: assigned value 2
    assignment = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            # Start BFS for this component
            queue = deque([i])
            assignment[i] = 1
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if assignment[v] == 0:
                        # XOR must be 3. If u is 1, v must be 2. If u is 2, v must be 1.
                        assignment[v] = 3 - assignment[u]
                        queue.append(v)
                    elif assignment[v] == assignment[u]:
                        # Conflict found
                        print("NO")
                        return
    
    print("YES")
    print(*(assignment[1:]))

if __name__ == '__main__':
    solve()
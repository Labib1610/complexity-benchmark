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

    # Sort adjacency lists to process neighbors in increasing order.
    # This helps in finding the lexicographically smallest valid assignment.
    for i in range(1, n + 1):
        adj[i].sort()

    # State array: 0 = unvisited, 1 = spin 1, 2 = spin 2
    state = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if state[i] == 0:
            # Start a BFS for the connected component containing i
            queue = deque([i])
            state[i] = 1  # Assign the lexicographically smallest spin
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if state[v] == 0:
                        state[v] = 3 - state[u]
                        queue.append(v)
                    elif state[v] == state[u]:
                        # Conflict found
                        sys.stdout.write("NO")
                        return

    # If no conflicts, output the result
    # Format the output string efficiently
    result = []
    result.append("YES")
    result.append(" ".join(map(str, state[1:])))
    sys.stdout.write("\n".join(result))

if __name__ == '__main__':
    solve()
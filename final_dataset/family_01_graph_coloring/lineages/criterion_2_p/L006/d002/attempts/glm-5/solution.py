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

    # State: 0 = unvisited, 1 = assigned 1, 2 = assigned 2
    state = [0] * (n + 1)
    possible = True

    for i in range(1, n + 1):
        if state[i] == 0:
            # BFS for this component
            # We want lexicographically smallest, so we prefer state 1.
            # Start node i gets state 1.
            queue = deque([i])
            state[i] = 1
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if state[v] == 0:
                        state[v] = 3 - state[u]
                        queue.append(v)
                    elif state[v] == state[u]:
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
        print(*(state[1:]))

if __name__ == '__main__':
    solve()
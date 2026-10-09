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

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n
    is_possible = True
    
    # We use BFS to check bipartiteness and assign colors.
    # To ensure lexicographically smallest output, we iterate vertices from 0 to n-1.
    # If a vertex is uncolored, we start a BFS from it assigning color 1.
    # This greedy approach works because assigning color 1 to the smallest index
    # in a connected component is always compatible with the lexicographically smallest valid assignment.
    
    for i in range(n):
        if color[i] == 0:
            # Start BFS
            queue = deque([i])
            color[i] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_possible = False
                        break
                if not is_possible:
                    break
        if not is_possible:
            break

    if not is_possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, color)))

if __name__ == '__main__':
    solve()
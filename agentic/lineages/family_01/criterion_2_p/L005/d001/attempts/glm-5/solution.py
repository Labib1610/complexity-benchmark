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

    color = [-1] * n
    possible = True

    for i in range(n):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
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
        print(*(x + 1 for x in color))

if __name__ == '__main__':
    solve()
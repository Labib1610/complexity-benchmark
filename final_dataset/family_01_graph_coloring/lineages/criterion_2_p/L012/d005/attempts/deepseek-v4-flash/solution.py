import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -=  ​1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n  # 0 uncolored, 1 or 2

    for i in range(n):
        if color[i] != 0:
            continue

        # try color 1
        ok = True
        stack = [i]
        color[i] = 1
        visited = [i]

        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - color[u]
                    visited.append(v)
                    stack.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
            if not ok:
                break

        if not ok:
            # revert this attempt
            for v in visited:
                color[v] = 0

            # try color 2
            ok = True
            stack = [i]
            color[i] =  ​2
            visited = [i]

            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] =  ​3 - color[u]
                        visited.append(v)
                        stack.append(v)
                    elif color[v] == color[u]:
                        ok = False
                        break
                if not ok:
                    break

            if not ok:
                print("NO")
                return

    print("YES")
    print(' '.join(str(color[i]) for i in range(n)))

if __name__ == "__main__":
    solve()
import sys
from sys import setrecursionlimit

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    possible = True

    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            stack = [i]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        nonlocal_possible = False
                        print("NO")
                        return

    print("YES")
    print(' '.join(map(str, color[1:])))

solve()
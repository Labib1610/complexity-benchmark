import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    color = [-1] * n
    part = [[], []]
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            part[0].append(i)
            q = deque([i])
            while q:
                u = q.popleft()
                for v in g[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        part[color[v]].append(v)
                        q.append(v)

    # take the larger part as base
    if len(part[0]) < len(part[1]):
        part[0], part[1] = part[1], part[0]

    if k > len(part[0]) + len(part[1]):
        print("NO")
        return

    if k <= len(part[0]):
        chosen = part[0][:k]
    else:
        need = k - len(part[0])
        chosen = part[0] + part[1][:need]

    print("YES")
    print(" ".join(str(x + 1) for x in chosen))

if __name__ == "__main__":
    solve()
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * n
ok = True

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
            if not ok:
                break
    if not ok:
        break

if not ok:
    print("NO")
else:
    # color 0 -> mode 1, color 1 -> mode 2
    # Try both assignments and pick the one with smaller energy
    def energy(assign):
        e = 0
        for i, val in enumerate(assign):
            e += val * (1 << (n - i - 1))
        return e

    assign1 = [1 if c == 0 else 2 for c in color]
    assign2 = [2 if c == 0 else 1 for c in color]

    if energy(assign1) <= energy(assign2):
        best = assign1
    else:
        best = assign2

    print("YES")
    print(" ".join(map(str, best)))
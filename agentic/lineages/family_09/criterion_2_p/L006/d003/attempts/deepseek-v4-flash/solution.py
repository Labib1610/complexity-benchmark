import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
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

# If not bipartite (shouldn't happen per problem statement)
if not ok:
    print("NO")
    sys.exit()

A = [i for i in range(n) if color[i] == 0]
B = [i for i in range(n) if color[i] == 1]

def try_build(main, other):
    # take all from main, then add from other that are not adjacent to main
    chosen = set(main)
    for v in other:
        if all(u not in chosen for u in adj[v]):
            chosen.add(v)
    return chosen

# Try both orientations
chosen1 = try_build(A, B)
chosen2 = try_build(B, A)

if len(chosen1) >= k:
    res = list(chosen1)[:k]
    print("YES")
    print(" ".join(str(x+1) for x in res))
elif len(chosen2) >= k:
    res = list(chosen2)[:k]
    print("YES")
    print(" ".join(str(x+1) for x in res))
else:
    print("NO")
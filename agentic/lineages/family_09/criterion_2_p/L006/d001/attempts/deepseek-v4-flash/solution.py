import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

color = [-1] * n
sets = [[], []]

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        sets[0].append(i)
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    sets[color[v]].append(v)
                    q.append(v)

a = sets[0]
b = sets[1]

# Try to pick k from one set if possible
if len(a) >= k:
    print("YES")
    print(" ".join(str(x+1) for x in a[:k]))
elif len(b) >= k:
    print("YES")
    print(" ".join(str(x+1) for x in b[:k]))
else:
    # Need to take from both sets
    # Take as many as possible from smaller set, rest from larger
    if len(a) > len(b):
        a, b = b, a
    take_a = min(len(a), k)
    take_b = k - take_a
    if take_b <= len(b):
        print("YES")
        res = a[:take_a] + b[:take_b]
        print(" ".join(str(x+1) for x in res))
    else:
        print("NO")
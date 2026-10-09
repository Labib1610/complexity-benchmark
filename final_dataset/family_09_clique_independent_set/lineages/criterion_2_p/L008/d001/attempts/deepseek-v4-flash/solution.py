import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * (n + 1)
groupA = []
groupB = []

for i in range(1, n + 1):
    if color[i] == -1:
        color[i] = 0
        groupA.append(i)
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    if color[v] == 0:
                        groupA.append(v)
                    else:
                        groupB.append(v)
                    q.append(v)

if len(groupA) < len(groupB):
    groupA, groupB = groupB, groupA

if len(groupA) < k:
    print("NO")
else:
    print("YES")
    print(" ".join(map(str, groupA[:k])))
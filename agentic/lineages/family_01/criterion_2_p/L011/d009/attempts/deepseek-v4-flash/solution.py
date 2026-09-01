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

state = [-1] * n

for i in range(n):
    if state[i] == -1:
        state[i] = 1
        q = deque([i])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if state[v] == -1:
                    state[v] = 3 - state[u]
                    q.append(v)
                elif state[v] == state[u]:
                    print("NO")
                    sys.exit()

print("YES")
print(" ".join(str(state[i]) for i in range(n)))
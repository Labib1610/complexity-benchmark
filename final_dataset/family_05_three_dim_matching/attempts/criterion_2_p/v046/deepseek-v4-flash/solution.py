import sys
from collections import deque

input = sys.stdin.readline

k, t = map(int, input().split())
adj = [[] for _ in range(k + 1)]

for _ in range(t):
    p, a, w = map(int, input().split())
    adj[p].append(w)

# Hopcroft-Karp for maximum bipartite matching
match_pilot = [0] * (k + 1)  # which window is matched to pilot
match_window = [0] * (k + 1) # which pilot is matched to window
dist = [0] * (k + 1)

def bfs():
    q = deque()
    for u in range(1, k + 1):
        if match_pilot[u] == 0:
            dist[u] = 0
            q.append(u)
        else:
            dist[u] = float('inf')
    found = False
    while q:
        u = q.popleft()
        for v in adj[u]:
            pu = match_window[v]
            if pu != 0 and dist[pu] == float('inf'):
                dist[pu] = dist[u] + 1
                q.append(pu)
            elif pu == 0:
                found = True
    return found

def dfs(u):
    for v in adj[u]:
        pu = match_window[v]
        if pu == 0 or (dist[pu] == dist[u] + 1 and dfs(pu)):
            match_pilot[u] = v
            match_window[v] = u
            return True
    dist[u] = float('inf')
    return False

matching = 0
while bfs():
    for u in range(1, k + 1):
        if match_pilot[u] == 0 and dfs(u):
            matching += 1

if matching == k:
    print("YES")
    for p in range(1, k + 1):
        print(p, p, match_pilot[p])  # aircraft number equals pilot number due to constraints
else:
    print("NO")
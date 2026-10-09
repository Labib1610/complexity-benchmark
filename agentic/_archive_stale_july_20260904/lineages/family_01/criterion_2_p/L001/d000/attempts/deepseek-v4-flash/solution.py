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

def bfs(start):
    q = deque([start])
    color[start] = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                q.append(v)
            elif color[v] == color[u]:
                return False
    return True

possible = True
for i in range(n):
    if color[i] == -1:
        if not bfs(i):
            possible = False
            break

if not possible:
    print("NO")
else:
    # We want lexicographically smallest: assign 1 to color 0, 2 to color 1
    # But we can flip colors in each component to get smaller values at earlier indices
    # We'll do a BFS/DFS to decide flipping per component
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # collect component
            comp = []
            q = deque([i])
            visited[i] = True
            comp.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
                        comp.append(v)
            # Check if flipping gives smaller lexicographic order
            # Count how many in comp have color 0 vs 1
            # We can try both assignments and pick smaller
            assign1 = []
            assign2 = []
            for node in comp:
                if color[node] == 0:
                    assign1.append(1)
                    assign2.append(2)
                else:
                    assign1.append(2)
                    assign2.append(1)
            # We need to compare in original index order
            comp_sorted = sorted(comp)
            # Build sequences in original order
            seq1 = []
            seq2 = []
            for node in comp_sorted:
                if color[node] == 0:
                    seq1.append(1)
                    seq2.append(2)
                else:
                    seq1.append(2)
                    seq2.append(1)
            if seq2 < seq1:
                # flip colors in this component
                for node in comp:
                    color[node] ^= 1

    result = [1 if color[i] == 0 else 2 for i in range(n)]
    print("YES")
    print(" ".join(map(str, result)))
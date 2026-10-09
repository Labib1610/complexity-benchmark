import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N, E, F = map(int, input().split())
    vital = set(map(int, input().split()))
    
    adj = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)
    
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        degree[u] += 1
        degree[v] += 1
    
    if F == 1:
        print(0)
        return
    
    # Remove non-vital leaves
    q = deque()
    removed = [False] * (N + 1)
    for i in range(1, N + 1):
        if degree[i] == 1 and i not in vital:
            q.append(i)
    
    while q:
        u = q.popleft()
        removed[u] = True
        for v, w in adj[u]:
            if not removed[v]:
                degree[v] -= 1
                if degree[v] == 1 and v not in vital:
                    q.append(v)
    
    # Sum weights of edges where both endpoints are not removed
    total = 0
    for u in range(1, N + 1):
        if removed[u]:
            continue
        for v, w in adj[u]:
            if u < v and not removed[v]:
                total += w
    
    print(total)

if __name__ == "__main__":
    solve()
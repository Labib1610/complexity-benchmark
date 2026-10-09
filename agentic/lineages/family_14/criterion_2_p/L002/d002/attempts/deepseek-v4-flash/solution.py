import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    critical = set(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    if t <= 1:
        print(0)
        return
    
    degree = [len(adj[i]) for i in range(n + 1)]
    in_queue = [True] * (n + 1)
    q = deque()
    
    for i in range(1, n + 1):
        if degree[i] == 1 and i not in critical:
            q.append(i)
            in_queue[i] = False
    
    total_weight = 0
    while q:
        u = q.popleft()
        for v, w in adj[u]:
            if in_queue[v]:
                total_weight += w
                degree[v] -= 1
                if degree[v] == 1 and v not in critical:
                    q.append(v)
                    in_queue[v] = False
    
    print(total_weight)

if __name__ == "__main__":
    solve()
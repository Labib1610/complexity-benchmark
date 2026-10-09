import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, m, t = map(int, input().split())
    targets = set(map(int, input().split()))
    adj = [[] for _ in range(n+1)]
    total_cost = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
        total_cost += w
    if t <= 1:
        print(0)
        return
    degree = [0]*(n+1)
    for i in range(1,n+1):
        degree[i] = len(adj[i])
    removed_cost = 0
    q = deque()
    visited = [False]*(n+1)
    for i in range(1,n+1):
        if degree[i] == 1 and i not in targets:
            q.append(i)
            visited[i] = True
    while q:
        v = q.popleft()
        for to, w in adj[v]:
            if not visited[to]:
                degree[to] -= 1
                removed_cost += w
                if degree[to] == 1 and to not in targets:
                    q.append(to)
                    visited[to] = True
    print(total_cost - removed_cost)

if __name__ == "__main__":
    main()
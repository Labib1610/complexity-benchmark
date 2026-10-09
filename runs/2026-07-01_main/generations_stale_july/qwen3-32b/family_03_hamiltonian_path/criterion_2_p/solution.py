import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        in_degree[v] += 1

    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
    top_order = []
    while q:
        u = q.popleft()
        top_order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    dp = [0] * (n + 1)
    prev = [0] * (n + 1)
    for u in top_order:
        for v in adj[u]:
            if dp[v] < dp[u] + 1:
                dp[v] = dp[u] + 1
                prev[v] = u

    max_len = 0
    last_node = 1
    for i in range(1, n + 1):
        if dp[i] > max_len:
            max_len = dp[i]
            last_node = i

    if max_len != n - 1:
        print("NO")
    else:
        path = []
        current = last_node
        for _ in range(n):
            path.append(current)
            current = prev[current]
        path.reverse()
        print("YES")
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()
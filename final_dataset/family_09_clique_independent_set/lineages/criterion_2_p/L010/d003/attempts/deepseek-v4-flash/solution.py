import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)
    color[0] = 0
    part1 = []
    part2 = []

    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            part1.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            part1.append(v)
                        else:
                            part2.append(v)
                        q.append(v)

    # The graph is bipartite, so we can pick from the larger partition
    if len(part1) < len(part2):
        part1, part2 = part2, part1

    if len(part1) >= k:
        print("YES")
        print(" ".join(map(str, part1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()
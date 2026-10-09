import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n
    possible = True

    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break

    if not possible:
        print("NO")
        return

    # Convert 0/1 to 1/2
    ans = [c + 1 for c in color]
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()
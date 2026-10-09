import sys
from collections import deque

def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * n

    for start in range(n):
        if color[start] != 0:
            continue

        color[start] = 1
        queue = deque([start])

        while queue:
            u = queue.popleft()
            required = 3 - color[u]

            for v in graph[u]:
                if color[v] == 0:
                    color[v] = required
                    queue.append(v)
                elif color[v] == color[u]:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)) + "\n")

if __name__ == "__main__":
    main()
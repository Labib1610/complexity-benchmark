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

    shift = [0] * n

    for start in range(n):
        if shift[start] != 0:
            continue

        shift[start] = 1
        queue = deque([start])

        while queue:
            u = queue.popleft()
            required = 3 - shift[u]

            for v in graph[u]:
                if shift[v] == 0:
                    shift[v] = required
                    queue.append(v)
                elif shift[v] != required:
                    print("NO")
                    return

    print("YES")
    print(*shift)

if __name__ == "__main__":
    main()
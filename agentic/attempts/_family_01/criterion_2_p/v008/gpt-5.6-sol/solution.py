import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph = [[] for _ in range(n)]

    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        graph[u].append(v)
        graph[v].append(u)

    shift = [0] * n
    queue = deque()

    for start in range(n):
        if shift[start] != 0:
            continue

        shift[start] = 1
        queue.append(start)

        while queue:
            u = queue.popleft()
            required = 3 - shift[u]

            for v in graph[u]:
                if shift[v] == 0:
                    shift[v] = required
                    queue.append(v)
                elif shift[v] != required:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, shift)) + "\n")

if __name__ == "__main__":
    main()
import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph = [[] for _ in range(n + 1)]

    pos = 2
    for _ in range(m):
        u = data[pos]
        v = data[pos + 1]
        pos += 2
        graph[u].append(v)
        graph[v].append(u)

    color = bytearray(n + 1)
    queue = deque()

    for start in range(1, n + 1):
        if color[start]:
            continue

        color[start] = 1
        queue.append(start)

        while queue:
            u = queue.popleft()
            other = 3 - color[u]

            for v in graph[u]:
                if color[v] == 0:
                    color[v] = other
                    queue.append(v)
                elif color[v] == color[u]:
                    sys.stdout.write("NO\n")
                    return

    assignment = ' '.join(map(str, color[1:]))
    sys.stdout.write("YES\n" + assignment + "\n")

if __name__ == "__main__":
    main()
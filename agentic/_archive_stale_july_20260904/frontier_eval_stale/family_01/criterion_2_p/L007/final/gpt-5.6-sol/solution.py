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

    state = [0] * n

    for start in range(n):
        if state[start] != 0:
            continue

        state[start] = 1
        queue = deque([start])

        while queue:
            u = queue.popleft()
            required = 3 - state[u]

            for v in graph[u]:
                if state[v] == 0:
                    state[v] = required
                    queue.append(v)
                elif state[v] != required:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, state)) + "\n")

if __name__ == "__main__":
    main()
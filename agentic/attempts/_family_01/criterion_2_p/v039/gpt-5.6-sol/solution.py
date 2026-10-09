import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[0], data[1]

    graph = [[] for _ in range(n)]
    pos = 2
    for _ in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        graph[u].append(v)
        graph[v].append(u)

    phase = [0] * n

    for start in range(n):
        if phase[start] != 0:
            continue

        phase[start] = 1
        queue = deque([start])

        while queue:
            u = queue.popleft()
            opposite = 3 - phase[u]

            for v in graph[u]:
                if phase[v] == 0:
                    phase[v] = opposite
                    queue.append(v)
                elif phase[v] == phase[u]:
                    sys.stdout.write("NO\n")
                    return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, phase)) + "\n")

if __name__ == "__main__":
    main()
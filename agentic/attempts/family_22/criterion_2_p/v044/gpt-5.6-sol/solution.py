import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    idx = 2
    for _ in range(m):
        a, b = data[idx], data[idx + 1]
        idx += 2
        graph[a].append(b)
        indegree[b] += 1

    queue = deque(i for i in range(1, n + 1) if indegree[i] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    if len(order) != n:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, order)) + "\n")

if __name__ == "__main__":
    main()
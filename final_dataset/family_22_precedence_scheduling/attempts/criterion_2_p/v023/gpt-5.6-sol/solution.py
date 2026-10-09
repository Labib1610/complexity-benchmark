import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    graph = [[] for _ in range(n)]
    indegree = [0] * n

    idx = 2
    for _ in range(m):
        x = data[idx] - 1
        y = data[idx + 1] - 1
        idx += 2
        graph[x].append(y)
        indegree[y] += 1

    queue = deque(i for i in range(n) if indegree[i] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node + 1)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) != n:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, order)) + "\n")

if __name__ == "__main__":
    main()
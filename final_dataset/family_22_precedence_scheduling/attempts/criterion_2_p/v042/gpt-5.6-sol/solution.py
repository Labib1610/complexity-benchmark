import sys
from collections import deque

def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    indegree = [0] * n

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        indegree[b] += 1

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
        print("NO")
    else:
        print("YES")
        print(*order)

if __name__ == "__main__":
    main()
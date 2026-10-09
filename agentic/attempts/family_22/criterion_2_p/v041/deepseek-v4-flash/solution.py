from collections import deque
import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque([i for i in range(1, n + 1) if indegree[i] == 0])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(order) != n:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, order)))

if __name__ == "__main__":
    main()
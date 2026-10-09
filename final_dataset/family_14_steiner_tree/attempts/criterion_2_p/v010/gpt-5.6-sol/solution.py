import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)
    t = next(it)

    priority = [False] * n
    for _ in range(t):
        priority[next(it) - 1] = True

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        graph[u].append((v, w))
        graph[v].append((u, w))

    if t <= 1:
        print(0)
        return

    parent = [-1] * n
    parent_weight = [0] * n
    order = [0]
    parent[0] = 0

    for u in order:
        for v, w in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                parent_weight[v] = w
                order.append(v)

    count = [0] * n
    answer = 0

    for u in reversed(order):
        count[u] += priority[u]
        if u != 0:
            if 0 < count[u] < t:
                answer += parent_weight[u]
            count[parent[u]] += count[u]

    print(answer)

if __name__ == "__main__":
    main()
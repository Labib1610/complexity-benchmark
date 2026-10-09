import sys

def main():
    data = map(int, sys.stdin.buffer.read().split())
    n = next(data)
    m = next(data)
    t = next(data)

    required = bytearray(n)
    for _ in range(t):
        required[next(data) - 1] = 1

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = next(data) - 1
        v = next(data) - 1
        w = next(data)
        graph[u].append((v, w))
        graph[v].append((u, w))

    parent = [-2] * n
    parent_weight = [0] * n
    parent[0] = -1
    order = [0]

    for u in order:
        for v, w in graph[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                order.append(v)

    count = list(required)
    answer = 0

    for u in reversed(order):
        p = parent[u]
        if p >= 0:
            if 0 < count[u] < t:
                answer += parent_weight[u]
            count[p] += count[u]

    print(answer)

if __name__ == "__main__":
    main()
import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)
    t = next(it)

    terminal = bytearray(n)
    for _ in range(t):
        terminal[next(it) - 1] = 1

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

    count = list(terminal)
    answer = 0

    for u in reversed(order[1:]):
        if 0 < count[u] < t:
            answer += parent_weight[u]
        count[parent[u]] += count[u]

    print(answer)

if __name__ == "__main__":
    main()
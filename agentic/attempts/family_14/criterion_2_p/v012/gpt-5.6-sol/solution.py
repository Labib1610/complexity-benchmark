import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)
    t = next(it)

    priority = [False] * (n + 1)
    for _ in range(t):
        priority[next(it)] = True

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        graph[u].append((v, w))
        graph[v].append((u, w))

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = [1]
    parent[1] = -1

    for u in order:
        for v, w in graph[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                order.append(v)

    terminal_count = [0] * (n + 1)
    answer = 0

    for u in reversed(order):
        count = 1 if priority[u] else 0
        for v, _ in graph[u]:
            if parent[v] == u:
                count += terminal_count[v]
        terminal_count[u] = count

        if u != 1 and 0 < count < t:
            answer += parent_weight[u]

    print(answer)

if __name__ == "__main__":
    main()
import sys

def main():
    it = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(it)
    m = next(it)
    t = next(it)

    critical = [0] * (n + 1)
    for _ in range(t):
        critical[next(it)] = 1

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        graph[u].append((v, w))
        graph[v].append((u, w))

    del it

    if t <= 1:
        print(0)
        return

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    parent[1] = -1
    order = [1]

    for u in order:
        for v, w in graph[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                order.append(v)

    terminal_count = critical
    answer = 0

    for u in reversed(order[1:]):
        count = terminal_count[u]
        if 0 < count < t:
            answer += parent_weight[u]
        terminal_count[parent[u]] += count

    print(answer)

if __name__ == "__main__":
    main()
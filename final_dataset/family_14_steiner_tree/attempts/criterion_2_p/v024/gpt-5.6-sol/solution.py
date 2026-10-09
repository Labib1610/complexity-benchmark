import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)

    n = next(it)
    m = next(it)
    t = next(it)

    is_hub = [0] * (n + 1)
    for _ in range(t):
        is_hub[next(it)] = 1

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        w = next(it)
        graph[u].append((v, w))
        graph[v].append((u, w))

    if t <= 1:
        print(0)
        return

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = [1]

    for u in order:
        for v, w in graph[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                order.append(v)

    hub_count = is_hub[:]
    answer = 0

    for u in reversed(order[1:]):
        if 0 < hub_count[u] < t:
            answer += parent_weight[u]
        hub_count[parent[u]] += hub_count[u]

    print(answer)

if __name__ == "__main__":
    main()
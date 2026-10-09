import sys

def main():
    data = map(int, sys.stdin.buffer.read().split())
    n = next(data)
    m = next(data)
    t = next(data)

    marked = bytearray(n + 1)
    for _ in range(t):
        marked[next(data)] = 1

    if t <= 1:
        print(0)
        return

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(data)
        v = next(data)
        w = next(data)
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

    count = list(marked)
    answer = 0

    for u in reversed(order[1:]):
        if 0 < count[u] < t:
            answer += parent_weight[u]
        count[parent[u]] += count[u]

    print(answer)

if __name__ == "__main__":
    main()
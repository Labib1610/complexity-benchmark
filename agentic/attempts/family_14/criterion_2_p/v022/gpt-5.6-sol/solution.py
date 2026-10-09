import sys


def main():
    input_buffer = sys.stdin.buffer
    n, m, t = map(int, input_buffer.readline().split())
    active_nodes = list(map(int, input_buffer.readline().split()))

    if t == 1:
        print(0)
        return

    active = bytearray(n + 1)
    for node in active_nodes:
        active[node] = 1

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input_buffer.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    root = active_nodes[0]
    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = [root]
    parent[root] = -1

    for u in order:
        for v, w in graph[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                order.append(v)

    active_count = list(active)
    answer = 0

    for u in reversed(order):
        count = active_count[u]
        if u != root:
            if 0 < count < t:
                answer += parent_weight[u]
            active_count[parent[u]] += count

    print(answer)


if __name__ == "__main__":
    main()
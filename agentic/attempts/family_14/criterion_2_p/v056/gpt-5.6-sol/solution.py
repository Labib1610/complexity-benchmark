import sys


def solve():
    input = sys.stdin.buffer.readline
    n, m, t = map(int, input().split())

    centers = []
    while len(centers) < t:
        centers.extend(map(int, input().split()))

    if t == 1:
        print(0)
        return

    is_center = bytearray(n + 1)
    for node in centers:
        is_center[node] = 1

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    parent = [0] * (n + 1)
    parent_cost = [0] * (n + 1)
    order = [1]

    for u in order:
        for v, w in graph[u]:
            if v != parent[u]:
                parent[v] = u
                parent_cost[v] = w
                order.append(v)

    terminal_count = list(is_center)
    answer = 0

    for u in reversed(order[1:]):
        count = terminal_count[u]
        if 0 < count < t:
            answer += parent_cost[u]
        terminal_count[parent[u]] += count

    print(answer)


if __name__ == "__main__":
    solve()
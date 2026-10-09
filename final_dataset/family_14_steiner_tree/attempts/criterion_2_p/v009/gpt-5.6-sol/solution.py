import sys

def main():
    input = sys.stdin.buffer.readline

    n, m, t = map(int, input().split())
    required_nodes = list(map(int, input().split()))

    required = bytearray(n + 1)
    for node in required_nodes:
        required[node] = 1

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
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

    count = [0] * (n + 1)
    answer = 0

    for u in reversed(order):
        count[u] += required[u]
        if parent[u] != -1:
            if 0 < count[u] < t:
                answer += parent_weight[u]
            count[parent[u]] += count[u]

    print(answer)

if __name__ == "__main__":
    main()
import sys

def main():
    input = sys.stdin.buffer.readline
    n, m, t = map(int, input().split())

    contaminated = bytearray(n)
    found = 0
    while found < t:
        for x in map(int, input().split()):
            contaminated[x - 1] = 1
            found += 1

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))

    parent = [-1] * n
    parent_weight = [0] * n
    order = [0]

    for u in order:
        for v, w in graph[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                order.append(v)

    counts = list(contaminated)
    answer = 0

    for u in reversed(order[1:]):
        count = counts[u]
        if 0 < count < t:
            answer += parent_weight[u]
        counts[parent[u]] += count

    print(answer)

if __name__ == "__main__":
    main()
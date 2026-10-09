import sys

def main():
    input = sys.stdin.buffer.readline

    n, m, t = map(int, input().split())

    special = []
    while len(special) < t:
        special.extend(map(int, input().split()))

    marked = bytearray(n + 1)
    for node in special:
        marked[node] = 1

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    order = [1]

    for u in order:
        for v, w in graph[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            parent_weight[v] = w
            order.append(v)

    subtree_special = list(marked)
    answer = 0

    for u in reversed(order[1:]):
        count = subtree_special[u]
        if 0 < count < t:
            answer += parent_weight[u]
        subtree_special[parent[u]] += count

    print(answer)

if __name__ == "__main__":
    main()
import sys

def main():
    input = sys.stdin.buffer.readline
    n, m, t = map(int, input().split())

    selected = bytearray(n + 1)
    for node in map(int, input().split()):
        selected[node] = 1

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    if t <= 1:
        print(0)
        return

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    parent[1] = -1
    order = []
    stack = [1]

    while stack:
        u = stack.pop()
        order.append(u)
        for v, w in graph[u]:
            if v != parent[u]:
                parent[v] = u
                parent_weight[v] = w
                stack.append(v)

    subtree_selected = list(selected)
    answer = 0

    for u in reversed(order[1:]):
        count = subtree_selected[u]
        if 0 < count < t:
            answer += parent_weight[u]
        subtree_selected[parent[u]] += count

    print(answer)

if __name__ == "__main__":
    main()
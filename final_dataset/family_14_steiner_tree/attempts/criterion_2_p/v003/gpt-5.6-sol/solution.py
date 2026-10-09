import sys

def main():
    input = sys.stdin.buffer.readline

    n, m, t = map(int, input().split())

    required = []
    while len(required) < t:
        required.extend(map(int, input().split()))

    marked = bytearray(n + 1)
    for v in required:
        marked[v] = 1
    root = required[0]

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    parent = [0] * (n + 1)
    parent_weight = [0] * (n + 1)
    parent[root] = -1

    order = []
    stack = [root]

    while stack:
        v = stack.pop()
        order.append(v)
        for nxt, weight in graph[v]:
            if nxt != parent[v]:
                parent[nxt] = v
                parent_weight[nxt] = weight
                stack.append(nxt)

    answer = 0
    for i in range(len(order) - 1, 0, -1):
        v = order[i]
        if marked[v]:
            answer += parent_weight[v]
            marked[parent[v]] = 1

    print(answer)

if __name__ == "__main__":
    main()
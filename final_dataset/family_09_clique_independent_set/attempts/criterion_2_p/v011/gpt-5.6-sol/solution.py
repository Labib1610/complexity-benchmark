import sys
from collections import deque

def main():
    input = sys.stdin.buffer.readline
    n, m, k = map(int, input().split())

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n
    left = []
    right = []

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    queue.append(v)

    for u in range(n):
        if color[u] == 0:
            left.append(u)
        else:
            right.append(u)

    pair_u = [-1] * n
    pair_v = [-1] * n
    dist = [0] * n
    INF = n + 1

    def bfs():
        queue = deque()
        for u in left:
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF

        shortest = INF

        while queue:
            u = queue.popleft()
            if dist[u] >= shortest:
                continue

            next_dist = dist[u] + 1
            for v in graph[u]:
                matched_u = pair_v[v]
                if matched_u == -1:
                    shortest = next_dist
                elif dist[matched_u] == INF:
                    dist[matched_u] = next_dist
                    queue.append(matched_u)

        return shortest

    def augment(root, shortest, edge_pos):
        stack_u = [root]
        stack_v = []

        while stack_u:
            u = stack_u[-1]
            advanced = False

            while edge_pos[u] < len(graph[u]):
                v = graph[u][edge_pos[u]]
                edge_pos[u] += 1
                matched_u = pair_v[v]

                if matched_u == -1:
                    if dist[u] + 1 != shortest:
                        continue

                    pair_u[u] = v
                    pair_v[v] = u

                    for i in range(len(stack_v) - 1, -1, -1):
                        parent_u = stack_u[i]
                        edge_v = stack_v[i]
                        pair_u[parent_u] = edge_v
                        pair_v[edge_v] = parent_u

                    return True

                if dist[matched_u] == dist[u] + 1:
                    stack_u.append(matched_u)
                    stack_v.append(v)
                    advanced = True
                    break

            if not advanced:
                dist[u] = INF
                stack_u.pop()
                if stack_v:
                    stack_v.pop()

        return False

    matching_size = 0

    while True:
        shortest = bfs()
        if shortest == INF:
            break

        edge_pos = [0] * n
        for u in left:
            if pair_u[u] == -1 and augment(u, shortest, edge_pos):
                matching_size += 1

    if n - matching_size < k:
        print("NO")
        return

    reachable_left = bytearray(n)
    reachable_right = bytearray(n)
    queue = deque()

    for u in left:
        if pair_u[u] == -1:
            reachable_left[u] = 1
            queue.append(u)

    while queue:
        u = queue.popleft()
        matched_v = pair_u[u]

        for v in graph[u]:
            if v == matched_v or reachable_right[v]:
                continue

            reachable_right[v] = 1
            matched_u = pair_v[v]

            if matched_u != -1 and not reachable_left[matched_u]:
                reachable_left[matched_u] = 1
                queue.append(matched_u)

    answer = []

    for u in left:
        if reachable_left[u]:
            answer.append(u + 1)
            if len(answer) == k:
                break

    if len(answer) < k:
        for v in right:
            if not reachable_right[v]:
                answer.append(v + 1)
                if len(answer) == k:
                    break

    print("YES")
    print(*answer)

if __name__ == "__main__":
    main()
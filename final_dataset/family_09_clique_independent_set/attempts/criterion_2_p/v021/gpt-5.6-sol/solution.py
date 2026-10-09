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
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            next_color = color[u] ^ 1
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = next_color
                    queue.append(v)

    left = [u for u in range(n) if color[u] == 0]

    pair_left = [-1] * n
    pair_right = [-1] * n
    dist = [0] * n
    inf = n + 1
    matching = 0

    while True:
        queue = deque()
        for u in left:
            if pair_left[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = inf

        shortest = inf
        while queue:
            u = queue.popleft()
            if dist[u] >= shortest:
                continue
            next_dist = dist[u] + 1
            for v in graph[u]:
                matched_u = pair_right[v]
                if matched_u == -1:
                    shortest = next_dist
                elif dist[matched_u] == inf:
                    dist[matched_u] = next_dist
                    queue.append(matched_u)

        if shortest == inf:
            break

        iterator = [0] * n

        def augment(root):
            stack = [root]
            path_rights = []

            while stack:
                u = stack[-1]
                found_next = False
                adjacency = graph[u]

                while iterator[u] < len(adjacency):
                    v = adjacency[iterator[u]]
                    iterator[u] += 1
                    matched_u = pair_right[v]

                    if matched_u == -1:
                        if dist[u] + 1 != shortest:
                            continue

                        path_rights.append(v)
                        for lu, rv in zip(stack, path_rights):
                            pair_left[lu] = rv
                            pair_right[rv] = lu
                            iterator[lu] = 0
                        return True

                    if dist[matched_u] == dist[u] + 1:
                        path_rights.append(v)
                        stack.append(matched_u)
                        found_next = True
                        break

                if not found_next:
                    dist[u] = inf
                    stack.pop()
                    if path_rights:
                        path_rights.pop()

            return False

        augmented = 0
        for u in left:
            if pair_left[u] == -1 and augment(u):
                augmented += 1

        if augmented == 0:
            break
        matching += augmented

    if n - matching < k:
        sys.stdout.write("NO\n")
        return

    reachable_left = [False] * n
    reachable_right = [False] * n
    queue = deque()

    for u in left:
        if pair_left[u] == -1:
            reachable_left[u] = True
            queue.append(u)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if pair_left[u] == v or reachable_right[v]:
                continue
            reachable_right[v] = True
            matched_u = pair_right[v]
            if matched_u != -1 and not reachable_left[matched_u]:
                reachable_left[matched_u] = True
                queue.append(matched_u)

    answer = []
    for u in range(n):
        if color[u] == 0:
            if reachable_left[u]:
                answer.append(u + 1)
        elif not reachable_right[u]:
            answer.append(u + 1)

        if len(answer) == k:
            break

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)) + "\n")

if __name__ == "__main__":
    main()
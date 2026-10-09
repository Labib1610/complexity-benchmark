import sys
from collections import deque

def main():
    input_buffer = sys.stdin.buffer
    n, m, k = map(int, input_buffer.readline().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input_buffer.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    color = bytearray(b'\xff') * (n + 1)
    left = []
    right = []
    queue = deque()

    for start in range(1, n + 1):
        if color[start] != 255:
            continue

        color[start] = 0
        queue.append(start)

        while queue:
            u = queue.popleft()
            if color[u] == 0:
                left.append(u)
            else:
                right.append(u)

            next_color = color[u] ^ 1
            for v in graph[u]:
                if color[v] == 255:
                    color[v] = next_color
                    queue.append(v)

    pair_left = [0] * (n + 1)
    pair_right = [0] * (n + 1)
    dist = [0] * (n + 1)
    pointer = [0] * (n + 1)
    inf = n + 1
    matching_size = 0

    while True:
        queue.clear()
        shortest = inf

        for u in left:
            if pair_left[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = inf

        while queue:
            u = queue.popleft()
            du = dist[u]
            if du > shortest:
                continue

            for v in graph[u]:
                matched_left = pair_right[v]
                if matched_left == 0:
                    if du < shortest:
                        shortest = du
                elif du < shortest and dist[matched_left] == inf:
                    dist[matched_left] = du + 1
                    queue.append(matched_left)

        if shortest == inf:
            break

        for u in left:
            pointer[u] = 0

        for start in left:
            if pair_left[start] != 0 or dist[start] == inf:
                continue

            stack_left = [start]
            connector_right = []
            augmented = False

            while stack_left:
                u = stack_left[-1]
                adjacency = graph[u]
                advanced = False

                while pointer[u] < len(adjacency):
                    v = adjacency[pointer[u]]
                    pointer[u] += 1
                    matched_left = pair_right[v]

                    if matched_left == 0:
                        if dist[u] == shortest:
                            pair_left[u] = v
                            pair_right[v] = u

                            for i in range(len(connector_right) - 1, -1, -1):
                                previous_left = stack_left[i]
                                previous_right = connector_right[i]
                                pair_left[previous_left] = previous_right
                                pair_right[previous_right] = previous_left

                            matching_size += 1
                            augmented = True
                            break
                    elif (
                        dist[u] < shortest
                        and dist[matched_left] == dist[u] + 1
                    ):
                        connector_right.append(v)
                        stack_left.append(matched_left)
                        advanced = True
                        break

                if augmented:
                    break
                if advanced:
                    continue

                dist[u] = inf
                stack_left.pop()
                if connector_right:
                    connector_right.pop()

    if n - matching_size < k:
        sys.stdout.write("NO\n")
        return

    reachable_left = bytearray(n + 1)
    reachable_right = bytearray(n + 1)
    queue.clear()

    for u in left:
        if pair_left[u] == 0:
            reachable_left[u] = 1
            queue.append(u)

    while queue:
        u = queue.popleft()
        matched_v = pair_left[u]

        for v in graph[u]:
            if v == matched_v or reachable_right[v]:
                continue

            reachable_right[v] = 1
            matched_u = pair_right[v]
            if matched_u != 0 and not reachable_left[matched_u]:
                reachable_left[matched_u] = 1
                queue.append(matched_u)

    answer = []

    for u in left:
        if reachable_left[u]:
            answer.append(u)
            if len(answer) == k:
                break

    if len(answer) < k:
        for v in right:
            if not reachable_right[v]:
                answer.append(v)
                if len(answer) == k:
                    break

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)) + "\n")

if __name__ == "__main__":
    main()
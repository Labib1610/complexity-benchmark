import sys

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
        stack = [start]
        while stack:
            u = stack.pop()
            next_color = color[u] ^ 1
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = next_color
                    stack.append(v)

    left = [u for u in range(n) if color[u] == 0]
    right = [u for u in range(n) if color[u] == 1]

    pair = [-1] * n
    dist = [0] * n
    inf = n + 1
    matching = 0

    while True:
        queue = []
        for u in left:
            if pair[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = inf

        head = 0
        shortest = inf

        while head < len(queue):
            u = queue[head]
            head += 1

            if dist[u] >= shortest:
                continue

            next_dist = dist[u] + 1
            for v in graph[u]:
                matched_left = pair[v]
                if matched_left == -1:
                    if next_dist < shortest:
                        shortest = next_dist
                elif next_dist < shortest and dist[matched_left] == inf:
                    dist[matched_left] = next_dist
                    queue.append(matched_left)

        if shortest == inf:
            break

        ptr = [0] * n

        for root in left:
            if pair[root] != -1 or dist[root] != 0:
                continue

            stack = [root]
            connecting_right = []
            augmented = False

            while stack:
                u = stack[-1]
                descended = False

                while ptr[u] < len(graph[u]):
                    v = graph[u][ptr[u]]
                    ptr[u] += 1
                    matched_left = pair[v]
                    next_dist = dist[u] + 1

                    if matched_left == -1:
                        if next_dist == shortest:
                            pair[u] = v
                            pair[v] = u

                            for i in range(len(connecting_right) - 1, -1, -1):
                                parent = stack[i]
                                bridge = connecting_right[i]
                                pair[parent] = bridge
                                pair[bridge] = parent

                            augmented = True
                            break
                    elif next_dist < shortest and dist[matched_left] == next_dist:
                        connecting_right.append(v)
                        stack.append(matched_left)
                        descended = True
                        break

                if augmented:
                    break

                if descended:
                    continue

                dist[u] = inf
                stack.pop()
                if connecting_right:
                    connecting_right.pop()

            if augmented:
                matching += 1

    if n - matching < k:
        sys.stdout.write("NO\n")
        return

    reachable_left = bytearray(n)
    reachable_right = bytearray(n)
    queue = []

    for u in left:
        if pair[u] == -1:
            reachable_left[u] = 1
            queue.append(u)

    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1

        matched_right = pair[u]
        for v in graph[u]:
            if v == matched_right:
                continue
            if not reachable_right[v]:
                reachable_right[v] = 1
                matched_left = pair[v]
                if matched_left != -1 and not reachable_left[matched_left]:
                    reachable_left[matched_left] = 1
                    queue.append(matched_left)

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

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)) + "\n")

if __name__ == "__main__":
    main()
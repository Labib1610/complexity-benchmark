import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    graph = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        graph[u].append(v)
        graph[v].append(u)

    UNSEEN = 2
    color = bytearray([UNSEEN]) * n
    left = []
    initial_independent = []

    for start in range(n):
        if color[start] != UNSEEN:
            continue

        color[start] = 0
        q = deque([start])
        part0 = []
        part1 = []

        while q:
            u = q.popleft()
            if color[u] == 0:
                part0.append(u)
            else:
                part1.append(u)

            next_color = color[u] ^ 1
            for v in graph[u]:
                if color[v] == UNSEEN:
                    color[v] = next_color
                    q.append(v)

        left.extend(part0)
        if len(part0) >= len(part1):
            initial_independent.extend(part0)
        else:
            initial_independent.extend(part1)

    if len(initial_independent) >= k:
        answer = initial_independent[:k]
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(v + 1) for v in answer))
        sys.stdout.write("\n")
        return

    initial_independent = None

    pair = [-1] * n
    dist = [0] * n
    inf = n + 1
    shortest = inf

    def bfs():
        nonlocal shortest
        q = deque()
        for u in left:
            if pair[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = inf

        shortest = inf

        while q:
            u = q.popleft()
            du = dist[u]
            if du >= shortest:
                continue

            for v in graph[u]:
                matched_left = pair[v]
                if matched_left == -1:
                    shortest = du + 1
                elif dist[matched_left] == inf:
                    dist[matched_left] = du + 1
                    q.append(matched_left)

        return shortest != inf

    def dfs(u):
        for v in graph[u]:
            matched_left = pair[v]

            if matched_left == -1:
                if dist[u] + 1 != shortest:
                    continue
            elif dist[matched_left] != dist[u] + 1 or not dfs(matched_left):
                continue

            pair[u] = v
            pair[v] = u
            return True

        dist[u] = inf
        return False

    matching_size = 0
    maximum_allowed_matching = n - k

    while bfs():
        for u in left:
            if pair[u] == -1 and dfs(u):
                matching_size += 1
                if matching_size > maximum_allowed_matching:
                    sys.stdout.write("NO\n")
                    return

    reachable = bytearray(n)
    q = deque()

    for u in left:
        if pair[u] == -1:
            reachable[u] = 1
            q.append(u)

    while q:
        u = q.popleft()
        matched_right = pair[u]

        for v in graph[u]:
            if v == matched_right or reachable[v]:
                continue

            reachable[v] = 1
            matched_left = pair[v]
            if matched_left != -1 and not reachable[matched_left]:
                reachable[matched_left] = 1
                q.append(matched_left)

    answer = []

    for u in left:
        if reachable[u]:
            answer.append(u)
            if len(answer) == k:
                break

    if len(answer) < k:
        for v in range(n):
            if color[v] == 1 and not reachable[v]:
                answer.append(v)
                if len(answer) == k:
                    break

    if len(answer) < k:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(v + 1) for v in answer))
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
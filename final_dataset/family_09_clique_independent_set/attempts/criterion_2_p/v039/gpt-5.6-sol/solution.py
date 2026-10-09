import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m, k = data[0], data[1], data[2]
    adj = [[] for _ in range(n)]

    p = 3
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        adj[u].append(v)
        adj[v].append(u)
    del data

    # Recover a bipartition.
    color = [-1] * n
    queue = []
    head = 0

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue.append(start)

        while head < len(queue):
            u = queue[head]
            head += 1
            next_color = color[u] ^ 1
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = next_color
                    queue.append(v)

    left = [u for u in range(n) if color[u] == 0]

    # Hopcroft-Karp maximum matching.
    pair = [-1] * n
    matching = 0
    INF = n + 1

    while True:
        dist = [INF] * n
        bfs_queue = []
        bfs_head = 0

        for u in left:
            if pair[u] == -1:
                dist[u] = 0
                bfs_queue.append(u)

        shortest = INF

        while bfs_head < len(bfs_queue):
            u = bfs_queue[bfs_head]
            bfs_head += 1

            if dist[u] >= shortest:
                continue

            nd = dist[u] + 1
            for v in adj[u]:
                w = pair[v]
                if w == -1:
                    if nd < shortest:
                        shortest = nd
                elif dist[w] == INF:
                    dist[w] = nd
                    bfs_queue.append(w)

        if shortest == INF:
            break

        ptr = [0] * n
        augmented_this_phase = 0

        for root in left:
            if pair[root] != -1 or dist[root] != 0:
                continue

            stack_u = [root]
            stack_v = []
            found = False

            while stack_u:
                u = stack_u[-1]
                neighbors = adj[u]
                advanced = False

                while ptr[u] < len(neighbors):
                    v = neighbors[ptr[u]]
                    ptr[u] += 1
                    w = pair[v]

                    if w == -1:
                        if dist[u] + 1 != shortest:
                            continue

                        pair[u] = v
                        pair[v] = u

                        for i in range(len(stack_v) - 1, -1, -1):
                            pu = stack_u[i]
                            pv = stack_v[i]
                            pair[pu] = pv
                            pair[pv] = pu

                        found = True
                        break

                    if dist[u] + 1 < shortest and dist[w] == dist[u] + 1:
                        stack_v.append(v)
                        stack_u.append(w)
                        advanced = True
                        break

                if found:
                    break
                if advanced:
                    continue

                dist[u] = INF
                stack_u.pop()
                if stack_v:
                    stack_v.pop()

            if found:
                augmented_this_phase += 1

        if augmented_this_phase == 0:
            break
        matching += augmented_this_phase

    if n - matching < k:
        sys.stdout.write("NO\n")
        return

    # Find vertices reachable from unmatched left vertices by alternating paths.
    reachable_left = bytearray(n)
    reachable_right = bytearray(n)
    alt_queue = []
    alt_head = 0

    for u in left:
        if pair[u] == -1:
            reachable_left[u] = 1
            alt_queue.append(u)

    while alt_head < len(alt_queue):
        u = alt_queue[alt_head]
        alt_head += 1
        matched_v = pair[u]

        for v in adj[u]:
            if v == matched_v:
                continue
            if reachable_right[v]:
                continue

            reachable_right[v] = 1
            w = pair[v]
            if w != -1 and not reachable_left[w]:
                reachable_left[w] = 1
                alt_queue.append(w)

    # Complement of a minimum vertex cover:
    # reachable left vertices plus unreachable right vertices.
    answer = []

    for u in left:
        if reachable_left[u]:
            answer.append(u + 1)
            if len(answer) == k:
                break

    if len(answer) < k:
        for v in range(n):
            if color[v] == 1 and not reachable_right[v]:
                answer.append(v + 1)
                if len(answer) == k:
                    break

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)) + "\n")

if __name__ == "__main__":
    main()
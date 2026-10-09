import sys

def read_ints(data):
    num = 0
    in_num = False
    for c in data:
        if 48 <= c <= 57:
            num = num * 10 + c - 48
            in_num = True
        elif in_num:
            yield num
            num = 0
            in_num = False
    if in_num:
        yield num

def main():
    data = sys.stdin.buffer.read()
    it = iter(read_ints(data))

    n = next(it)
    m = next(it)
    k = next(it)

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)

    del it, data

    color = bytearray(b'\xff') * n
    count = [0, 0]
    queue = []

    for start in range(n):
        if color[start] != 255:
            continue
        color[start] = 0
        count[0] += 1
        queue.clear()
        queue.append(start)
        head = 0

        while head < len(queue):
            u = queue[head]
            head += 1
            nc = color[u] ^ 1
            for v in adj[u]:
                if color[v] == 255:
                    color[v] = nc
                    count[nc] += 1
                    queue.append(v)

    larger_color = 0 if count[0] >= count[1] else 1
    if count[larger_color] >= k:
        answer = []
        for v in range(n):
            if color[v] == larger_color:
                answer.append(v + 1)
                if len(answer) == k:
                    break
        sys.stdout.write("YES\n" + " ".join(map(str, answer)))
        return

    left_color = 0 if count[0] <= count[1] else 1
    left = [v for v in range(n) if color[v] == left_color]

    pair = [-1] * n
    dist = [-1] * n
    ptr = [0] * n
    matching = 0
    maximum_allowed = n - k

    while True:
        queue.clear()
        for u in left:
            ptr[u] = 0
            if pair[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1

        head = 0
        shortest = n + 1

        while head < len(queue):
            u = queue[head]
            head += 1
            du = dist[u]
            if du >= shortest:
                continue

            nd = du + 1
            for v in adj[u]:
                w = pair[v]
                if w == -1:
                    if nd < shortest:
                        shortest = nd
                elif dist[w] == -1:
                    dist[w] = nd
                    queue.append(w)

        if shortest == n + 1:
            break

        for root in left:
            if pair[root] != -1 or dist[root] != 0:
                continue

            stack_u = [root]
            stack_v = []
            augmented = False

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

                        for j in range(len(stack_v) - 1, -1, -1):
                            pu = stack_u[j]
                            pv = stack_v[j]
                            pair[pu] = pv
                            pair[pv] = pu

                        augmented = True
                        break

                    if dist[w] == dist[u] + 1:
                        stack_v.append(v)
                        stack_u.append(w)
                        advanced = True
                        break

                if augmented:
                    break
                if advanced:
                    continue

                dist[u] = -1
                stack_u.pop()
                if stack_v:
                    stack_v.pop()

            if augmented:
                matching += 1
                if matching > maximum_allowed:
                    sys.stdout.write("NO")
                    return

    seen = bytearray(n)
    queue.clear()

    for u in left:
        if pair[u] == -1:
            seen[u] = 1
            queue.append(u)

    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1

        for v in adj[u]:
            if pair[u] == v:
                continue
            if seen[v]:
                continue

            seen[v] = 1
            w = pair[v]
            if w != -1 and not seen[w]:
                seen[w] = 1
                queue.append(w)

    answer = []
    for v in range(n):
        if color[v] == left_color:
            if seen[v]:
                answer.append(v + 1)
        elif not seen[v]:
            answer.append(v + 1)

        if len(answer) == k:
            break

    if len(answer) < k:
        sys.stdout.write("NO")
    else:
        sys.stdout.write("YES\n" + " ".join(map(str, answer)))

if __name__ == "__main__":
    main()
import sys

def ints_from_bytes(data):
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
    it = iter(ints_from_bytes(data))

    n = next(it)
    m = next(it)
    k = next(it)

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = bytearray([255]) * n
    left = []
    right = []

    for start in range(n):
        if color[start] != 255:
            continue
        color[start] = 0
        queue = [start]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            if color[u] == 0:
                left.append(u)
            else:
                right.append(u)
            next_color = color[u] ^ 1
            for v in adj[u]:
                if color[v] == 255:
                    color[v] = next_color
                    queue.append(v)

    match_left = [-1] * n
    match_right = [-1] * n
    dist = [-1] * n

    while True:
        queue = []
        for u in left:
            if match_left[u] == -1:
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
            if du + 1 > shortest:
                continue
            for v in adj[u]:
                w = match_right[v]
                if w == -1:
                    if du + 1 < shortest:
                        shortest = du + 1
                elif dist[w] == -1:
                    dist[w] = du + 1
                    queue.append(w)

        if shortest == n + 1:
            break

        augmented = 0

        for root in left:
            if match_left[root] != -1 or dist[root] != 0:
                continue

            stack = [root]
            edge_pos = [0]
            path_rights = []
            found = False

            while stack:
                u = stack[-1]
                descended = False

                while edge_pos[-1] < len(adj[u]):
                    v = adj[u][edge_pos[-1]]
                    edge_pos[-1] += 1
                    w = match_right[v]

                    if w == -1:
                        if dist[u] + 1 == shortest:
                            rights = path_rights + [v]
                            for lu, rv in zip(stack, rights):
                                match_left[lu] = rv
                                match_right[rv] = lu
                            found = True
                            break
                    elif dist[w] == dist[u] + 1:
                        stack.append(w)
                        edge_pos.append(0)
                        path_rights.append(v)
                        descended = True
                        break

                if found:
                    break
                if descended:
                    continue

                dist[u] = -1
                stack.pop()
                edge_pos.pop()
                if len(path_rights) >= len(stack):
                    path_rights.pop()

            if found:
                augmented += 1

        if augmented == 0:
            break

    reachable_left = bytearray(n)
    reachable_right = bytearray(n)
    queue = []

    for u in left:
        if match_left[u] == -1:
            reachable_left[u] = 1
            queue.append(u)

    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        matched_v = match_left[u]

        for v in adj[u]:
            if v == matched_v:
                continue
            if not reachable_right[v]:
                reachable_right[v] = 1
                w = match_right[v]
                if w != -1 and not reachable_left[w]:
                    reachable_left[w] = 1
                    queue.append(w)

    independent = []
    for u in left:
        if reachable_left[u]:
            independent.append(u + 1)
    for v in right:
        if not reachable_right[v]:
            independent.append(v + 1)

    if len(independent) < k:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, independent[:k])) + "\n")

if __name__ == "__main__":
    main()
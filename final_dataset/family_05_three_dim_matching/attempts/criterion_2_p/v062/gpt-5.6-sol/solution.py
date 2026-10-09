import sys

def main():
    lines = sys.stdin.buffer.read().splitlines()
    if not lines:
        return

    k, t = map(int, lines[0].split())
    adj = [[] for _ in range(k + 1)]
    azimuthal = [0] * (k + 1)

    pair_u = [0] * (k + 1)
    pair_v = [0] * (k + 1)
    matched = 0

    for line in lines[1:]:
        p, a, m = map(int, line.split())
        adj[p].append(m)
        azimuthal[p] = a

        if pair_u[p] == 0 and pair_v[m] == 0:
            pair_u[p] = m
            pair_v[m] = p
            matched += 1

    del lines

    if matched < k:
        sys.setrecursionlimit(3 * k + 100)
        dist = [-1] * (k + 1)
        ptr = [0] * (k + 1)

        while matched < k:
            queue = []
            for u in range(1, k + 1):
                if pair_u[u] == 0:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = -1

            shortest = k + 1

            for u in queue:
                if dist[u] >= shortest:
                    continue
                next_dist = dist[u] + 1
                for v in adj[u]:
                    other = pair_v[v]
                    if other == 0:
                        shortest = next_dist
                    elif dist[other] == -1:
                        dist[other] = next_dist
                        queue.append(other)

            if shortest == k + 1:
                break

            ptr[:] = [0] * (k + 1)

            def dfs(u):
                next_dist = dist[u] + 1
                edges = adj[u]
                i = ptr[u]

                while i < len(edges):
                    v = edges[i]
                    i += 1
                    ptr[u] = i
                    other = pair_v[v]

                    if other == 0:
                        if next_dist != shortest:
                            continue
                    elif dist[other] != next_dist or not dfs(other):
                        continue

                    pair_u[u] = v
                    pair_v[v] = u
                    return True

                dist[u] = -1
                return False

            augmented = 0
            for u in range(1, k + 1):
                if pair_u[u] == 0 and dfs(u):
                    augmented += 1

            if augmented == 0:
                break
            matched += augmented

    if matched != k:
        sys.stdout.write("NO\n")
        return

    output = ["YES"]
    output.extend(
        f"{p} {azimuthal[p]} {pair_u[p]}"
        for p in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
import sys

sys.setrecursionlimit(10000)


def main():
    inp = sys.stdin.buffer
    first = inp.readline().split()
    if not first:
        return

    k, t = map(int, first)
    if t < k:
        print("NO")
        return

    adj = [[] for _ in range(k + 1)]
    vehicle = [0] * (k + 1)
    match_route = [0] * (k + 1)
    match_driver = [0] * (k + 1)
    matched = 0

    for _ in range(t):
        x, y, z = map(int, inp.readline().split())
        adj[x].append(z)
        vehicle[x] = y

        if match_route[x] == 0 and match_driver[z] == 0:
            match_route[x] = z
            match_driver[z] = x
            matched += 1

    if matched < k:
        inf = k + 1
        dist = [inf] * (k + 1)

        def bfs():
            queue = []
            for u in range(1, k + 1):
                if match_route[u] == 0:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = inf

            dist[0] = inf
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                if dist[u] >= dist[0]:
                    continue
                next_dist = dist[u] + 1
                for v in adj[u]:
                    paired_route = match_driver[v]
                    if dist[paired_route] == inf:
                        dist[paired_route] = next_dist
                        if paired_route != 0:
                            queue.append(paired_route)

            return dist[0] != inf

        def dfs(u):
            next_dist = dist[u] + 1
            for v in adj[u]:
                paired_route = match_driver[v]
                if dist[paired_route] == next_dist and (
                    paired_route == 0 or dfs(paired_route)
                ):
                    match_route[u] = v
                    match_driver[v] = u
                    return True
            dist[u] = inf
            return False

        while matched < k and bfs():
            for u in range(1, k + 1):
                if match_route[u] == 0 and dfs(u):
                    matched += 1

    if matched != k:
        print("NO")
        return

    output = ["YES"]
    output.extend(
        f"{x} {vehicle[x]} {match_route[x]}"
        for x in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
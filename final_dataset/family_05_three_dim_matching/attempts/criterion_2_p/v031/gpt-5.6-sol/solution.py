import sys

def main():
    input_line = sys.stdin.buffer.readline
    k, t = map(int, input_line().split())

    adj = [[] for _ in range(k)]
    alias = [0] * k
    match_x = [-1] * k
    match_z = [-1] * k
    matched = 0

    for _ in range(t):
        x, y, z = map(int, input_line().split())
        x -= 1
        z -= 1
        alias[x] = y
        adj[x].append(z)

        if match_x[x] == -1 and match_z[z] == -1:
            match_x[x] = z
            match_z[z] = x
            matched += 1

    sys.setrecursionlimit(10000)
    inf = k + 1
    dist = [inf] * k

    while matched < k:
        queue = []
        for x in range(k):
            if match_x[x] == -1:
                dist[x] = 0
                queue.append(x)
            else:
                dist[x] = inf

        head = 0
        shortest = inf

        while head < len(queue):
            x = queue[head]
            head += 1

            if dist[x] >= shortest:
                continue

            next_dist = dist[x] + 1
            for z in adj[x]:
                other = match_z[z]
                if other == -1:
                    shortest = next_dist
                elif dist[other] == inf:
                    dist[other] = next_dist
                    queue.append(other)

        if shortest == inf:
            break

        def dfs(x):
            next_dist = dist[x] + 1
            for z in adj[x]:
                other = match_z[z]
                if other == -1:
                    if next_dist != shortest:
                        continue
                elif dist[other] != next_dist or not dfs(other):
                    continue

                match_x[x] = z
                match_z[z] = x
                return True

            dist[x] = inf
            return False

        augmented = 0
        for x in range(k):
            if match_x[x] == -1 and dfs(x):
                augmented += 1

        if augmented == 0:
            break
        matched += augmented

    if matched != k:
        sys.stdout.write("NO\n")
        return

    output = ["YES"]
    for x in range(k):
        output.append(f"{x + 1} {alias[x]} {match_x[x] + 1}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
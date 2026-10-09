import sys
from collections import deque

def main():
    read = sys.stdin.buffer.readline
    k, t = map(int, read().split())

    adj = [[] for _ in range(k + 1)]
    y_for_x = [0] * (k + 1)
    match_x = [0] * (k + 1)
    match_z = [0] * (k + 1)
    matched = 0

    for _ in range(t):
        x, y, z = map(int, read().split())
        adj[x].append(z)
        y_for_x[x] = y

        if match_x[x] == 0 and match_z[z] == 0:
            match_x[x] = z
            match_z[z] = x
            matched += 1

    if any(y_for_x[x] == 0 for x in range(1, k + 1)):
        print("NO")
        return

    sys.setrecursionlimit(5000)
    INF = k + 1

    while matched < k:
        dist = [INF] * (k + 1)
        queue = deque()

        for x in range(1, k + 1):
            if match_x[x] == 0:
                dist[x] = 0
                queue.append(x)

        shortest = INF

        while queue:
            x = queue.popleft()
            next_dist = dist[x] + 1

            if next_dist > shortest:
                continue

            for z in adj[x]:
                other_x = match_z[z]
                if other_x == 0:
                    shortest = next_dist
                elif dist[other_x] == INF:
                    dist[other_x] = next_dist
                    queue.append(other_x)

        if shortest == INF:
            break

        edge_pos = [0] * (k + 1)

        def dfs(x):
            next_dist = dist[x] + 1
            edges = adj[x]
            pos = edge_pos[x]

            while pos < len(edges):
                z = edges[pos]
                pos += 1
                edge_pos[x] = pos
                other_x = match_z[z]

                if other_x == 0:
                    if next_dist == shortest:
                        match_x[x] = z
                        match_z[z] = x
                        return True
                elif dist[other_x] == next_dist and dfs(other_x):
                    match_x[x] = z
                    match_z[z] = x
                    return True

            dist[x] = INF
            return False

        augmented = 0
        for x in range(1, k + 1):
            if match_x[x] == 0 and dfs(x):
                augmented += 1

        if augmented == 0:
            break
        matched += augmented

    if matched != k:
        print("NO")
        return

    output = ["YES"]
    output.extend(
        f"{x} {y_for_x[x]} {match_x[x]}"
        for x in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
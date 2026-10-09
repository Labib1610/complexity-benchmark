import sys
from collections import deque

def main():
    input_line = sys.stdin.buffer.readline
    k, t = map(int, input_line().split())

    adjacency = [[] for _ in range(k + 1)]
    machine = [0] * (k + 1)

    for _ in range(t):
        x, y, z = map(int, input_line().split())
        adjacency[x].append(z)
        if machine[x] == 0:
            machine[x] = y

    seen_machines = bytearray(k + 1)
    for x in range(1, k + 1):
        y = machine[x]
        if y == 0 or seen_machines[y]:
            print("NO")
            return
        seen_machines[y] = 1

    match_x = [0] * (k + 1)
    match_z = [0] * (k + 1)

    # Build an initial greedy matching.
    for x in range(1, k + 1):
        for z in adjacency[x]:
            if match_z[z] == 0:
                match_x[x] = z
                match_z[z] = x
                break

    inf = k + 1
    distance = [inf] * (k + 1)
    edge_index = [0] * (k + 1)

    sys.setrecursionlimit(10000)

    def bfs():
        queue = deque()
        for x in range(1, k + 1):
            if match_x[x] == 0:
                distance[x] = 0
                queue.append(x)
            else:
                distance[x] = inf

        distance[0] = inf

        while queue:
            x = queue.popleft()
            if distance[x] >= distance[0]:
                continue

            next_distance = distance[x] + 1
            for z in adjacency[x]:
                other_x = match_z[z]
                if other_x == 0:
                    if next_distance < distance[0]:
                        distance[0] = next_distance
                elif distance[other_x] == inf:
                    distance[other_x] = next_distance
                    queue.append(other_x)

        return distance[0] != inf

    def dfs(x):
        if x == 0:
            return True

        edges = adjacency[x]
        i = edge_index[x]

        while i < len(edges):
            z = edges[i]
            i += 1
            edge_index[x] = i
            other_x = match_z[z]

            if distance[other_x] == distance[x] + 1 and dfs(other_x):
                match_x[x] = z
                match_z[z] = x
                return True

        distance[x] = inf
        return False

    matched = sum(1 for x in range(1, k + 1) if match_x[x] != 0)

    while matched < k and bfs():
        edge_index = [0] * (k + 1)
        for x in range(1, k + 1):
            if match_x[x] == 0 and dfs(x):
                matched += 1

    if matched != k:
        print("NO")
        return

    output = ["YES"]
    output.extend(
        f"{x} {machine[x]} {match_x[x]}"
        for x in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
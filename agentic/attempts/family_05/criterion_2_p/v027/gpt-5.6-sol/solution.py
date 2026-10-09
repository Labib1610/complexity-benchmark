import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer
    first = input_data.readline().split()
    if not first:
        return

    k, t = map(int, first)
    adjacency = [[] for _ in range(k + 1)]
    receptor = [0] * (k + 1)

    for _ in range(t):
        x, y, z = map(int, input_data.readline().split())
        adjacency[x].append(z)
        receptor[x] = y

    if t < k or any(not adjacency[x] for x in range(1, k + 1)):
        print("NO")
        return

    match_left = [0] * (k + 1)
    match_right = [0] * (k + 1)
    distance = [0] * (k + 1)
    inf = k + 1

    sys.setrecursionlimit(2 * k + 100)

    def bfs():
        queue = deque()
        for x in range(1, k + 1):
            if match_left[x] == 0:
                distance[x] = 0
                queue.append(x)
            else:
                distance[x] = inf

        shortest = inf
        while queue:
            x = queue.popleft()
            if distance[x] >= shortest:
                continue
            next_distance = distance[x] + 1
            for z in adjacency[x]:
                other = match_right[z]
                if other == 0:
                    shortest = next_distance
                elif distance[other] == inf:
                    distance[other] = next_distance
                    queue.append(other)
        return shortest

    def dfs(x, shortest):
        next_distance = distance[x] + 1
        for z in adjacency[x]:
            other = match_right[z]
            if other == 0:
                if next_distance != shortest:
                    continue
            elif distance[other] != next_distance or not dfs(other, shortest):
                continue

            match_left[x] = z
            match_right[z] = x
            return True

        distance[x] = inf
        return False

    matching_size = 0
    while True:
        shortest = bfs()
        if shortest == inf:
            break
        for x in range(1, k + 1):
            if match_left[x] == 0 and dfs(x, shortest):
                matching_size += 1

    if matching_size != k:
        print("NO")
        return

    output = ["YES"]
    output.extend(
        f"{x} {receptor[x]} {match_left[x]}"
        for x in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
import sys
from collections import deque

def main():
    input_buffer = sys.stdin.buffer
    first = input_buffer.readline().split()
    if not first:
        return

    k, t = map(int, first)
    adjacency = [[] for _ in range(k + 1)]
    slot = [0] * (k + 1)

    for _ in range(t):
        x, y, z = map(int, input_buffer.readline().split())
        slot[x] = y
        adjacency[x].append(z)

    if t < k or any(not adjacency[x] for x in range(1, k + 1)):
        print("NO")
        return

    sys.setrecursionlimit(10000)

    match_satellite = [0] * (k + 1)
    match_frequency = [0] * (k + 1)
    distance = [-1] * (k + 1)
    pointer = [0] * (k + 1)
    infinity = k + 1

    def bfs():
        queue = deque()
        for x in range(1, k + 1):
            if match_satellite[x] == 0:
                distance[x] = 0
                queue.append(x)
            else:
                distance[x] = -1

        shortest = infinity

        while queue:
            x = queue.popleft()
            next_distance = distance[x] + 1
            if next_distance > shortest:
                continue

            for z in adjacency[x]:
                other = match_frequency[z]
                if other == 0:
                    shortest = next_distance
                elif next_distance < shortest and distance[other] == -1:
                    distance[other] = next_distance
                    queue.append(other)

        return shortest

    def dfs(x, shortest):
        edges = adjacency[x]
        i = pointer[x]

        while i < len(edges):
            z = edges[i]
            i += 1
            pointer[x] = i
            other = match_frequency[z]

            if other == 0:
                if distance[x] + 1 != shortest:
                    continue
            elif distance[other] != distance[x] + 1 or not dfs(other, shortest):
                continue

            match_satellite[x] = z
            match_frequency[z] = x
            return True

        distance[x] = -1
        return False

    matched = 0

    while True:
        shortest = bfs()
        if shortest == infinity:
            break

        pointer = [0] * (k + 1)
        for x in range(1, k + 1):
            if match_satellite[x] == 0 and dfs(x, shortest):
                matched += 1

    if matched != k:
        print("NO")
        return

    output = ["YES"]
    output.extend(
        f"{x} {slot[x]} {match_satellite[x]}"
        for x in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()